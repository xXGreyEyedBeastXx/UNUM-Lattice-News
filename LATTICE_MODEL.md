# Lattice Operating Model

Updated: 2026-08-22

## Purpose

UNUM Lattice News organizes public evidence through distinct cooperating structures:

```text
source -> story -> state transition -> node -> relation -> rendition
             \-> contribution -----------/
             \----------> spread <-------/
             -> hashtags ->

confirmed contribution
        |
        v
harm / accountability assessment
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

A source may support several stories, state transitions, nodes, relations, and contribution records.

## Story

A story is a dated event or development.

It answers:

> What happened, when, according to which evidence, and what changed?

Stories should remain temporally bounded. They may propose updates to state transitions, nodes, relations, and contributions, but they do not become the permanent identity of any participant.

## State transition

A state transition is the typed intermediate crossing between a dated event/development and the durable records it may update.

It answers:

> Given the best recoverable prior state, what operation, event, pressure, observation, or correction occurred; what changed afterward; what remained continuous; and which clock belongs to each date?

Use a transition when a free-form `what_changed` summary would collapse materially important distinctions such as:

- event time versus publication or observation time;
- newly discovered evidence versus a newly occurring event;
- attempted change versus realized result;
- resistance that blocks or narrows an attempt;
- opposing pressures hidden by a small net change;
- projection/rhetoric change versus material-state change;
- legal, organizational, accounting, jurisdictional, or naming change with surviving causal continuity;
- correction of the evidence state versus rewrite of the historical event.

A transition should preserve:

```text
prior bounded state
-> evidenced crossing
-> later bounded state
```

and distinguish:

```text
changed
continued
unresolved
```

Keep separate clocks where material:

```text
event time
publication time
observation time
access time
state-as-of time
correction time
```

A transition may propose node, relation, contribution, or claim updates. It does not automatically promote them.

See:

- `docs/NEWS_STATE_TRANSITION_MODEL_v0_1.md`;
- `schemas/NEWS_STATE_TRANSITION_v0_1.yaml`;
- `templates/STATE_TRANSITION.yaml`.

## Node

A node is the durable, independently readable home for a recurring subject.

New nodes use the canonical `family` / `subtype` classification in `schemas/NODE_TYPE_REGISTRY_v0_1.yaml`. Existing nodes using legacy `node_type` or `entity_type` fields remain valid migration surfaces and do not require cosmetic rewrites merely to erase schema history.

Canonical families include actors, networks, systems, instruments, events/actions, places/jurisdictions, populations/communities, ecologies/living systems, conditions/lived states, resource flows, claims/propositions, ideologies/cultural frames, consequences, responses/repairs, and analysis frameworks.

A node should contain only enough context to understand that subject locally:

- identity and canonical family/subtype;
- current bounded summary;
- direct evidence-backed relationships;
- timeline story and state-transition pointers;
- contribution index where relevant;
- harm-rating windows where relevant;
- authority, vulnerability, or accountability state where relevant;
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

Node family does not determine relation role. An institution may be a funder, employer, regulator, gatekeeper, beneficiary, loss-bearer, term-setter, repair actor, or another role only where the relevant relation is evidenced.

## Contribution

A contribution is a reusable accountability record for a specific actor's participation in a bounded causal field.

It answers:

> What did this actor contribute, through what mechanism, during what period, to which causal field, with what evidence and what limits?

Contribution types may include policy, vote, funding, contract, procurement, deployment, transfer, lobbying, statement, operational action, regulatory action, intentional term-setting, omission under a defined duty, correction, or other consequential participation.

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
- responsibility grade;
- intentional action/term-setting where material and evidenced;
- intended gain, cost reduction, or capacity increase where material and evidenced;
- harmful-endpoint intent where material and evidenced;
- knowledge, capacity to know, foreseeability, and credible notice where accountability turns on them;
- capacity to correct and response after notice;
- gain or insulation retained after notice where relevant;
- harm assessment where relevant;
- evidence effects, unknowns, and limitations;
- path-forward objects where unresolved;
- debunking record where a claim is affirmatively defeated;
- related stories, state transitions, relations, and nodes;
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

## Accountability state

Where knowledge, intent, or persistence materially affects responsibility, keep the following separations visible:

```text
intentional action / term-setting
intended gain / cost reduction / capacity increase
harmful-endpoint intent
knowledge state
capacity to know
foreseeability
credible notice
capacity to correct
response after notice
gain or insulation retained after notice
repair or mitigation
```

The lattice does not require proof that an actor desired every downstream harm before recognizing a deliberately chosen term or mechanism as intentional.

Likewise:

```text
capacity to know != actual knowledge
foreseeability != desire
should have known != automatic legal negligence finding
deliberate avoidance requires evidence
absence of harmful-endpoint intent != absence of accountability
```

See `docs/HARMFUL_INTENT_AND_TRAJECTORY_MODEL_v0_1.md` and `nodes/harm-domination-protection-weighting.yaml`.

## Harm assessment

A harm assessment is a structured read of a contribution's consequences, power effects, and—where separately established—harmful intent or trajectory.

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

The public rating is a four-axis tuple:

```text
[realized harm, structural harm, catastrophic risk, harmful intent / trajectory]
```

The first three axes describe realized/structural harm and risk. The fourth preserves evidenced harmful intent, attempted harmful policy, preparation, or trajectory so blocked attempts do not vanish and rhetoric is not falsely counted as realized injury.

Do not silently convert that tuple into a claim of criminal guilt or moral essence.

Where multiple contributors participate in the same underlying harm, preserve a shared harm identifier and contributor-specific responsibility so the victim count is not multiplied across actors.

## Hashtag

A hashtag is a traversal handle and discovery neighborhood.

Examples:

```text
#domain/Neurotechnology
#mechanism/Surveillance
#flow/UpwardRecirculation
#constraint/LackOfMeaningfulExit
#accountability/CredibleNotice
#right/MentalPrivacy
#institution/UNESCO
#status/Observed
```

Hashtag co-occurrence does not establish coordination, guilt, causation, ownership, agreement, knowledge, intent, or identity.

Hashtags provide high recall. Typed relations, claims, contributions, state transitions, and accountability records provide higher-precision findings.

Where a tag begins carrying case-specific evidentiary meaning, promote the underlying claim or relation instead of making the hashtag do evidentiary work.

## Relation

A relation is an explicit, typed, evidence-backed edge between nodes or between a node and a proposition, event, capability, population, ecology, resource, consequence, or contribution.

Examples:

```text
A --[ADOPTED]----------> policy
A --[DEVELOPS]---------> technology
A --[USES]-------------> system
A --[WARNS_ABOUT]------> risk
A --[AFFECTS]----------> population
A --[CONTRACTS_WITH]---> institution
A --[EXTERNALIZES_COST_TO]--> population
```

Every consequential edge should preserve its evidence and scope.

Co-occurrence is not an edge.

## Spread

A spread is a reader-facing discovery/review surface assembled from underlying records for a bounded question, event complex, or time window.

It may pull together sources, stories, state transitions, nodes, relations, contribution records, harm assessments, accountability states, and renditions without becoming their permanent evidence container.

The same contribution or transition may therefore participate in multiple spreads without duplication.

## Rendition

A rendition is a dated synthesis generated from a selected set of nodes, stories, state transitions, hashtags, relations, contributions, and sources.

It answers:

> Given this bounded evidence surface, what does the current state appear to be?

A rendition should separate:

- established facts;
- public statements and ambitions;
- supported inferences;
- possible or likely trajectories;
- documented harms;
- accountability findings about intent, knowledge, notice, persistence, or repair where actually supported;
- evidence that bears on the exact claim under review;
- disputed or unsupported claims;
- affected people and ecologies;
- protective options;
- evidence that would change the assessment.

A rendition is revisable. It does not rewrite the underlying sources, stories, state transitions, nodes, relations, contribution records, or harm assessments.

## Self-population boundary

Automation and agents may:

- ingest public sources;
- extract candidate entities and hashtags;
- suggest existing or new nodes;
- propose relation types;
- propose state transitions;
- propose contribution records;
- identify connected stories;
- surface contradictions, stale claims, and missing evidence;
- produce provisional harm vectors, accountability-state candidates, and hierarchy candidates;
- draft bounded renditions.

Automation and agents may not independently:

- publish accusations about identifiable people or organizations;
- convert hashtag co-occurrence into a relation;
- convert a new publication into a new material event without evidence;
- convert a projection delta into a material-state delta without evidence;
- convert study membership into causal contribution;
- convert contribution into culpability;
- convert capacity to know into actual knowledge;
- convert continued harm into a secret motive without evidence;
- promote allegation into fact;
- infer private facts;
- erase claim-relevant evidence or uncertainty;
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
Intentional term-setting != intent to cause every downstream harm.
Capacity to know != actual knowledge.
Foreseeability != desire.
Historical context != justification.
Pending != debunked.
Searched-not-found != debunked.
Threat assessment != enemy designation.
Harm hierarchy != legal guilt.
Rendition != canonical truth.
New article != new event by default.
New source != new world-state by default.
Net zero != no opposing pressure.
Projection delta != material delta by default.
Correction strengthens the lattice.
```
