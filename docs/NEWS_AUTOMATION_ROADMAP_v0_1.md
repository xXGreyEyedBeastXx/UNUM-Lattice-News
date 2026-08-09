# News Automation Roadmap v0.1

**Status:** implementation TODO

**Boundary:** automation may discover, organize, and draft. It may not establish consequential claims, promote nodes, or publish without the required review.

## Already present

- review-only RSS/Atom intake;
- bounded feed registry and source limitations;
- candidate deduplication and provenance merging;
- fixture tests and scheduled artifact workflow;
- spread lenses and candidate-node exposure fields;
- explicit separation between intake candidates and lattice records.

## 1. Canonical node model

Resolve the drift between `templates/NODE.yaml` and `schemas/LATTICE_RECORD_TEMPLATES_v0_1.yaml` before automated node work.

Proposed node families:

- `actor`
  - person;
  - institution;
  - collective or movement;
- `system`
  - technology;
  - platform;
  - infrastructure;
- `instrument`
  - policy;
  - law;
  - program;
  - contract;
- `event_action`;
- `place_jurisdiction`;
- `population_community`;
- `ecology_living_system`;
- `resource_flow`
  - money;
  - labor;
  - data;
  - land;
  - energy;
  - supply;
- `claim_proposition`;
- `ideology_cultural_frame`;
- `condition_consequence`;
- `response_repair`.

`actor` must also remain a relation role. A person or institution may be actor, funder, regulator, target, beneficiary, or affected party depending on the evidenced relation.

### Acceptance criteria

- one canonical registry defines node families and subtypes;
- node template and record schema consume the same vocabulary;
- migration aliases preserve existing `concept` and `proposition` records;
- validation rejects unknown types without rewriting archived records.

## 2. Anti-sprawl landing gate

Most extracted names should never become nodes.

```text
mention -> candidate -> landed node
```

### Mention

A story-local reference. It may carry normalized text, source position, possible aliases, and possible existing-node matches. It does not receive a durable node file.

### Candidate

A bounded proposal created when a mention is recurring, materially consequential, or necessary to express an evidenced relation. Candidates remain review objects.

### Landed node

A durable node accepted after review. Landing should normally require:

- stable, resolvable identity;
- more than incidental mention;
- at least two materially distinct story/source appearances, or one high-consequence primary record;
- a timeline contribution, evidenced relation, or durable consequence not represented elsewhere;
- alias and duplicate review;
- named reviewer decision.

### Required exceptions

- A high-consequence one-source event may create a candidate, never automatic promotion.
- Affected populations should not be fragmented into identity nodes merely because an article lists them.
- Ideological labels require evidence that the frame itself is materially operating; labels must not encode guilt by association.
- Empty landing results are valid. A spread does not owe the lattice new nodes.

## 3. Story drafting stage

Add a review-only story-draft packet between intake and nodes.

```text
intake candidate
-> source verification
-> duplicate/story-cluster check
-> bounded claim extraction
-> mentions and existing-node matches
-> candidate relations
-> lens coverage and missing perspectives
-> human review
```

The draft must preserve source URLs, dates, source kind, claim posture, quotation boundaries, counterevidence, and unknowns. Institutional feeds must not determine the entire field of view; seek independent reporting and affected-community knowledge before consequential publication.

## 4. Deterministic report builder

Generate draft reports from reviewed structured records before adding narrative generation.

Each report should assemble:

- bounded question and time window;
- what changed since the previous report;
- anchor stories and source provenance;
- established observations and stated claims;
- supported inferences, allegations, disputes, and unknowns;
- existing and candidate nodes;
- evidenced relations;
- relevant lenses and empty lenses;
- affected people, communities, ecologies, and material systems;
- counterevidence and evidence that would change the assessment;
- resistance, remedy, repair, refusal, exit, or appeal;
- correction and review status.

The deterministic output should be valid without an AI-written narrative. A later language-model pass may draft connective prose, but every paragraph must remain recoverable to the structured report fields and source pointers.

### Outputs

- machine-readable report JSON;
- human-readable Markdown;
- static HTML generated from the same report record;
- workflow status and validation results.

## 5. Report viewer

Build a lightweight static viewer before a database-backed application.

Minimum viewer features:

- report list by date and status;
- full report page with visible evidence posture;
- filters for node, lens, source kind, geography, and posture;
- node page showing stories, relations, timeline, unknowns, and corrections;
- relation links that display their evidence rather than only drawing an edge;
- clear separation of mentions, candidates, and landed nodes;
- comparison with the previous report;
- printable and accessible layout;
- no analytics or third-party scripts by default.

Initial delivery should be a downloadable workflow artifact. Public hosting requires a separate review of privacy, rights, accessibility, and publication authority.

## 6. Workflow sequence

```text
collect
-> validate feeds
-> produce intake artifact
-> verify and cluster sources
-> draft story packet
-> match mentions to existing nodes
-> propose candidates and relations
-> apply landing gate
-> validate structured report
-> render Markdown and HTML
-> upload review artifact
```

No workflow token should receive repository write permission until a separately reviewed requirement proves it necessary. The first report workflow should not commit generated reports, open issues, or publish a site.

## 7. Source coverage TODO

- retain working official primary-source feeds;
- resolve or replace blocked FTC automation routes without bypassing access controls;
- add independent investigative reporting;
- add disability-led and affected-community sources;
- add labor, care, ecological, local, and international sources;
- record ownership, funding, geography, language, and source limitations;
- measure which lenses and populations remain systematically absent.

Source quantity is not source diversity. Availability must not silently become editorial authority.

## Recommended implementation order

1. Canonical node registry and schema validation.
2. Mention/candidate/landed record templates and tests.
3. Story-draft packet and source-cluster review.
4. Deterministic report schema and renderer.
5. Static viewer and accessibility checks.
6. Review-only workflow integration.
7. Source-coverage expansion and gap reporting.
