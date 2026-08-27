# Lattice-only light gathering — 2026-08-27 late pass

**Status:** INTAKE-RETURN NOTE / NO AUTOMATIC PROMOTION  
**Scope:** `UNUM-Lattice-News` family only  
**Source custody:** `UNUM-Lattice-News-Intake`

This small pass intentionally tested whether the growing source-first archive can distinguish:

```text
new world event
!= new article
!= correction to existing article
!= new litigation over existing mechanism
!= preparedness / watch signal
```

## 1. Federal grant-conditioning attempt meets appellate constraint

Reuters reported that a divided Ninth Circuit panel largely upheld an injunction blocking challenged HUD and Transportation grant conditions tying federal funding to recipient positions or practices involving immigration, transgender policy, abortion, and related issues.

Current Lattice posture:

```yaml
attempted_funding_leverage: SUPPORTED
appellate_constraint: SUPPORTED
current_enforceability_of_challenged_conditions: LIMITED_BY_INJUNCTION
private_motive: NOT_ESTABLISHED_BY_RULING_ALONE
```

Evidence functions:

```text
CONSTRAINT_RESISTANCE
REALIZED_OUTCOME
SCOPE_LIMITING
```

Important: the court's intervention is not exculpatory evidence that the attempted conditions did not exist.

Intake path:
`candidates/LIGHT_GATHERING_UPDATE_2026-08-27_LATE.yaml`

## 2. Asia-Pacific H5N1 becomes a preparedness/watch surface

WHO's August 27 regional update describes increasing HPAI A(H5N1) animal outbreaks and recent incursions in Australia and New Zealand, with regional health and laboratory networks emphasizing One Health surveillance and zoonotic preparedness.

Current Lattice posture:

```yaml
regional_animal_health_and_zoonotic_watch_signal: SUPPORTED
regional_preparedness_capacity_expansion: SUPPORTED
sustained_human_to_human_transmission: NOT_ESTABLISHED_BY_THIS_SOURCE
regional_human_pandemic: NOT_ESTABLISHED
```

This belongs in the mesh as a future-risk / capacity surface, not as realized human pandemic harm.

## 3. Visa-pause source correction updates scope, not history

Reuters corrected its August 26 reporting to clarify that the global pause concerns **immigrant-visa appointments**, not all visa services.

Treat as:

```text
EVIDENCE-STATE SCOPE CORRECTION
```

not:

```text
SECOND WORLD EVENT
```

This is a useful live test of source versioning: preserve the earlier publication state, the correction, the changed claim scope, and the access chronology.

## 4. Mail-ballot litigation changes the constraint field

AP reported a new state challenge to USPS implementation of Trump's mail-ballot restrictions after a recent Supreme Court order changed one related injunction posture.

Current lock:

```text
interlocutory / emergency Supreme Court action
!= final merits adjudication that the underlying executive order is lawful
```

The new lawsuit is a fresh litigation/constraint event around an existing policy mechanism, not a wholly new election-policy object.

## Family routing

```text
UNUM-Lattice-News-Intake
  -> owns source items, corrections, candidate state, clocks, lineage

UNUM-Lattice-News
  -> preserves the bounded state-transition / evidence-state interpretation

UNUM-Lattice-News-Real-Bad-Policy
  -> reviews grant-conditioning and immigrant-visa mechanisms

UNUM-Lattice-News-Humanitarian-Environmentalism
  -> watches H5N1 One Health risk and preparedness relation
```

No item from this pass is promoted to `UNUM-Lattice-News-Proven-Harm` merely because it was found.

## Tiny lock

> A bigger archive should create fewer fake events, not more. Preserve what changed: world, evidence, projection, constraint, or forecast.
