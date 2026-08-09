#!/usr/bin/env python3
"""Collect bounded RSS/Atom discovery metadata into a review-only packet."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterable


MAX_FEED_BYTES = 5 * 1024 * 1024
MAX_TITLE_CHARS = 500
USER_AGENT = "UNUM-Lattice-News-review-intake/0.1 (+https://github.com/xXGreyEyedBeastXx/UNUM-Lattice-News)"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def clean_text(value: str | None) -> str:
    return " ".join((value or "").split())


def first_text(element: ET.Element, names: Iterable[str]) -> str:
    wanted = {name.lower() for name in names}
    for child in element.iter():
        if child is element:
            continue
        if local_name(child.tag) in wanted:
            value = clean_text("".join(child.itertext()))
            if value:
                return value
    return ""


def canonical_http_url(value: str, base_url: str) -> str:
    candidate = urllib.parse.urljoin(base_url, clean_text(value))
    parsed = urllib.parse.urlsplit(candidate)
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
        return ""
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), parsed.path or "/", parsed.query, "")
    )


def entry_link(element: ET.Element, feed_url: str) -> str:
    fallbacks: list[str] = []
    for child in element.iter():
        name = local_name(child.tag)
        if name == "link":
            href = clean_text(child.attrib.get("href"))
            text_value = clean_text("".join(child.itertext()))
            value = href or text_value
            if not value:
                continue
            link = canonical_http_url(value, feed_url)
            if not link:
                continue
            rel = clean_text(child.attrib.get("rel")).lower()
            if not rel or rel == "alternate":
                return link
            fallbacks.append(link)
        elif name in {"guid", "id"}:
            identifier = clean_text("".join(child.itertext()))
            if urllib.parse.urlsplit(identifier).scheme.lower() in {"http", "https"}:
                link = canonical_http_url(identifier, feed_url)
                if link:
                    fallbacks.append(link)
    return fallbacks[0] if fallbacks else ""


def parse_feed(payload: bytes, feed_url: str) -> list[dict[str, str]]:
    root = ET.fromstring(payload)
    records: list[dict[str, str]] = []
    for element in root.iter():
        if local_name(element.tag) not in {"item", "entry"}:
            continue
        title = first_text(element, {"title"})[:MAX_TITLE_CHARS]
        link = entry_link(element, feed_url)
        if not title or not link:
            continue
        records.append(
            {
                "title": title,
                "url": link,
                "published": first_text(
                    element, {"published", "updated", "pubdate", "date"}
                ),
            }
        )
    return records


def fetch_url(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml;q=0.9",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = response.read(MAX_FEED_BYTES + 1)
    if len(payload) > MAX_FEED_BYTES:
        raise ValueError(f"feed exceeded {MAX_FEED_BYTES} bytes")
    return payload


def stable_candidate_id(url: str) -> str:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:20]
    return f"candidate-{digest}"


def append_unique(target: list[str], values: Iterable[str]) -> None:
    for value in values:
        if value and value not in target:
            target.append(value)


def new_candidate(entry: dict[str, str], feed: dict[str, Any], collected_at: str) -> dict[str, Any]:
    return {
        "schema": "unum-lattice-news/intake-candidate/v0.1",
        "id": stable_candidate_id(entry["url"]),
        "review_status": "candidate_unreviewed",
        "claim_posture": "unknown",
        "title": entry["title"],
        "url": entry["url"],
        "published": entry["published"] or None,
        "collected_at": collected_at,
        "discovered_via": [
            {
                "feed_id": feed["id"],
                "feed_label": feed["label"],
                "publisher": feed["publisher"],
                "source_kind": feed["source_kind"],
            }
        ],
        "default_hashtags": list(feed.get("default_hashtags", [])),
        "default_lenses": list(feed.get("default_lenses", [])),
        "candidate_nodes": [],
        "review_notes": [],
    }


def merge_discovery(candidate: dict[str, Any], feed: dict[str, Any]) -> None:
    feed_id = feed["id"]
    if all(item["feed_id"] != feed_id for item in candidate["discovered_via"]):
        candidate["discovered_via"].append(
            {
                "feed_id": feed_id,
                "feed_label": feed["label"],
                "publisher": feed["publisher"],
                "source_kind": feed["source_kind"],
            }
        )
    append_unique(candidate["default_hashtags"], feed.get("default_hashtags", []))
    append_unique(candidate["default_lenses"], feed.get("default_lenses", []))


def validate_registry(registry: dict[str, Any]) -> list[dict[str, Any]]:
    feeds = registry.get("feeds")
    if not isinstance(feeds, list):
        raise ValueError("registry.feeds must be a list")
    enabled = [feed for feed in feeds if feed.get("enabled") is True]
    if not enabled:
        raise ValueError("registry has no enabled feeds")
    required = {"id", "label", "publisher", "url", "format", "source_kind"}
    seen_ids: set[str] = set()
    for feed in enabled:
        missing = sorted(required - set(feed))
        if missing:
            raise ValueError(f"feed is missing required fields: {', '.join(missing)}")
        if feed["id"] in seen_ids:
            raise ValueError(f"duplicate feed id: {feed['id']}")
        seen_ids.add(feed["id"])
        if not canonical_http_url(feed["url"], feed["url"]):
            raise ValueError(f"feed has invalid HTTP(S) URL: {feed['id']}")
    return enabled


def collect_candidates(
    registry: dict[str, Any],
    fetcher: Callable[[str], bytes] = fetch_url,
    limit_per_feed: int = 25,
    collected_at: str | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if limit_per_feed < 1 or limit_per_feed > 200:
        raise ValueError("limit_per_feed must be between 1 and 200")

    timestamp = collected_at or utc_now()
    enabled_feeds = validate_registry(registry)
    by_url: dict[str, dict[str, Any]] = {}
    feed_status: list[dict[str, Any]] = []
    successful_feeds = 0

    for feed in enabled_feeds:
        status: dict[str, Any] = {
            "feed_id": feed["id"],
            "url": feed["url"],
            "status": "failed",
            "items_seen": 0,
            "items_added": 0,
            "duplicates_merged": 0,
            "error": None,
        }
        try:
            if feed["format"] != "rss_atom":
                raise ValueError(f"unsupported feed format: {feed['format']}")
            entries = parse_feed(fetcher(feed["url"]), feed["url"])
            status["items_seen"] = len(entries)
            for entry in entries[:limit_per_feed]:
                existing = by_url.get(entry["url"])
                if existing is None:
                    by_url[entry["url"]] = new_candidate(entry, feed, timestamp)
                    status["items_added"] += 1
                else:
                    merge_discovery(existing, feed)
                    status["duplicates_merged"] += 1
            status["status"] = "ok"
            successful_feeds += 1
        except Exception as exc:  # Preserve per-feed failure while other feeds continue.
            status["error"] = f"{type(exc).__name__}: {exc}"
        feed_status.append(status)

    candidates = list(by_url.values())
    status_packet = {
        "schema": "unum-lattice-news/feed-status/v0.1",
        "collected_at": timestamp,
        "enabled_feed_count": len(enabled_feeds),
        "successful_feed_count": successful_feeds,
        "candidate_count": len(candidates),
        "all_feeds_failed": successful_feeds == 0,
        "feeds": feed_status,
    }
    return candidates, status_packet


def markdown_text(value: object) -> str:
    return (
        str(value or "")
        .replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("[", "\\[")
        .replace("]", "\\]")
    )


def render_review_packet(candidates: list[dict[str, Any]], status: dict[str, Any]) -> str:
    lines = [
        "# News intake review packet",
        "",
        f"Collected: `{status['collected_at']}`",
        "",
        "> Discovery metadata only. Every item is unreviewed; a headline is not an established claim, node, relation, or publication decision.",
        "",
        "## Feed status",
        "",
        "| Feed | Status | Seen | Added | Merged | Error |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for feed in status["feeds"]:
        lines.append(
            f"| {markdown_text(feed['feed_id'])} | {markdown_text(feed['status'])} | "
            f"{feed['items_seen']} | {feed['items_added']} | {feed['duplicates_merged']} | "
            f"{markdown_text(feed['error'])} |"
        )

    lines.extend(["", f"## Candidates ({len(candidates)})", ""])
    if not candidates:
        lines.append("No candidates were collected.")
    for candidate in candidates:
        feeds = ", ".join(item["feed_id"] for item in candidate["discovered_via"])
        lenses = ", ".join(candidate["default_lenses"]) or "none configured"
        published = candidate["published"] or "date not supplied by feed"
        lines.extend(
            [
                f"### {markdown_text(candidate['title'])}",
                "",
                f"- Candidate: `{candidate['id']}`",
                f"- URL: {candidate['url']}",
                f"- Published: {markdown_text(published)}",
                f"- Discovered via: {markdown_text(feeds)}",
                f"- Review lenses: {markdown_text(lenses)}",
                "- Review status: `candidate_unreviewed`",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(output_dir: Path, candidates: list[dict[str, Any]], status: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    jsonl = "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in candidates)
    (output_dir / "candidates.jsonl").write_text(jsonl, encoding="utf-8", newline="\n")
    (output_dir / "feed_status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (output_dir / "review_packet.md").write_text(
        render_review_packet(candidates, status), encoding="utf-8", newline="\n"
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=Path("registries/FEEDS.json"))
    parser.add_argument("--output", type=Path, default=Path("artifacts/news-candidate-intake"))
    parser.add_argument("--limit-per-feed", type=int, default=25)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
        candidates, status = collect_candidates(
            registry, limit_per_feed=args.limit_per_feed
        )
        write_outputs(args.output, candidates, status)
    except Exception as exc:
        print(f"intake failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2

    print(
        f"collected {len(candidates)} candidates from "
        f"{status['successful_feed_count']}/{status['enabled_feed_count']} enabled feeds"
    )
    return 1 if status["all_feeds_failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
