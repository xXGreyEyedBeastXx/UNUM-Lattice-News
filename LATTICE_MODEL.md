# Lattice Operating Model

## Purpose

UNUM Lattice News organizes public evidence through distinct cooperating structures:

```text
source -> story -> node -> relation -> rendition
             \-> contribution ->/
             \-----> spread <-----/
             -> hashtags ->
```

These structures cooperate without becoming interchangeable.

## Source

A source is the recoverable evidence object: an official document, research paper, legal filing, dataset, public statement, investigative report, interview, or other attributable record.

A source record should preserve:

- title;
- author or institution;
- publication date;
- event date when different;
- source type;
- URL or durable identifier;
- access date;
- relevant claims;
- limitations or conflicts;
- rights or license information when known.

A source may support several stories, nodes, relations, and contribution records.

## Story

A story is a dated event or development.

It answers:

> What happened, when, according to which evidence, and what changed?

Stories should remain temporally bounded. They may propose updates to nodes, relations, and contributions, but they do not become the permanent identity of any participant.

## Node

A node is the durable, independently readable home for a person, institution, technology, policy, movement, place, population, ecology, or other recurring subject.

A node should contain only enough context to understand that subject locally:

- identity and node type;
- current bounded summary;
- direct evidence-backed relationships;
- timeline pointers;
- contribution index where relevant;
- hashtag neighborhoods;
- current disputes and unknowns;
- sources and correction history.

A node is not a dossier of everything ever associated with the subject.

Large recurring actors may maintain a historical spine that points to independently reusable policy/action and contribution records rather than reproducing every event in full. See `docs/HISTORICAL_ACTOR_AND_CONTRIBUTION_MODEL_v0_1.md`.

## Contribution

A contribution is a reusable accountability record for a specific actor's participation in a bounded causal field.

It answers:

> What did this actor contribute, through what mechanism, during what period, to which causal field, with what evidence and what limits?

Contribution types may include policy, vote, funding, contract, procurement, deployment, transfer, lobbying, statement, operational action, regulatory action, omission under a defined duty, correction, or other consequential participation.

A contribution should preserve:

- contributor node;
- policy/action/mechanism node when available;
- date or period;
- causal scope;
- immediate mechanism;
- direct and downstream effects;
- affected participants or ecologies;
- evidence posture;
- counterevidence and unknowns;
- related stories, relations, and nodes;
- study/spread memberships;
- correction history.

One contribution may appear in many studies. The underlying factual record should not be duplicated merely because several spreads interpret it.

A contribution is not automatic culpability. Historical context is not justification. Benefit is not causation.

## Hashtag

A hashtag is a traversal handle and discovery neighborhood.

Examples:

```text
#domain/Neurotechnology
#mechanism/Surveillance
#right/MentalPrivacy
#institution/UNESCO
#status/Observed
```

Hashtag co-occurrence does not establish coordination, guilt, causation, ownership, agreement, or identity.

Hashtags provide high recall. Typed relations provide higher-precision claims.

## Relation

A relation is an explicit, typed, evidence-backed edge between nodes or between a node and a proposition, event, capability, population, ecology, or contribution.

Examples:

```text
A --[ADOPTED]----------> policy
A --[DEVELOPS]---------> technology
A --[USES]-------------> system
A --[WARNS_ABOUT]------> risk
A --[AFFECTS]----------> population
A --[CONTRACTS_WITH]---> institution
```

Every consequential edge should preserve its evidence and scope.

Co-occurrence is not an edge.

## Spread

A spread is a reader-facing discovery/review surface assembled from underlying records for a bounded question, event complex, or time window.

It may pull together sources, stories, nodes, relations, contribution records, and renditions without becoming their permanent evidence container.

The same contribution may therefore participate in multiple spreads without duplication.

## Rendition

A rendition is a dated synthesis generated from a selected set of nodes, stories, hashtags, relations, contributions, and sources.

It answers:

> Given this bounded evidence surface, what does the current state appear to be?

A rendition should separate:

- established facts;
- public statements and ambitions;
- supported inferences;
- possible or likely trajectories;
- documented harms;
- counterevidence;
- disputed or unsupported claims;
- affected people and ecologies;
- protective options;
- evidence that would change the assessment.

A rendition is revisable. It does not rewrite the underlying sources, stories, nodes, relations, or contribution records.

## Self-population boundary

Automation and agents may:

- ingest public sources;
- extract candidate entities and hashtags;
- suggest existing or new nodes;
- propose relation types;
- propose contribution records;
- identify connected stories;
- surface contradictions, stale claims, and missing evidence;
- draft bounded renditions.

Automation and agents may not independently:

- publish accusations about identifiable people or organizations;
- convert hashtag co-occurrence into a relation;
- convert study membership into causal contribution;
- convert contribution into culpability;
- promote allegation into fact;
- infer private facts;
- erase counterevidence or uncertainty;
- turn threat assessment into enemy designation;
- publish material merely because it supports an existing conclusion.

## Core locks

```text
Node != verdict.
Hashtag != edge.
Association != culpability.
Contribution != culpability.
Benefit != causation.
Capability != intent.
Historical context != justification.
Threat assessment != enemy designation.
Rendition != canonical truth.
Correction strengthens the lattice.
```
