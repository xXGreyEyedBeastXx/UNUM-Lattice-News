# Evidence Jurisdiction and Laundering Taxonomy v0.1

Status: active operational rule
Updated: 2026-08-18

## Prime law

> **Evidence updates only the claim, edge, variable, or model component it actually bears on.**

Evidence does not acquire a global positive or negative sign merely because it is favorable or unfavorable to an actor.

```text
true fact != answer to every nearby question
constraint success != defense of the attempted objective
stated condemnation != erasure of contradictory conduct
association evidence != membership evidence
legal outcome != moral exoneration
```

For an evidence item `e`, declare its jurisdiction as one or more target/function pairs:

```text
J(e) = {(target_1, function_1), (target_2, function_2), ...}
```

If a target is outside `J(e)`, the update is zero for that target.

## Evidence-effect functions

Use these functions instead of an undifferentiated `counterevidence` bucket:

- `CLAIM_DEFEATING` — directly contradicts or makes the scoped claim untenable.
- `SCOPE_LIMITING` — narrows actor, population, chronology, mechanism, magnitude, or domain.
- `DIRECTION` — bears on demonstrated preference/objective/trajectory.
- `ATTEMPT` — bears on whether implementation was actually attempted.
- `CAPACITY` — bears on practical ability to execute the objective.
- `REALIZED_OUTCOME` — bears on what actually happened.
- `CONSTRAINT_RESISTANCE` — bears on whether a court, election, agency, civil society actor, market, law, or other constraint blocked/limited the action.
- `MOTIVE_LIMITING` — weakens a claim about motive without erasing conduct or outcome.
- `RELATION_LIMITING` — weakens a claimed relation such as coordination, membership, ownership, control, or causation.
- `ALTERNATIVE_SUPPORTING` — strengthens a competing causal explanation.
- `RELIABILITY_MODIFYING` — changes confidence in a source, measurement, testimony, or evidence lineage.
- `NON_RESPONSIVE` — true/relevant context that does not update the scoped claim or edge under review.

One evidence item may carry more than one function, but each function must name its target.

## Direction / attempt / capacity / result / resistance lock

Keep these variables independent:

```text
D = demonstrated direction or objective
A = attempted implementation
C = available operational capacity
R = realized result
S = surviving resistance / constraint
```

Therefore:

```text
A=1, R=0, S=1
```

means:

> the actor tried; the objective was not realized; resistance worked.

It does **not** mean the actor partly did not try.

A blocked attempt limits realized harm and demonstrated capacity. It does not retroactively defend the attempt. If an actor returns through a new mechanism after resistance, preserve the earlier attempt and add the reroute as evidence of persistence.

## Legacy `counterevidence` migration

Existing records may retain `counterevidence` for historical compatibility. New and materially revised records should use `evidence_effects`.

When migrating a legacy item:

1. identify the exact claim/edge/variable it bears on;
2. assign one or more evidence-effect functions;
3. mark unrelated nearby claims `NON_RESPONSIVE` when leakage is plausible;
4. preserve the original wording/source lineage;
5. do not convert `CONSTRAINT_RESISTANCE` or `REALIZED_OUTCOME` into `CLAIM_DEFEATING` unless it truly defeats the scoped claim.

## Laundering family

`laundering` is a transformation claim: something materially consequential is made to appear cleaner, independent, legitimate, voluntary, neutral, unrelated, or differently owned by changing labels, partitions, provenance, accounting seats, institutional forms, or narratives.

Do not assign a laundering label from dislike or resemblance alone. Trace the transformation.

### Investigative laundering classes

- `CAUSAL_PARTITION_LAUNDERING` — splits one causal path into compartments so responsibility or gain appears disconnected.
- `TRUTH_CITATION_LAUNDERING` — inherited claims acquire false independence/authority through repetition or citation chains.
- `LEGALITY_LAUNDERING` — legality or formal compliance is used as proof of legitimacy or harmlessness.
- `VOLUNTARINESS_LAUNDERING` — formal agreement/choice obscures coercion, dependency, asymmetry, confinement, or lack of realistic exit.
- `MORAL_LAUNDERING` — naming, role partition, reputation, or institutional prestige changes moral treatment without changing the underlying transformation.
- `ETHICAL_LAUNDERING` — an ethics process, code, disclosure, recusal claim, review board, compliance ritual, or professional norm is used to imply ethical resolution while the material conflict/harm remains unresolved.
- `REPUTATION_LAUNDERING` — unrelated prestige, charity, favorable biography, credentials, or public-service achievements are used to offset or obscure a scoped harmful mechanism.
- `PATRONAGE_RETURN_LAUNDERING` — benefits return through indirect access, appointments, contracts, donations, clemency, favors, or network intermediaries while appearing disconnected from the originating support.
- `FINANCIAL_PROVENANCE_OBSCURATION` — source, ownership, destination, beneficial control, or economic purpose of funds is obscured without yet asserting the legal crime of money laundering.
- `MONEY_LAUNDERING_LEGAL_CLAIM` — reserved for a legally grounded money-laundering allegation/finding with the required predicate/proceeds/transaction/evidentiary elements for the relevant jurisdiction. Do not use metaphorically.

### Literal laundry lock

- `LITERAL_LAUNDRY` — washing clothes, linens, uniforms, textiles, or comparable physical goods.

Literal laundry is not evidence of financial, moral, ethical, causal, or epistemic laundering. The presence of the word `laundry` must not trigger an investigative laundering operator without the relevant transformation.

Yes, the lattice recognizes laundry.

## Laundering-claim record

Use a typed claim rather than an adjective:

```yaml
laundering_claim:
  type: MORAL_LAUNDERING
  posture: supported_inference
  source_state: ""
  transform_or_partition: ""
  cleaned_or_obscured_appearance: ""
  underlying_relation_preserved: ""
  beneficiary_or_accountability_effect: ""
  evidence_effects: []
  strongest_alternative: ""
  discriminator: ""
```

For `MONEY_LAUNDERING_LEGAL_CLAIM`, add jurisdiction, statutory/legal theory, alleged predicate proceeds, transaction path, knowledge/intent evidence where required, and adjudication status.

## Anti-laundering check

Before accepting an exculpatory, legitimizing, or condemnatory narrative, ask:

```text
What exact edge is being updated?
What changed materially?
What changed only in name, accounting, jurisdiction, legal form, or story?
Did harm disappear, or only move ledgers?
Did gain disappear, or only reseat?
Did responsibility terminate, or distribute?
Did resistance defeat the objective, or only block the outcome?
Is a true fact being used to answer the wrong question?
```

## Tiny lock

> Evidence gets jurisdiction, not a team jersey. The only laundering that needs no causal audit is the kind with soap.