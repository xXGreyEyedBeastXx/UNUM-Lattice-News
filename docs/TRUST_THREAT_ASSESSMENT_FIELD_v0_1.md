# Trust & Threat Assessment Field v0.1

**Status:** working infrastructure; non-canonical scoring model  
**Purpose:** add inspectable trust and threat assessment without converting scores into identity, verdict, punishment, authority, or positive moral credit.

## Core separation

```text
TRUST != THREAT != HARM != GUILT != IDENTITY != MORAL GOODNESS
```

Trust asks whether a bounded source/claim deserves epistemic weight.
Threat asks what an actor/system is capable of doing, what direction it is moving, and how much agency it can constrain.
Harm asks what consequences are occurring or have occurred.
Accountability asks how choice, knowledge, power, alternatives, repetition, and causal contribution intersect.

These surfaces may inform one another but must remain separately recoverable.

Trust is an evidence instrument, not a reputation credit. A source may be reliable on one bounded claim while an actor associated with it remains harmful in another causal field.

## Instrument law

Before scoring, preserve a qualitative observation and the evidence packet that produced it.

```text
observation -> dimensions -> evidence -> score/range -> review -> re-entry
```

A score is an instrument output, not a moral identity and not permission to escalate.
Scores must expose their dimensions, weights, missing inputs, uncertainty, and correction history.

## Trust field

Prefer:

```text
trust(source, claim, domain, time)
```

over a universal source reputation number.

Recommended dimensions:

```yaml
trust:
  authenticity: null
  provenance: null
  evidence_recoverability: null
  independence_interest: null
  domain_competence: null
  historical_reliability: null
  correction_reentry: null
  transparency: null
  adversarial_survivability: null
```

### Interpretation

- **authenticity** — confidence that the source is who/what it claims to be.
- **provenance** — whether origin, authorship, date, and lineage can be recovered.
- **evidence_recoverability** — whether documents, data, witnesses, methods, or direct records are exposed.
- **independence_interest** — relevant financial, political, institutional, ideological, or personal interests; low independence is not automatic falsity.
- **domain_competence** — whether the source is positioned to know this particular claim.
- **historical_reliability** — how prior checkable claims survived later evidence.
- **correction_reentry** — whether errors are visibly corrected without erasing lineage.
- **transparency** — ownership, funding, conflicts, methods, anonymous-source handling, AI use when known.
- **adversarial_survivability** — how much of the claim survives serious independent or hostile scrutiny.

A source-history rating may provide a prior, but each consequential claim earns its own assessment.

Repeated citation descendants do not become independent corroboration. Track claim lineage.

## Threat field

Threat is a state of capability, trajectory, and constraint interaction, not an enemy designation.

Recommended dimensions:

```yaml
threat:
  capability: null
  expressed_direction: null
  trajectory: null
  constraint_erosion: null
  reach: null
  target_vulnerability: null
  irreversibility: null
  opacity: null
  precedent_repetition: null
  escalation_potential: null
  repair_capacity: null
  immediacy: null
```

### Interpretation

- **capability** — force, money, law, authority, infrastructure, surveillance, access, technical capacity.
- **expressed_direction** — stated goals, threats, policies, commitments, and repeated rhetoric; distinguish from inferred intent.
- **trajectory** — whether coercive or harmful conduct is accelerating, stabilizing, or receding.
- **constraint_erosion** — weakening, bypass, intimidation, capture, or removal of courts, inspectors, regulators, elections, local sovereignty, whistleblower channels, or other resistance layers.
- **reach** — number and scale of people, systems, territories, ecologies, or institutions potentially affected.
- **target_vulnerability** — how little refusal, exit, appeal, protection, or material resilience affected populations possess.
- **irreversibility** — difficulty of restoring the prior state after damage.
- **opacity** — how hidden, deniable, unauditable, or information-asymmetric the mechanism is.
- **precedent_repetition** — relevant demonstrated use of similar mechanisms.
- **escalation_potential** — ease of conversion from rhetoric/economic pressure into legal, police, military, infrastructural, or other coercion.
- **repair_capacity** — credible correction, restitution, institutional reversal, rehabilitation, or democratic removal routes.
- **immediacy** — distance from activation or ongoing manifestation.

Do not collapse probability and severity into one number. Render at least:

```yaml
threat_summary:
  current_threat: null
  escalation_risk: null
  maximum_plausible_harm: null
```

A high maximum plausible harm with low immediacy is not the same state as moderate harm already occurring.

## Power / Agency / Harm coupling

Threat should be derived from, and remain auditable back to, the News maps:

```text
POWER MAP      -> capability / reach / constraint control
AGENCY MAP     -> vulnerability / alternatives / refusal space
HARM MAP       -> severity / irreversibility / affected populations
TRAJECTORY     -> direction / repetition / escalation
```

This is a projection layer, not a replacement for the underlying maps.

## Prospective scenario branches

Where escalation is uncertain, record the branch before the outcome when possible:

```yaml
scenario:
  trigger: ""
  pathway: []
  evidence_for: []
  evidence_against: []
  discriminators: []
  current_state: inactive|emerging|active|weakened|disproven
```

This prevents retrospective arrow-fitting.

## Scoring discipline

Numeric scoring is optional. Prefer ranges or ordinal bands until calibration exists.

If numeric scores are used:

1. dimensions remain visible;
2. weights are explicit and revisable;
3. missing data does not silently become zero;
4. confidence in the score is separate from the score itself;
5. source trust does not mechanically determine claim truth;
6. source trust does not create moral credit or offset harm;
7. threat does not mechanically determine enforcement;
8. harm does not erase dignity;
9. no score may automatically trigger publication, targeting, punishment, surveillance, exposure, or escalation.

Suggested confidence wrapper:

```yaml
assessment:
  value_or_band: null
  confidence: low|medium|high
  missingness: []
  evidence: []
  counterevidence: []
  weights_version: ""
  assessed_at: ""
  next_reentry: ""
```

## Governance locks

- no body may police itself and count that as independent review;
- accusation alone is insufficient for sanction;
- emergency increases the burden of justification;
- accountability targets conduct and machinery, not disposable identity;
- privacy may protect the weak while secrecy may protect the powerful.

Assessment code, weights, datasets, and outputs require independent review pathways proportional to consequence.

## Actor-node integration

Do not store `trusted`, `untrusted`, `dangerous`, `good`, `bad`, or `enemy` as identity labels.

Attach assessments as dated, scoped records:

```yaml
assessments:
  trust: []
  threat: []
```

Each record must specify claim/domain/event scope, evidence, time, confidence, and revision path.

## Rendition integration

A mature rendition may include:

```yaml
assessment_field:
  trust_assessments: []
  threat_assessments: []
  scenario_branches: []
  score_limitations: []
```

The deterministic evidence packet must remain usable if all scores are removed.

## Tiny locks

> Listen before scoring.

> Score the relation and state, not the soul.

> Trust is claim-local. Threat is trajectory-local. Harm is consequence-local. Dignity is not score-dependent.

> Trust is not moral credit. A score may focus attention. It may never decide alone.
