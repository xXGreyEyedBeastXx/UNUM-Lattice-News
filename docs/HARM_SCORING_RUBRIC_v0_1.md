# Harm Scoring Rubric v0.1

Status: active review / calibration required

## Purpose

This rubric turns confirmed harm records into sortable hierarchy values without hiding the underlying evidence or pretending moral judgment is exact arithmetic.

The score is an indexing instrument. The contribution record, harm vector, affected population, source chain, and responsibility grade remain primary.

See `docs/HARM_HIERARCHY_LEGIBILITY_ADVERSARIAL_AUDIT_v0_1.md`.

## Eligibility

Only `CONFIRMED` contribution or consolidated shared-harm attribution records may enter confirmed hierarchy totals.

```text
PENDING      -> visible, not counted
PATH_FORWARD -> visible, not counted
CONFIRMED    -> eligible to count
DEBUNKED     -> excluded, explanation retained
```

A contribution may be confirmed as conduct while a downstream causal claim remains pending. Score only the confirmed scope.

## Harm dimensions: 0-5

Use integer scores with a written explanation.

### General severity anchors

```text
0 = no currently supported harm in this dimension for the scoped contribution
1 = limited / low-intensity harm
2 = moderate harm with meaningful consequence
3 = serious harm or durable rights/material loss
4 = severe harm, repeated grave injury, or large structural deprivation
5 = extreme harm within the category, including killing, torture, permanent dispossession, systemic rights destruction, or comparable endpoint
```

The severity score measures the type/intensity of harm. Reach is scored separately so population size is not hidden inside severity.

### Realized-harm dimensions

```text
lethal_physical_harm
confinement_coercion
material_deprivation
rights_agency_harm
land_sovereignty_displacement
ecological_future_harm
democratic_epistemic_harm
```

### Structural-harm dimension

```text
power_concentration
```

Power concentration includes increased executive, military, police, carceral, surveillance, monopoly, evidence-control, or other coercive capacity and reduced independent resistance or oversight.

### Catastrophic-risk dimension

```text
catastrophic_risk_imposition
```

Keep extreme-tail risk separate from realized injury. A nuclear-war escalation pathway must not be numerically represented as though the forecast deaths have already occurred.

## Propagation dimensions: 0-5

### Reach

Use the best available affected-population or affected-system estimate and preserve the raw number/range when known.

```text
0 = no confirmed exposure
1 = individual / household / very small localized group
2 = tens to hundreds, or a bounded local community/system
3 = thousands to tens of thousands, or regional-scale exposure
4 = hundreds of thousands to several million, or major national-scale subsystem
5 = ten million+, population-wide, transnational, or ecosystem-scale exposure
```

For land/ecology, use the closest functional analogue and preserve acreage, habitat range, watershed, population, or other native unit.

### Duration

```text
0 = no duration
1 = hours to days
2 = weeks to months
3 = approximately 1-4 years
4 = approximately 5-19 years
5 = multi-decade, intergenerational, or effectively permanent
```

### Irreversibility

```text
0 = no loss / fully reversible
1 = readily correctable
2 = reversible with meaningful cost or delay
3 = only partially reversible / durable loss
4 = permanent for many affected people or systems
5 = death, extinction, destroyed sacred/cultural object, irreversible bodily injury, permanent dispossession, or comparable endpoint
```

### Vulnerability

```text
0 = target has equal or greater power and easy exit
1 = ordinary asymmetry
2 = meaningful institutional/economic disadvantage
3 = dependent population with constrained alternatives
4 = captive, detained, occupied, medically dependent, impoverished, disenfranchised, or otherwise strongly constrained
5 = extreme dependence / inability to exit or protect oneself, including children in custody, severely disabled captive populations, populations under siege, or comparable conditions
```

Do not infer vulnerability from identity alone. Score the actual relationship.

## Responsibility attribution

Use the repository responsibility grade and internal multiplier:

```text
R0 adjacency                                      0.00
R1 rhetorical support / normalization             0.15
R2 vote / endorsement / formal support             0.35
R3 sponsorship / funding / material facilitation   0.60
R4 leadership / decisive enabling / command        0.85
R5 direct operational control                      1.00
```

The multiplier is an audit convenience, not a legal-liability formula.

If multiple actions by the same actor contribute to one shared harm, first consolidate them into one actor-to-shared-harm attribution so the same victims are not counted repeatedly.

## Realized Harm Score (RHS)

Let:

```text
D = sum of the seven realized-harm dimension scores / 35
P = (reach + duration + irreversibility + vulnerability) / 20
A = responsibility multiplier
```

Then:

```text
RHS_contribution = 100 * D * (0.5 + 0.5 * P) * A
```

Rationale:
- `D` preserves multi-domain seriousness;
- propagation can amplify but cannot erase a severe individualized harm;
- attribution limits how much of the shared harm is assigned to a contributor.

RHS is not capped across an actor's entire history. An actor with many independently confirmed harms can accumulate more confirmed harm points than an actor with one harm.

## Structural Harm Score (SHS)

Let:

```text
C = power_concentration / 5
S = (reach + duration + irreversibility) / 15
A = responsibility multiplier
```

Then:

```text
SHS_contribution = 100 * C * (0.5 + 0.5 * S) * A
```

Structural harm is scored even when no later victim endpoint has yet been confirmed, provided the power expansion itself is confirmed.

Examples:
- expanding detention capacity;
- transferring military capability into domestic policing;
- removing independent oversight;
- centralizing executive control over formerly independent functions.

## Catastrophic Risk Score (CRS)

Catastrophic risk needs an additional `pathway_support` score from 0-5:

```text
0 = no supported causal pathway
1 = theoretical pathway only
2 = plausible pathway with some relevant conditions
3 = concrete pathway with material capability and partial conditions present
4 = active escalation pathway with multiple necessary conditions present
5 = immediate or near-immediate pathway with high capability and weak remaining barriers
```

Let:

```text
K = catastrophic_risk_imposition / 5
Q = pathway_support / 5
A = responsibility multiplier
```

Then:

```text
CRS_contribution = 100 * K * Q * A
```

Do not translate CRS into a probability of catastrophe unless a separate quantitative risk model supports doing so.

For actor-level display, use the **maximum confirmed CRS pathway** as the headline catastrophic-risk score and list additional independent pathways below it. Do not mechanically sum overlapping extinction or nuclear-war pathways.

## Actor / institution hierarchy totals

For each declared time window:

```text
Confirmed Realized Harm Points = sum(deduplicated RHS contributions)
Confirmed Structural Harm Points = sum(deduplicated SHS contributions)
Catastrophic Risk Headline = max(confirmed CRS pathways)
```

Public rating:

```text
HR = [confirmed_realized_harm_points,
      confirmed_structural_harm_points,
      catastrophic_risk_headline]
```

Sort within the same hierarchy class and time window primarily by confirmed realized harm points, while always displaying structural harm and catastrophic risk beside it.

If rankings are sensitive to uncertain reach, attribution, or overlapping harms, show a range and mark the ordering `PROVISIONAL` rather than manufacturing precision.

## No positive offset

There is no subtraction term for beneficial conduct.

```text
harm points - good deeds = prohibited model
```

This is a harm inventory, not a net virtue score.

A protective action may be documented elsewhere and may bear on causation or mitigation of the *same* harm, but unrelated good conduct does not erase confirmed injury.

## Calibration requirement

Before publishing a league-table style ranking, calibrate this rubric on a mixed historical set containing:
- individualized physical harm;
- mass civilian harm;
- detention and coerced labor;
- healthcare/food deprivation;
- Indigenous land or sovereignty loss;
- oversight destruction;
- military/police power concentration;
- low-probability catastrophic-risk imposition.

If the ordering repeatedly contradicts obvious magnitude differences because of the arithmetic, revise the formula rather than defending the score.

The hierarchy serves the evidence. The evidence does not serve the hierarchy.
