# Correction-Response Primitive v0.1

## Purpose

Historical lineage is not a biography field. It is a time-aware relational surface.

The lattice needs to preserve not only what an actor, institution, movement, or policy did, but what happened when the record later changed and the subject had a meaningful opportunity to respond.

```text
ORIGINAL CLAIM / ACTION
-> affected participant or ecology
-> contemporaneous warning / contrary evidence
-> later correction / exoneration / adjudication / factual update
-> opportunity to revise
-> actual response
-> repair / persistence / retaliation / policy change
-> later recurrence or reform
```

The canonical schema is `schemas/CORRECTION_RESPONSE_STITCH_v0_1.yaml`.

## Why a stitch rather than an actor-owned ledger

A correction event belongs to a relation among multiple durable addresses:

```text
actor
<-> original claim/action
<-> affected population
<-> evidence or adjudicating institution
<-> correction event
<-> later response
<-> downstream consequence
```

An actor dossier may point to that relation, but does not own it. The same stitch can be visible from a court, institution, affected-population, scientific-evidence, or policy dossier.

## Evidence discipline

A correction record has two separate proof burdens:

1. Was the original claim/action represented accurately?
2. Was the later correction, exoneration, adjudication, or contrary evidence itself strong enough to change the record?

Only after both are established should the response be classified.

## Response states

The schema supports acknowledgment, partial or full update, denial, silence, doubling down, apology, repair, retaliation, disputed correction, and insufficient evidence.

These are event states, not personality diagnoses.

For example:

`DOUBLED_DOWN` means evidence supports a later affirmative repetition or reinforcement after a meaningful opportunity to update. It does not mean the lattice has inferred a permanent psychological trait.

`RETALIATED` requires evidence connecting a later adverse action to the correction/dissent context; mere procedural enforcement or disagreement is not sufficient.

## Pattern formation

One correction-response event does not establish a pattern.

```text
event A
+ event B
+ event C
-> candidate recurring pattern
-> compare mechanisms and contexts
-> preserve counterexamples
-> preserve genuine reform
-> assign confidence
```

Pattern objects must retain evidence that cuts against the pattern.

## Historical Talos / Charlie Seay contribution

Issue #36 was created by `xXGreyEyedBeastXx`. Talos / Charlie Seay later proposed `CORRECTION_RESISTANCE_LEDGER_v0_1.md` in original PR #37.

The exact historical proposal is preserved in recovered draft PR #45 and branch `talos/bounty-36-1786433951172`.

Useful ideas retained:

- historical actor lineage;
- explicit correction attempts;
- response-state recording;
- retaliation as a separately evidenced event;
- source-backed recurrence;
- review status.

Modernized or rejected:

- the primitive is not coupled to feed intake;
- response states now include apology, repair, partial update, dispute, and insufficient evidence;
- private motive is not inferred from failure to update;
- recurrence requires comparable sourced events plus counterexamples;
- the relation is a stitch/bridge object, not solely an actor-owned ledger.

## Validation surfaces

The original issue suggested substantially different cases such as an individual public figure responding to later exonerating evidence and a legislature responding to protest/dissent. Those remain useful population tests, but they are content work rather than prerequisites for the schema to exist.

Any real case must carry its own sources and evidence posture. The schema itself does not preload a conclusion about those cases.

## Nonclaims

`Past act != permanent identity.`

`Correction assertion != established correction.`

`No apology != proof of malicious intent.`

`Sanction != retaliation automatically.`

`Repeated allegation != repeated event.`

`Later reform != erasure of historical harm.`

`Historical harm != proof that later reform is fake.`
