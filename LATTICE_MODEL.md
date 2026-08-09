# Lattice Operating Model

## Purpose

UNUM Lattice News organizes public evidence through five distinct structures:

```text
source → story → node → relation → rendition
             ↘ hashtags ↗
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

A source may support several stories, nodes, and relations.

## Story

A story is a dated event or development.

It answers:

> What happened, when, according to which evidence, and what changed?

Stories should remain temporally bounded. They may propose updates to nodes and relations, but they do not become the permanent identity of any participant.

## Node

A node is the durable, independently readable home for a person, institution, technology, policy, movement, place, population, ecology, or other recurring subject.

A node should contain only enough context to understand that subject locally:

- identity and node type;
- current bounded summary;
- direct evidence-backed relationships;
- timeline pointers;
- hashtag neighborhoods;
- current disputes and unknowns;
- sources and correction history.

A node is not a dossier of everything ever associated with the subject.

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

A relation is an explicit, typed, evidence-backed edge between nodes or between a node and a proposition, event, capability, population, or ecology.

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

## Rendition

A rendition is a dated synthesis generated from a selected set of nodes, stories, hashtags, relations, and sources.

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

A rendition is revisable. It does not rewrite the underlying sources or stories.

## Self-population boundary

Automation and agents may:

- ingest public sources;
- extract candidate entities and hashtags;
- suggest existing or new nodes;
- propose relation types;
- identify connected stories;
- surface contradictions, stale claims, and missing evidence;
- draft bounded renditions.

Automation and agents may not independently:

- publish accusations about identifiable people or organizations;
- convert hashtag co-occurrence into a relation;
- promote allegation into fact;
- infer private facts;
- erase counterevidence or uncertainty;
- turn threat assessment into enemy designation;
- publish material merely because it supports an existing conclusion.

## Core locks

```text
Node ≠ verdict.
Hashtag ≠ edge.
Association ≠ culpability.
Capability ≠ intent.
Threat assessment ≠ enemy designation.
Rendition ≠ canonical truth.
Correction strengthens the lattice.
```
