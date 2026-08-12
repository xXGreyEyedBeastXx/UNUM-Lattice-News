# Lattice Operating Model

## Purpose

UNUM Lattice News organizes public evidence through distinct cooperating structures:

```text
source -> story -> node -> relation -> rendition
             \-> contribution ->/
             \-----> spread <-----/
             -> hashtags ->

confirmed contribution
        |
        v
harm assessment
        |
        v
category-bounded harm hierarchy
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
- harm-rating windows where relevant;
- hashtag neighborhoods;
- current disputes and unknowns;
- sources and correction history.

A node is not a dossier of everything ever associated with the subject.

Large recurring actors may maintain a historical spine that points to independently reusable policy/action and contribution records rather than reproducing every event in full. See `docs/HISTORICAL_ACTOR_AND_CONTRIBUTION_MODEL_v0_1.md`.

Nodes participating in harm hierarchy work should declare a hierarchy class:

```text
institution
leader
non_leader_actor
affected_population
not_scored
```

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
- investigation state;
- harm assessment where relevant;
- counterevidence and unknowns;
- path-forward objects where unresolved;
- debunking record where a claim is affirmatively defeated;
- related stories, relations, and nodes;
- study/spread memberships;
- correction history.

One contribution may appear in many studies. The underlying factual record should not be duplicated merely because several spreads interpret it.

A contribution is not automatic culpability. Historical context is not justification. Benefit is not causation.

## Investigation state

Harm-audit contributions and consequential relations use four workflow states:

```text
PENDING
PATH_FORWARD
CONFIRMED
DEBUNKED
```

These are not substitutes for evidentiary posture.

`DEBUNKED` requires an affirmative explanation of why the scoped claim fails. `SEARCHED_NOT_FOUND` is not enough.

See `docs/HARM_HIERARCHY_LEGIBILITY_ADVERSARIAL_AUDIT_v0_1.md` and `EDITORIAL_STANDARD.md`.

## Harm assessment

A harm assessment is a structured read of a contribution's consequences and power effects.

It preserves a decomposed harm vector rather than hiding the entire judgment inside one scalar score.

Core dimensions include:

```text
lethal / physical harm
confinement / coercion
material deprivation
rights / agency harm
land / sovereignty / displacement
ecological / future-generation harm
democratic / epistemic harm
power concentration
catastrophic risk imposition
```

Propagation dimensions include reach, duration, irreversibility, and target vulnerability.

Only `CONFIRMED` contributions may add to the confirmed harm hierarchy. `PENDING` and `PATH_FORWARD` remain visible but uncounted as confirmed realized harm. `DEBUNKED` claims contribute zero while retaining their explanation.

Beneficial conduct elsewhere does not subtract from a documented harm. The harm hierarchy is not a net-goodness score.

## Harm hierarchy

A harm hierarchy is a dated, time-bounded assembly of confirmed harm contributions for legibility.

Maintain separate ranking surfaces for:

```text
institutions
leaders
non-leader actors
```

The public rating remains a tuple:

```text
[realized harm, structural harm, catastrophic risk]
```

Do not silently convert that tuple into a claim of criminal guilt or moral essence.

Where multiple contributors participate in the same underlying harm, preserve a shared harm identifier and contributor-specific responsibility so the victim count is not multiplied across actors.

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

It may pull together sources, stories, nodes, relations, contribution records, harm assessments, and renditions without becoming their permanent evidence container.

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
- counterevidence that bears on the claim;
- disputed or unsupported claims;
- affected people and ecologies;
- protective options;
- evidence that would change the assessment.

A rendition is revisable. It does not rewrite the underlying sources, stories, nodes, relations, contribution records, or harm assessments.

## Self-population boundary

Automation and agents may:

- ingest public sources;
- extract candidate entities and hashtags;
- suggest existing or new nodes;
- propose relation types;
- propose contribution records;
- identify connected stories;
- surface contradictions, stale claims, and missing evidence;
- produce provisional harm vectors and hierarchy candidates;
- draft bounded renditions.

Automation and agents may not independently:

- publish accusations about identifiable people or organizations;
- convert hashtag co-occurrence into a relation;
- convert study membership into causal contribution;
- convert contribution into culpability;
- promote allegation into fact;
- infer private facts;
- erase claim-relevant counterevidence or uncertainty;
- mark a claim debunked merely because a search failed;
- turn threat assessment into enemy designation;
- turn a harm hierarchy into punishment authorization;
- publish material merely because it supports an existing conclusion.

## Core locks

```text
Node != verdict.
Hashtag != edge.
Association != culpability.
Contribution != culpability.
Benefit != causation.
Beneficial action != offset for unrelated harm.
Capability != intent.
Historical context != justification.
Pending != debunked.
Searched-not-found != debunked.
Threat assessment != enemy designation.
Harm hierarchy != legal guilt.
Rendition != canonical truth.
Correction strengthens the lattice.
```
