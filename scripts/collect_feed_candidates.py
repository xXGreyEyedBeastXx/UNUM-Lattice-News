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
        "candidate_notes": "headline is not an established claim — requires editorial review before publication",
    }


def merge_candidate(existing: dict[str, Any], entry: dict[str, str], feed: dict[str, Any]) -> int:
    """Merge feed provenance into an existing candidate. Returns 1 if duplicate merged."""
    existing_feed_ids = {via["feed_id"] for via in existing["discovered_via"]}
    if feed["id"] not in existing_feed_ids:
        existing["discovered_via"].append(
            {
                "feed_id": feed["id"],
                "feed_label": feed["label"],
                "publisher": feed["publisher"],
                "source_kind": feed["source_kind"],
            }
        )
        append_unique(existing["default_hashtags"], feed.get("default_hashtags", []))
        append_unique(existing["default_lenses"], feed.get("default_lenses", []))
        return 1
    return 0


def collect_candidates(
    registry: dict[str, Any],
    fetcher: Callable[[str], bytes] = fetch_url,
    collected_at: str | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if collected_at is None:
        collected_at = utc_now()

    feeds = [f for f in registry.get("feeds", []) if f.get("enabled", True)]
    url_index: dict[str, dict[str, Any]] = {}
    feed_statuses: list[dict[str, Any]] = []
    successful = 0

    for feed in feeds:
        url = feed["url"]
        feed_status: dict[str, Any] = {"feed_id": feed["id"], "url": url, "duplicates_merged": 0}
        try:
            payload = fetcher(url)
            entries = parse_feed(payload, url)
            feed_status["status"] = "ok"
            feed_status["entry_count"] = len(entries)
            successful += 1
            for entry in entries:
                cid = stable_candidate_id(entry["url"])
                if cid in url_index:
                    merged = merge_candidate(url_index[cid], entry, feed)
                    feed_status["duplicates_merged"] = feed_status.get("duplicates_merged", 0) + merged
                else:
                    url_index[cid] = new_candidate(entry, feed, collected_at)
        except Exception as exc:
            feed_status["status"] = "failed"
            feed_status["error"] = f"{type(exc).__name__}: {exc}"

        feed_statuses.append(feed_status)

    candidates = list(url_index.values())
    status = {
        "collected_at": collected_at,
        "total_feed_count": len(feeds),
        "successful_feed_count": successful,
        "all_feeds_failed": len(feeds) > 0 and successful == 0,
        "total_candidates": len(candidates),
        "feeds": feed_statuses,
    }
    return candidates, status


def render_review_packet(candidates: list[dict[str, Any]], status: dict[str, Any]) -> str:
    lines: list[str] = [
        "# Feed Candidate Review Packet",
        "",
        f"**Collected at:** {status['collected_at']}",
        f"**Feeds processed:** {status['successful_feed_count']} / {status['total_feed_count']}",
        f"**Candidates found:** {status['total_candidates']}",
        "",
        "> **Editorial notice:** Each item below is a feed headline. A headline is not an established claim.",
        "> All items require editorial review before publication.",
        "",
        "---",
        "",
    ]
    for i, candidate in enumerate(candidates, 1):
        lines.append(f"## {i}. {candidate['title']}")
        lines.append(f"- **URL:** {candidate['url']}")
        if candidate.get("published"):
            lines.append(f"- **Published:** {candidate['published']}")
        lines.append(f"- **Collected at:** {candidate['collected_at']}")
        lines.append(f"- **Review status:** {candidate['review_status']}")
        lines.append(f"- **Lenses:** {', '.join(candidate['default_lenses']) or 'none'}")
        lines.append(f"- **Discovered via:** {', '.join(v['feed_id'] for v in candidate['discovered_via'])}")
        lines.append("")
    return "\n".join(lines)


def write_outputs(
    output_dir: Path,
    candidates: list[dict[str, Any]],
    status: dict[str, Any],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    candidates_path = output_dir / "candidates.jsonl"
    with candidates_path.open("w", encoding="utf-8") as fh:
        for candidate in candidates:
            fh.write(json.dumps(candidate, ensure_ascii=False) + "\n")

    status_path = output_dir / "feed_status.json"
    status_path.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")

    packet_path = output_dir / "review_packet.md"
    packet_path.write_text(render_review_packet(candidates, status), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="registries/FEEDS.json", help="Path to feed registry JSON")
    parser.add_argument("--output", default="intake/candidates", help="Output directory")
    args = parser.parse_args(argv)

    registry_path = Path(args.registry)
    if not registry_path.exists():
        print(f"ERROR: registry not found: {registry_path}", file=sys.stderr)
        return 1

    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    candidates, status = collect_candidates(registry)

    output_dir = Path(args.output)
    write_outputs(output_dir, candidates, status)

    print(f"Collected {status['total_candidates']} candidates from {status['successful_feed_count']} feeds.")
    if status["all_feeds_failed"]:
        print("WARNING: all feeds failed.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())