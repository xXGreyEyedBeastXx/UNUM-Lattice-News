# UNUM Lattice News — Operating Model

**Status:** compatibility overview  
**Updated:** 2026-08-21  
**Current operational authority:** `docs/NEWS_OPERATIONS_v0_2.md`, `LATTICE_MODEL.md`, `docs/HARM_MESH_OPERATING_MODEL_v0_1.md`, and the active schema/registry surfaces.

This document remains a compact human-readable overview. Where it conflicts with the current operations layer, lattice model, node-type registry, evidence-jurisdiction rules, harm model, or record templates, the newer specialized surface controls. Older `entity_type`, flat node lists, `counterevidence`, and three-axis harm references should be read as schema-history rather than as instructions to undo later work.

## Purpose

UNUM Lattice News is intended to become a self-resurfacing public evidence lattice rather than a conventional chronological news feed.

The basic cycle is:

```text
source -> story -> node updates -> evidenced relations -> hashtag neighborhoods -> bounded rendition
                                      ^                         |
                                      +---- correction/review --+
```

The system should make consequential relationships easier to inspect without forcing a reader through every connected subject at once.

## Core public objects

### Story

A **story** is a dated evidence surface describing an event, publication, decision, deployment, statement, discovery, or consequential change.

Stories should preserve sources and propose updates to durable nodes. A story is not the only place where information about a subject lives.

### Node

A **node** is the bounded durable home for one recurring subject. New records use the canonical `family` / `subtype` registry in `schemas/NODE_TYPE_REGISTRY_v0_1.yaml`; older `entity_type` or `node_type` fields remain migration-compatible.

A node should remain locally understandable. It may contain:

- identity and canonical type;
- current evidence-bounded summary;
- timeline;
- direct evidenced relations;
- active hashtags;
- relevant stories and contributions;
- authority, vulnerability, or accountability state where relevant;
- unresolved questions;
- evidence effects;
- corrections;
- references.

Nodes should not drag readers through the entire lattice. They expose doors outward.

### Hashtag

A **hashtag** is a discovery route across independently readable nodes and stories.

Hashtags identify shared neighborhoods, domains, mechanisms, material flows, constraints, accountability questions, rights, harms, technologies, institutions, movements, or other useful cross-cuts. Co-occurrence under a hashtag does **not** establish coordination, agreement, guilt, causation, knowledge, intent, or conspiracy.

Human-facing tags may remain simple. The typed registry distinguishes entity, domain, mechanism, flow, constraint, accountability, right, harm, governance, status, and source neighborhoods.

### Relation / Edge

A **relation** is an evidenced, typed connection between two nodes or between a node and a proposition/event/resource/consequence.

Examples include:

- `OWNS`
- `FUNDS`
- `CONTRACTS_WITH`
- `EMPLOYS`
- `APPOINTED_BY`
- `REGULATES`
- `PARTNERS_WITH`
- `DEPENDS_ON`
- `SUPPLIES`
- `OPPOSES`
- `SUPPORTS`
- `CLAIMS`
- `AFFECTS`
- `EXTERNALIZES_COST_TO`

Every consequential edge should be recoverable to evidence. Two nodes appearing in the same story or hashtag neighborhood is not enough to create an edge.

### Contribution

A **contribution** is a bounded accountability record for an actor's participation in a causal field. It preserves mechanism, evidence, investigation state, responsibility grade, harm assessment, and—where material—intentional term-setting, knowledge/notice, correction capacity, persistence, or repair.

Contribution is not automatic culpability.

### Spread

A **spread** is a bounded investigation/review surface that assembles reusable records without becoming their permanent evidence container.

### Rendition

A **rendition** is a dated, bounded synthesis across selected nodes, stories, relations, contributions, sources, and hashtags.

It asks:

> Given the evidence available through this bounded surface at this time, what does the current state appear to be?

A rendition may include:

- established observations;
- publicly stated positions or ambitions;
- supported inferences;
- documented harms;
- claim-specific evidence effects and competing models;
- accountability findings where supported;
- disputed and unsupported claims;
- trajectories;
- affected people and ecologies;
- proposed protective responses;
- unresolved questions;
- evidence that would change the assessment.

A new rendition may supersede an earlier assessment without erasing the earlier evidence state.

## Self-population boundary

Automation and agents may assist with:

```text
ingest source
-> extract candidate entities
-> suggest hashtags
-> identify existing nodes
-> suggest candidate relations
-> find connected stories
-> surface contradictions and evidence effects
-> update timelines
-> identify missing evidence
-> propose contribution/accountability records
-> draft bounded renditions
```

But the following locks remain:

```text
suggested relation != established relation
generated synthesis != published finding
association != culpability
threat != enemy
capability != intent
capacity_to_know != actual_knowledge
intentional_term_setting != harmful_endpoint_intent
```

Consequential public claims about identifiable people or organizations require evidence review before publication until a later governance process explicitly establishes a narrower safe authority.

## Honest-rendition objective

The system is not optimized to make a conclusion impossible to deny. It is optimized to make the evidence and reasoning inspectable enough that disagreement must engage what is actually present.

It should be capable of discovering evidence that weakens its own prior assessment.

A challenge supported by better evidence is a repair input, not an attack on the lattice.

## Ideological non-capture

The same mechanisms should be traceable regardless of claimed ideology, party, institution, nationality, religion, corporation, movement, or project.

Examples of mechanisms worth tracing include:

- dehumanization;
- authoritarian concentration;
- purity policing;
- collective punishment;
- political violence;
- suppression of dissent;
- racial, ethnic, religious, or other supremacy;
- economic domination;
- forced assimilation;
- ecological externalization;
- information manipulation;
- surveillance and classification;
- institutional capture;
- intentional material term-setting with externalized harm;
- grievance routing and downward scapegoating.

No ideological label automatically establishes safety or danger. The evidence, mechanism, consequence, trajectory, and accountability path must do the work.

## Protection target

The lattice exists to improve the visibility of conditions affecting:

- human dignity;
- bodily, mental, cognitive, and relational self-sovereignty;
- meaningful consent, refusal, exit, and appeal;
- material security and access to life-sustaining necessities;
- democratic and institutional accountability;
- plural human and nonhuman life;
- ecological continuity and life-support systems;
- information and reality integrity;
- recoverable futures.

## Tiny lock

> Do not tell the reader whom to hate. Show what connects, what happened, what the evidence supports, what remains uncertain, who bears the consequences, who gains or is insulated, what the powerful actor could know or correct, and where the trajectory appears to lead.
