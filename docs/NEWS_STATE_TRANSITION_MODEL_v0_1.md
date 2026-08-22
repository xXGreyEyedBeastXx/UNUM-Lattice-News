# UNUM-Lattice-News — News State Transition Model v0.1

**Status:** active working model  
**Introduced:** 2026-08-22  
**Purpose:** preserve the intermediate state-change layer between a dated story and the durable node/relation/contribution surfaces it may update.

## 1. Why this layer exists

A story answers:

> What happened, when, according to which evidence, and what changed?

That is necessary but not always sufficient. A free-form `what_changed` summary can collapse distinctions that matter to later investigation:

- the event happened at one time but became publicly known later;
- a policy was announced, then implemented only partially;
- an attempted change was blocked while the underlying objective persisted;
- two opposing pressures produced little net movement even though both were large;
- a legal or organizational label changed while the causal body continued;
- a headline repeated an older event without creating a new material state;
- a correction changed the evidentiary read without changing the historical event;
- several observations described different seats of one evolving public state.

The state-transition layer therefore preserves:

```text
bounded prior state
-> evidenced operation / event / pressure
-> bounded later state
```

without treating either state as complete reality.

## 2. News state is a seated read

A news state is an evidence-bounded read of a public configuration at an explicit seat.

Minimum seat:

```text
as_of
scope
jurisdiction
participants / ecologies
active relations
active constraints
material conditions
known claims
known unknowns
source-access conditions
```

A state is not a timeless verdict. It is revisable when later evidence improves the read.

```text
state snapshot != permanent identity
state snapshot != complete world
state change != moral verdict
```

## 3. Keep the clocks separate

Do not force one timestamp to do every job.

Use distinct clocks where material:

```text
event_time
  when the underlying occurrence or operation happened

publication_time
  when a source or announcement became public

observation_time
  when the relevant condition was measured or directly observed

access_time
  when the investigator recovered the source

state_as_of
  the bounded time-seat represented by the state snapshot

correction_time
  when the public/evidentiary record was corrected or materially revised
```

These times may coincide, but they should not be assumed identical.

Examples:

```text
late publication != late event
new article != new event
new evidence != changed historical occurrence
changed state != newly discovered state
correction of claim != erasure of prior publication
```

## 4. Transition grammar

Represent a transition as:

```text
S0 --[T]--> S1
```

where:

- `S0` = best recoverable bounded prior state;
- `T` = event, operation, pressure, decision, observation, correction, or other evidenced transformation;
- `S1` = best recoverable bounded later state.

For every material transition preserve three classes:

### Changed
What became different?

Examples:

- officeholder;
- legal status;
- policy text;
- enforcement practice;
- funding level;
- ownership/control;
- access condition;
- territorial control;
- exposure to harm;
- available refusal/exit/appeal;
- information available to decision-makers;
- public claim posture;
- institutional correction capacity.

### Continued
What remained materially continuous despite the event or renaming?

Examples:

- same beneficial owner;
- same personnel pipeline;
- same constraint on affected people;
- same operational practice;
- same funding route;
- same unresolved allegation;
- same warning ignored across successive decisions.

### Unresolved
What could not yet be determined?

Preserve typed missingness rather than narrating the gap away.

## 5. Delta types

A transition may contain several simultaneous deltas.

Preferred families:

```text
IDENTITY_DELTA
RELATION_DELTA
CONSTRAINT_DELTA
AUTHORITY_DELTA
MATERIAL_FLOW_DELTA
POLICY_DELTA
PRACTICE_DELTA
INFORMATION_DELTA
KNOWLEDGE_NOTICE_DELTA
HARM_EXPOSURE_DELTA
REALIZED_OUTCOME_DELTA
RESISTANCE_DELTA
ACCOUNTABILITY_DELTA
CORRECTION_DELTA
PROJECTION_DELTA
NO_MATERIAL_DELTA_SUPPORTED
UNKNOWN_DELTA
```

A delta should point to evidence effects that actually bear on it.

Do not infer a material delta merely because rhetoric, branding, legal form, or headline wording changed.

## 6. Opposing pressures and balance

A small net change can conceal large opposing transformations.

```text
pressure_A = +10
pressure_B = -10
net = 0
```

`net = 0` does not mean `nothing happened`.

Where the evidence supports it, preserve:

- direction of each pressure;
- actor or mechanism producing it;
- magnitude or qualitative strength if recoverable;
- resistance or counterforce;
- which population/ecology bears the interaction;
- which relation survived after balance.

This is especially important for blocked policy attempts, contested enforcement, strikes, litigation, regulatory resistance, budget fights, and ecological systems with delayed effects.

## 7. Re-announcement and novelty test

Before treating an item as a new state change, ask:

1. Is there a new underlying event?
2. Is there a new implementation step?
3. Is there a newly observed consequence?
4. Is there new evidence about an old event?
5. Is this only a restatement, anniversary, repost, or rhetorical reframing?
6. Did the relation, constraint, authority, material flow, outcome, or evidence posture actually change?

If the answer supports no material change, record `NO_MATERIAL_DELTA_SUPPORTED` while preserving the publication as a source or projection event where relevant.

## 8. Projection versus state

Public framing belongs in the record, but it is not the state by default.

Keep separate:

```text
what an actor says changed
what a source reports changed
what the evidence establishes changed
what remains disputed
what the underlying material configuration appears to be
```

A narrative shift may itself be an evidenced `PROJECTION_DELTA` even when no policy/material state changed.

## 9. Identity continuity through transformations

A transition should not create false discontinuity merely because an address changed.

Test:

```text
rename
reorganization
merger / spinoff
office transition
subsidiary transfer
contractor substitution
jurisdiction shift
accounting reclassification
program relabeling
```

against the mesh rules:

```text
name change != identity change
legal separation != causal separation
accounting separation != material separation
```

If continuity is supported, preserve both the changed address and the surviving relation.

## 10. Evidence jurisdiction inside a transition

Every evidence item updates only the delta, claim, edge, or variable it actually bears on.

Example:

```text
court blocks policy
-> REALIZED_OUTCOME / CONSTRAINT_RESISTANCE update
!= automatic CLAIM_DEFEATING evidence against the attempted policy or stated direction
```

Likewise:

```text
new denial
-> STATED / PROJECTION update
!= automatic material-state reversal

new damaging report
-> may update evidence confidence
!= proof the underlying event occurred on publication day
```

## 11. Transition chain and trajectory

State transitions may be chained without pretending the chain has one simple direction.

```text
S0 -> S1 -> S2 -> S3
```

Each hop should remain independently recoverable.

Trajectory analysis may then ask:

- which deltas repeat;
- which pressures persist after resistance;
- whether a mechanism reroutes after blockage;
- whether correction capacity strengthens or decays;
- whether the same affected population repeatedly bears cost;
- whether a claimed reversal actually restored the prior condition;
- which relations survive changes of office, branding, jurisdiction, or public narrative.

Trajectory is an inference over preserved transitions. It must not erase the individual transitions that make it testable.

## 12. Correction and epistemic transitions

Some transitions change the evidence state rather than the historical world-state.

Keep both:

```text
world_state_transition
  what materially happened

evidence_state_transition
  what the recoverable record now supports
```

A correction can therefore change claim posture, confidence, attribution, or scope without rewriting the underlying event chronology.

## 13. Relation to lattice objects

```text
source
  -> supports story and transition evidence

story
  -> dated event/development surface

state transition
  -> typed before/after change surface

node
  -> durable recurring subject seat

relation / contribution
  -> reusable causal/accountability structure

spread / rendition
  -> reader-facing bounded projection of current recoverable state
```

A transition may propose node, relation, or contribution updates. It does not automatically promote them.

## 14. Minimum transition packet

```yaml
state_transition:
  id: ""
  scope: ""
  prior_state_ref: null
  later_state_ref: null
  state_as_of_before: null
  state_as_of_after: null
  clocks:
    event_time: null
    publication_time: null
    observation_time: null
    access_time: null
    correction_time: null
  operation_or_event: ""
  changed: []
  continued: []
  unresolved: []
  deltas: []
  opposing_pressures: []
  evidence_effects: []
  affected_participants_or_ecologies: []
  source_lineage: []
  corrections: []
  evidence_that_would_change_assessment: []
  re_entry: []
```

Use `schemas/NEWS_STATE_TRANSITION_v0_1.yaml` for the active structured surface.

## 15. Re-entry test

A future reviewer should be able to answer:

- What was the prior supported state?
- What event/operation/pressure is claimed to have changed it?
- Which clock is being used for each date?
- What changed materially?
- What merely changed in presentation or evidence availability?
- What remained continuous?
- Were opposing pressures hidden by a net result?
- Which evidence bears on each delta?
- What is still unresolved?
- What later observation would defeat, narrow, reroute, or reverse this transition read?

If those cannot be recovered, the intermediate state has been over-compressed.

## Tiny lock

> A headline is not a state change. A new source is not necessarily a new event. Preserve the before, the crossing, the after, the clocks, the surviving relation, and the weak edge.