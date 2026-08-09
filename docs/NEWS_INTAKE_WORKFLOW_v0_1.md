# News Intake Workflow v0.1

## Purpose

The intake workflow watches a small, explicit registry of public feeds and produces a short-lived review artifact. It reduces repetitive discovery work without converting an external headline into a lattice claim or committing collected items to the repository.

## State boundary

```text
external feed
  -> intake candidate
  -> human source review
  -> source/story record
  -> node and relation review
  -> spread or rendition review
  -> publication
```

Only the first arrow is automated by this repository.

An intake candidate means only: "this feed exposed an item with this title, URL, and date." It does not mean the item is true, important, safe to quote, independent, complete, or suitable for publication.

## Automated stage

The scheduled GitHub Actions workflow:

1. checks out the default branch with read-only repository permissions;
2. runs the collector tests;
3. reads enabled entries from `registries/FEEDS.json`;
4. fetches bounded RSS or Atom payloads;
5. keeps title, URL, published date, feed provenance, and configured review lenses;
6. deduplicates candidates by stable URL;
7. uploads JSON Lines, feed status, and a Markdown review packet as a short-lived workflow artifact.

Configured lenses are review prompts, not classifications. The seed registry does not automatically assign lattice hashtags; tags require separate record-level review against the active hashtag registry.

It does not:

- scrape article bodies;
- summarize or classify the article's claims;
- infer culpability, motive, ideology, or threat status;
- create or promote nodes or relations;
- edit the repository;
- open issues or pull requests;
- publish a spread or rendition.

## Human review stage

Before a candidate can become a source or story record, a reviewer should:

- open the canonical URL and confirm publisher, date, and document identity;
- distinguish primary evidence, institutional statement, reporting, analysis, and opinion;
- inspect rights, quotation, privacy, and safety constraints;
- record relevant claim posture and missing evidence;
- compare independent or materially different sources where the claim warrants it;
- identify applicable lenses without forcing a node into existence;
- either reject the candidate, defer it, or create a separately reviewed record.

## Failure behavior

Each feed records success or failure independently. A partial outage remains visible in `feed_status.json`; it must not silently erase candidates from other feeds. The workflow fails when every enabled feed fails, when the registry is invalid, or when the collector cannot write a complete packet.

## Rights boundary

The seed collector stores only limited discovery metadata. Third-party materials remain under their own terms. A public feed is not blanket permission to republish its contents, and a feed's presence in the registry is not an editorial endorsement.

The initial registry is intentionally a small primary-source lane. It is not a balanced news diet. Before consequential publication, reviewers should seek independent reporting, affected-community knowledge, and materially different evidence rather than allowing institutional feed availability to determine the lattice's field of view.

## Publication gate

Moving any intake result into tracked source, story, node, relation, spread, or rendition records is a separate editorial action. Consequential claims require human review under `EDITORIAL_STANDARD.md`; public corrections remain governed by `CORRECTIONS.md`.
