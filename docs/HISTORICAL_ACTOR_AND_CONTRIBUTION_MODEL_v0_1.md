# Historical Actor and Contribution Model v0.1

## Purpose

UNUM-Lattice-News needs to preserve both long historical continuity and small, reusable causal units.

A single study document is too large to serve as the permanent home for every policy, action, funding decision, deployment, vote, contract, statement, omission, or downstream consequence. The same historical act may matter to several studies at once.

A single actor page is also too large if it becomes a dossier containing every event in full.

This model therefore separates four persistence layers:

```text
actor historical spine
        |
        v
policy / action / program node
        |
        v
contribution record
        |
        +--------------------+
        |                    |
        v                    v
study / spread A        study / spread B
```

The same contribution record may appear in many spreads without being copied or rewritten.

## Core distinction

```text
actor identity/history
!= policy or action identity
!= contribution to a bounded causal field
!= study interpretation
```

A contribution record is not a verdict and does not itself establish moral or legal culpability.

## 1. Historical actor spine

Large recurring actors should have a durable historical node or local index.

Examples include:

- sovereign states;
- national governments and administrations;
- military and intelligence institutions;
- major corporations;
- large advocacy or lobbying organizations;
- major political movements;
- major public officials whose authority spans many studies.

The historical spine should preserve:

```text
identity and aliases
authority / jurisdiction / organizational form
major eras or administrations
long-running strategies and declared missions
major institutional relationships
funding / ownership / procurement lanes
policy families
major disputes and corrections
historical contribution index
```

The actor history page should normally summarize and point outward rather than reproduce every contribution in full.

Recommended local shape:

```text
actor
├── identity
├── authority and jurisdiction
├── historical timeline
├── policy families
├── money / procurement / funding lanes
├── institutional relationships
├── contribution index
├── disputes / counterevidence
└── sources / corrections
```

## 2. Policy, action, program, and event nodes

A policy, program, operation, funding mechanism, law, contract family, military deployment, sanctions regime, arms-transfer program, or other recurring mechanism may become its own node when it has independent identity and appears in multiple contexts.

Examples:

```text
foreign military financing
military basing policy
sanctions regime
arms-transfer program
specific statute
specific executive policy
defense procurement program
settlement policy
surveillance program
```

The policy/action node answers:

> What is this mechanism, when did it exist, who had authority over it, how did it work, and what populations or systems did it affect?

It does not answer every question about every actor's responsibility for it.

## 3. Contribution record

A contribution record is the smallest reusable accountability surface for a consequential participation.

It answers:

> What did this actor contribute, through what mechanism, during what period, to which bounded causal field, with what evidence and what limits?

A contribution may describe harmful, protective, mixed, neutral, enabling, constraining, preventive, corrective, or uncertain participation.

Suggested fields:

```yaml
contribution_record:
  id: contribution_slug
  title: ""
  contributor_node: node_id
  mechanism_node: null
  contribution_type: policy | vote | funding | contract | procurement | deployment | transfer | lobbying | statement | operational_action | regulatory_action | omission_under_duty | correction | other
  start_date: null
  end_date: null
  scope: ""
  causal_fields: []
  studies_or_spreads: []
  immediate_mechanism: ""
  direct_effects: []
  downstream_effects: []
  affected_participants_or_ecologies: []
  responsibility_grade: null
  claim_posture: observed | stated | adjudicated | supported_inference | alleged | disputed | ambiguous | unknown
  evidence: []
  counterevidence: []
  unknowns: []
  related_relations: []
  related_stories: []
  related_nodes: []
  corrections: []
  last_reviewed: "YYYY-MM-DD"
```

### Responsibility grade

Where useful, a contribution may preserve a graded responsibility field rather than a binary guilty/not-guilty label.

A compatible working scale is:

```text
R0 adjacency
R1 rhetorical support
R2 vote / endorsement / formal support
R3 sponsorship / funding / material facilitation
R4 leadership / decisive enabling / command responsibility
R5 direct operational control
```

This grade must remain scoped to the named contribution. It must not automatically become a total judgment of the actor.

## 4. Study / spread

A study or spread is an assembly surface, not the permanent home of all underlying evidence.

A spread may pull together:

```text
sources
stories
actor nodes
policy/action nodes
relations
contribution records
other spreads
renditions
```

The study answers a bounded question. The underlying contribution records remain reusable elsewhere.

Example:

```text
U.S. military aid policy contribution
        |
        +--> Israel / Palestine study
        +--> military-industrial-complex study
        +--> 9/11 past-cone study
        +--> congressional influence study
        +--> arms-manufacturer study
```

No copy should become the canonical truth merely because it appears in a later study.

## 5. Cross-study rule

When an item crosses studies, do not duplicate the factual body if the same contribution record can be referenced.

Use:

```text
one contribution record
-> many study memberships
-> study-specific interpretation stays in each spread/rendition
```

If two studies require different causal claims about the same underlying act, keep the shared observed contribution stable and place the differing interpretations in separate typed relations or renditions.

## 6. Historical contribution index

Large actor nodes should expose an index rather than a flat unsorted list.

Recommended grouping:

```text
by era / administration
by policy family
by geography
by affected population
by mechanism
by responsibility grade
by study membership
by claim posture
```

This allows a reader to move from a broad historical actor to the individual action without turning the actor page into a monolith.

## 7. Causal-cone compatibility

Contribution records are especially useful for event-complex studies that require both a past cone and a consequence cone.

```text
past contributions
-> event
-> consequence contributions
```

The same actor may appear on both sides through different contribution records.

Do not infer that an actor which benefits from a consequence caused the triggering event without separate evidence.

## 8. Cross-institution chains

Some contributions only become legible as chains:

```text
legislature
-> appropriation
-> executive administration
-> agency
-> contractor
-> recipient institution
-> operational use
-> affected population
```

Preserve each independently evidenced step. Do not collapse the chain into one unlabeled edge.

Contribution pages may therefore reference several relation records and several nodes while still having one primary contributor.

## 9. Directory guidance

This model does not require one rigid filesystem, but a workable structure is:

```text
nodes/
  actors/
  institutions/
  policies/
  programs/
  events/

contributions/
  <actor-or-institution>/
    <date-or-policy-slug>.md

spreads/
  <bounded-study>.yaml
```

Existing node locations do not need to be moved immediately. New structure should be adopted incrementally and linked rather than reorganizing the repository destructively.

## 10. Evidence and accusation locks

```text
Contribution != culpability.
Benefit != causation.
Funding != command.
Policy support != responsibility for every downstream act.
Historical context != justification.
Causal contribution != legal justification.
Causal contribution != individual targetability.
Study membership != proof of coordination.
One contribution record may support several competing interpretations.
```

Every consequential contribution must preserve claim posture, evidence, counterevidence, unknowns, scope, and correction path.

## 11. Why this model exists

The lattice should be able to answer both:

> What is the historical record of this major actor?

and:

> What exactly did this actor contribute to this particular outcome?

without forcing either answer to destroy the other.

The historical spine preserves continuity.
The contribution record preserves causal precision.
The spread preserves bounded inquiry.
The relation graph preserves crossings between them.
