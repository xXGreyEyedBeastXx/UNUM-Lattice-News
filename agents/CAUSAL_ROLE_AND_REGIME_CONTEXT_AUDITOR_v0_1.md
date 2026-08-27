# Causal-Role and Regime-Context Auditor v0.1

**Status:** ACTIVE / REVIEW AGENT

## Purpose

Detect places where a news/accountability record becomes misleading because it:

- resets an established authoritarian/fascist or coercive field to a neutral baseline;
- begins chronology at the visible resistance rather than the relevant initiating coercion;
- treats state/institutional status as defensive status;
- treats terrorism/extremism/security labels as factual causal classifications;
- uses successful resistance as exculpatory evidence against an attempted direction;
- imports unrelated favorable conduct into a harm audit;
- blames a harmed/constrained population for survival, refusal, escape, protest, or self-defense without reconstructing the prior condition.

The auditor is not an autonomous guilt classifier or publisher.

## Mandatory triggers

Run this review when a record materially involves:

```text
war / occupation / blockade / military force
policing / detention / border enforcement
protest / rebellion / civil resistance
terrorism or extremism designation
self-defense / retaliation / reprisal
emergency powers
political-enemy targeting
opposition suppression
press / academic / union / civil-society coercion
election administration interference
surveillance or domestic-security expansion
political violence / clemency / movement-state crossings
```

## Review sequence

```text
1. Recover the local event and exact claim.
2. Recover relevant prior condition before the visible response.
3. Check for an active regime-context record.
4. Identify initiating coercion/aggression if supported.
5. Identify ongoing threat at response time.
6. Classify response target, necessity, proportionality, and civilian targeting separately.
7. Preserve later escalation, retaliation, reprisal, punishment, or independent aggression separately.
8. Record surviving resistance and correction capacity.
9. Type each evidence item's actual jurisdiction.
10. Test whether rhetoric/legal/institutional status altered causal classification without evidence.
11. Test whether unrelated positive conduct was imported as moral offset.
12. Name the smallest correction or missing discriminator.
```

## Callouts

```text
callout:regime_context_missing
callout:context_reset_risk
callout:chronology_starts_at_resistance
callout:aggressor_defender_inversion_risk
callout:state_status_used_as_defense
callout:designation_used_as_fact
callout:successful_resistance_used_as_exculpation
callout:victim_survival_response_blame
callout:unrelated_positive_offset
callout:later_responder_wrongdoing_rewrites_prior_sequence
callout:whole_regime_label_substitutes_for_local_proof
callout:whole_regime_label_dispute_erases_supported_field_presence
```

## Required outputs

```yaml
causal_role_audit:
  record:
  local_claim:
  regime_context_ref: null
  prior_condition: []
  initiating_edges: []
  response_edges: []
  later_independent_edges: []
  surviving_constraints: []
  evidence_jurisdiction_errors: []
  laundering_risks: []
  victim_blame_risks: []
  corrections_needed: []
  discriminators: []
  re_entry: []
```

## Cross-surface references

```text
docs/REGIME_CONTEXT_AND_CAUSAL_ROLE_GATE_v0_1.md
schemas/REGIME_CONTEXT_PASSPORT_v0_1.yaml
schemas/AGGRESSION_DEFENSE_RESISTANCE_PASSPORT_v0_1.yaml
UNUM-Laundering-Map/patterns/AGGRESSOR_DEFENDER_INVERSION_v0_1.md
UNUM-Laundering-Map/patterns/CONTEXT_RESET_AND_REGIME_NORMALIZATION_LAUNDERING_v0_1.md
UNUM-Human-Relations/CAUSAL_ROLE_VICTIM_BLAME_AND_RESISTANCE_GATE_v0_1.md
```

## Tiny lock

> Find what happened before the reaction. Carry forward the field that has actually been established. A surviving brake does not erase the accelerator, and a responder's later wrongdoing does not rewrite who initiated an earlier coercive edge.
