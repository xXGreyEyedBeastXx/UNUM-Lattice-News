# Extensible Evidence Grammar v0.1

Status: ACTIVE METHODOLOGY
Date: 2026-08-17

## Root rule

**Grammar may expand and evolve. Evidentiary collapse is the worse failure.**

The lattice vocabulary is an instrument for preserving distinctions discovered in evidence. It is not a closed ontology and it must not force materially different relations, postures, mechanisms, or authority seats into an existing category merely to maintain schema stability.

```text
SCHEMA_COMPATIBILITY < PRESERVING_MATERIAL_DIFFERENCE
```

when the two genuinely conflict.

Compatibility should be preserved where it does not cost meaning. When it does, add a typed extension and record the reason.

## When grammar should expand

Add or refine a type when an existing type would collapse distinctions that change any of the following:

- identity or kinship;
- evidentiary posture;
- authority or responsibility;
- causal mechanism;
- intent or knowledge;
- temporal sequence;
- territorial effect;
- victim/affected-population seat;
- law versus observed conduct;
- stated justification versus operating procedure;
- local practice versus system-wide pattern;
- direct perpetration versus enabling, encouragement, omission, protection, or impunity;
- movement continuity versus legal-organizational identity;
- formal separation versus functional continuity;
- allegation versus independent finding versus adjudication;
- present effect versus projected trajectory.

## Extension pattern

New vocabulary should be typed and reversible rather than silently replacing older records.

```text
existing_type
  -> remains readable
  -> extension adds resolution
  -> old records can be migrated when useful
  -> no evidence is upgraded merely because a new type exists
```

Preferred extension record:

```yaml
grammar_extension:
  term: DELIBERATE_TARGETING_FINDING
  parent_family: EXTERNAL_FINDING
  reason: >-
    distinguish a competent investigative finding of deliberate targeting from
    raw allegation, observed death, ordinary supported inference, or final court judgment
  introduced: 2026-08-17
  migration: optional
```

## Current extensions opened by Israel / Palestine conduct trace

The following are first-class distinctions because collapsing them would lose evidence:

- `STATED_JUSTIFICATION` — the actor's declared reason or legal/moral frame.
- `FORMAL_POLICY` — enacted or formally directed policy.
- `LOCAL_ORDER` — documented order at unit, facility, checkpoint, zone, or commander level.
- `OPERATING_PROCEDURE` — repeated practice established as de facto or formal procedure.
- `OBSERVED_CONDUCT` — directly documented action without automatic intent inference.
- `DOCUMENTED_EFFECT` — death, injury, deprivation, displacement, destruction, territorial control, return obstruction, etc.
- `SYSTEMATIC_PATTERN` — repeated conduct established across sufficient incidents/locations/times.
- `LEADERSHIP_ENCOURAGEMENT` — competent evidence that leadership implicitly encouraged conduct.
- `LEADERSHIP_ORDER` — competent evidence of explicit leadership direction.
- `EXTERNAL_FACT_FINDING` — finding by a competent investigatory body, distinct from a court judgment.
- `LEGAL_ADVISORY_FINDING` — authoritative advisory legal determination, distinct from criminal adjudication.
- `DELIBERATE_TARGETING_FINDING` — competent finding that a protected civilian class/persons were deliberately targeted.
- `COLLECTIVE_PUNISHMENT_FINDING` — competent finding that collective punishment occurred.
- `TERRITORIAL_EFFECT` — persistent change in control, access, settlement, displacement, returnability or boundary practice.
- `ACCOUNTABILITY_EVASION_FUNCTION` — supported inference that a framing or organizational form manages attribution/accountability; not equivalent to proven deceptive intent.
- `DENIAL_OR_COUNTERPOSITION` — actor's direct denial or alternative account, preserved without automatic priority.
- `CROSS_THEATER_ANALOGUE` — similar transformation in a distinct legal/geographic theater; never automatic identity or common command.

## Non-collapse locks

```text
WORDS != ORDERS
ORDERS != ALL CONDUCT
CONDUCT != EFFECT
EFFECT != INTENT
PATTERN != CENTRAL COMMAND
PATTERN != COINCIDENCE merely because command is unproven
DENIAL != DEBUNKING
FACT_FINDING != CRIMINAL_CONVICTION
ADVISORY_OPINION != CRIMINAL_CONVICTION
LOCAL_ORDER != ARMY_WIDE_POLICY
FORMAL_POLICY != COMPLETE DESCRIPTION OF PRACTICE
LEGAL_CATEGORY != MORAL TOTALITY
CROSS_THEATER_ANALOGUE != SAME LEGAL REGIME
```

## Relation to existing grammar

The existing `source -> story -> node -> relation -> contribution -> spread -> rendition` architecture remains useful. These extensions increase the resolution *inside* those objects. They do not crown a replacement ontology.

If future evidence requires more resolution, extend again.

## Re-entry rule

When a later analyst encounters a relation that does not fit:

1. do not choose the nearest existing label by habit;
2. state what difference would be lost;
3. search for an existing equivalent or historical term;
4. if none preserves the distinction, add a typed extension;
5. record its parent family, reason, scope and migration implications;
6. leave older evidence intact unless a deliberate migration improves legibility without changing posture.

**The lattice is allowed to learn new grammar. It is not allowed to gain neatness by losing reality.**
