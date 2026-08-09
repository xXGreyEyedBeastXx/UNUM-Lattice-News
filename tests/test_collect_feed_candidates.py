import json
import tempfile
import unittest
from pathlib import Path

from scripts.collect_feed_candidates import (
    collect_candidates,
    parse_feed,
    render_review_packet,
    write_outputs,
)


FIXTURES = Path(__file__).parent / "fixtures"
COLLECTED_AT = "2026-08-09T12:00:00Z"


def feed(feed_id: str, url: str, lenses: list[str]) -> dict:
    return {
        "id": feed_id,
        "label": f"Feed {feed_id}",
        "publisher": "Example Public Institution",
        "url": url,
        "format": "rss_atom",
        "enabled": True,
        "source_kind": "official_test_source",
        "default_hashtags": ["#Test"],
        "default_lenses": lenses,
    }


class FeedCandidateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rss = (FIXTURES / "sample_rss.xml").read_bytes()
        self.atom = (FIXTURES / "sample_atom.xml").read_bytes()

    def test_parses_rss_without_copying_description(self) -> None:
        entries = parse_feed(self.rss, "https://example.gov/feed.xml")
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["title"], "Accessible transit review published")
        self.assertNotIn("description", entries[0])
        self.assertNotIn("body", entries[0])

    def test_parses_atom_and_removes_url_fragment(self) -> None:
        entries = parse_feed(self.atom, "https://example.gov/feed.atom")
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["url"], "https://example.gov/reports/accessible-transit")
        self.assertNotIn("summary", entries[0])

    def test_deduplicates_and_merges_feed_provenance_and_lenses(self) -> None:
        first_url = "https://example.gov/rss"
        second_url = "https://example.gov/atom"
        registry = {
            "feeds": [
                feed("oversight", first_url, ["law_governance_accountability"]),
                feed("health", second_url, ["health", "disability_accessibility"]),
            ]
        }
        payloads = {first_url: self.rss, second_url: self.atom}
        candidates, status = collect_candidates(
            registry,
            fetcher=payloads.__getitem__,
            collected_at=COLLECTED_AT,
        )

        self.assertEqual(len(candidates), 2)
        shared = next(item for item in candidates if item["url"].endswith("accessible-transit"))
        self.assertEqual(
            [item["feed_id"] for item in shared["discovered_via"]],
            ["oversight", "health"],
        )
        self.assertEqual(
            shared["default_lenses"],
            ["law_governance_accountability", "health", "disability_accessibility"],
        )
        self.assertEqual(status["successful_feed_count"], 2)
        self.assertEqual(status["feeds"][1]["duplicates_merged"], 1)

    def test_preserves_partial_feed_failure(self) -> None:
        good_url = "https://example.gov/good"
        bad_url = "https://example.gov/bad"
        registry = {
            "feeds": [
                feed("good", good_url, ["health"]),
                feed("bad", bad_url, ["culture"]),
            ]
        }

        def fetcher(url: str) -> bytes:
            if url == bad_url:
                raise TimeoutError("fixture timeout")
            return self.rss

        candidates, status = collect_candidates(
            registry, fetcher=fetcher, collected_at=COLLECTED_AT
        )
        self.assertEqual(len(candidates), 1)
        self.assertFalse(status["all_feeds_failed"])
        self.assertEqual(status["feeds"][1]["status"], "failed")
        self.assertIn("TimeoutError", status["feeds"][1]["error"])

    def test_writes_complete_review_artifact_set(self) -> None:
        url = "https://example.gov/rss"
        registry = {"feeds": [feed("one", url, ["health"])]}
        candidates, status = collect_candidates(
            registry,
            fetcher=lambda _: self.rss,
            collected_at=COLLECTED_AT,
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            write_outputs(output, candidates, status)
            self.assertEqual(
                {path.name for path in output.iterdir()},
                {"candidates.jsonl", "feed_status.json", "review_packet.md"},
            )
            candidate = json.loads((output / "candidates.jsonl").read_text(encoding="utf-8"))
            self.assertEqual(candidate["review_status"], "candidate_unreviewed")
            packet = render_review_packet(candidates, status)
            self.assertIn("headline is not an established claim", packet)


if __name__ == "__main__":
    unittest.main()
