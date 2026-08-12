# Harmful Intent and Trajectory Model v0.1

Status: active review / harm-hierarchy extension

## Purpose

The Harm Hierarchy Legibility Adversarial Audit needs to distinguish what an actor **wanted or tried to do** from what the actor successfully enacted and from what harm actually occurred.

A failed attempt to impose harm is still evidence about the actor. It must not be counted as realized harm, but it should remain legible as intent, preparation, attempted exercise of power, and future trajectory.

This model therefore adds a fourth public axis beside realized harm, structural harm, and catastrophic risk:

```text
HR = [RHS, SHS, CRS, HIS]
```

where:

- `RHS` = Realized Harm Score;
- `SHS` = Structural Harm Score;
- `CRS` = Catastrophic Risk Score;
- `HIS` = Harmful Intent / Trajectory Score.

`HIS` is not a mind-reading score. It is a score for **evidenced harmful intent or attempted harmful policy**.

## Why intent matters

The following are not equivalent:

```text
actor says nothing harmful and no harmful mechanism exists
actor states a harmful objective but lacks power
actor introduces legislation designed to create the harmful condition
actor orders implementation but courts/legislatures block it
actor successfully implements the harmful condition
actor implements it and people are actually harmed
```

The earlier harm model captured the last two more clearly than the middle cases. This extension preserves the middle.

## Intent evidence classes

### I0 — no supported harmful intent

No currently supported evidence that the actor intended the scoped harm or harmful mechanism.

### I1 — rhetorical hostility / devaluation

Direct statements demean, threaten, exclude, erase, or normalize harm toward a person, population, ecology, or protected civic capacity, but no specific harmful policy or operational pathway is yet identified.

Examples:
- dehumanizing or collective-punishment language;
- explicit desire to reduce a group's rights or standing;
- glorification or normalization of violence or dispossession.

### I2 — stated harmful policy objective

The actor explicitly advocates a policy whose operative mechanism would impose a named harm if enacted.

Examples:
- explicit mass detention or deportation proposal;
- explicit removal of healthcare/food/rights from a named population;
- explicit expansion of settlement/dispossession policy;
- explicit suppression of lawful speech or protest;
- explicit expansion of coercive state power against a civilian population.

### I3 — attempted institutional action

The actor takes formal steps to enact the harmful objective:

```text
introduces bill
signs order
requests appropriation
files litigation
issues agency directive
organizes implementation personnel
pressures another authority
uses funding threat / grant leverage
seeks procurement or deployment
```

The action may fail.

### I4 — operational preparation / partial implementation

Material implementation machinery exists even if the intended endpoint is incomplete or blocked.

Examples:
- facilities contracted;
- personnel deployed;
- databases built;
- weapons transferred;
- enforcement guidance activated;
- partner governments or state/local governments mobilized;
- legal/oversight obstacles removed.

### I5 — explicit intent plus operational execution

The actor's harmful objective is explicit and the actor possesses or exercises a material mechanism capable of producing the intended harm.

This still does not substitute for `RHS`: actual harm must be separately measured.

## Harmful Intent Score dimensions

Score each confirmed intent record from `0-5` on:

```text
harm_severity_intended      severity of the endpoint the actor sought
specificity                 how explicit and bounded the target/mechanism is
capability                   authority/resources available to execute it
preparation                  concrete steps taken toward execution
persistence                  repetition/duration despite opposition or correction opportunities
target_vulnerability         inability of intended targets to refuse, exit, defend, or appeal
```

All scores require evidence anchors.

## HIS formula

Let:

```text
E = (harm_severity_intended + specificity + capability + preparation + persistence + target_vulnerability) / 30
A = responsibility/authority multiplier for the attempted mechanism
```

Then:

```text
HIS = 100 * E * A
```

Recommended authority multiplier uses the existing R0-R5 responsibility scale where appropriate. For pure public advocacy by a leader without formal action, use the responsibility grade attached to the rhetoric/normalization contribution rather than pretending direct implementation occurred.

## Investigation-state rule

Only `CONFIRMED` evidence of the statement, proposal, order, attempted action, or preparation can enter HIS.

A disputed interpretation of what the actor meant remains `PENDING` unless the mechanism itself resolves the ambiguity.

Example:

```yaml
statement_confirmed: true
statement_content: "we should deport X population"
intent_record: CONFIRMED
implementation_success: false
RHS: 0 for unimplemented endpoint
HIS: eligible
```

## Mechanism-over-spin rule

Intent may be inferred from a mechanism where the operative consequence is explicit even if the actor uses euphemistic language, but the inference must be inspectable.

Use:

```text
stated purpose
-> actual operative mechanism
-> necessary/foreseeable target effect
-> actor knowledge / notice
-> persistence or correction response
```

Do not use:

```text
bad outcome -> actor secretly wanted it
```

unless additional evidence supports that inference.

## Notice and persistence

Intent evidence strengthens when an actor receives credible notice of harm and nevertheless preserves, escalates, or repeats the mechanism.

This is not automatic proof that the actor desired every resulting injury.

Record separately:

```text
initial intent
notice of harm
ability to correct
response after notice
escalation / continuation / mitigation / reversal
```

A leader who continues a policy after documented harm may accumulate stronger responsibility or recklessness evidence even when the original stated purpose was different.

## Attempted harm and democratic constraint

Courts, legislatures, elections, civil servants, protesters, foreign governments, or institutional resistance may prevent an intended harmful policy from succeeding.

The prevention does not erase the attempt.

```text
attempt blocked -> RHS may remain 0
attempt blocked -> HIS remains visible
constraint success -> record separately as protective/counter-power evidence
```

## Protective intent is not a negative offset

The harm audit does not subtract unrelated protective intentions from harmful intent.

If the same policy has a genuine protective purpose and a harmful mechanism, preserve both as competing or simultaneous objects only where they bear on interpreting the same act.

A claimed protective intention cannot erase a directly intended harmful endpoint.

## Current hierarchy display

For each actor, institution, or leader within a declared time window display:

```text
Confirmed Realized Harm Points
Confirmed Structural Harm Points
Catastrophic Risk Headline
Harmful Intent / Trajectory Headline
Pending Harm Claims
Path-Forward Investigations
Debunked Claims with explanation
```

This prevents a low-current-power extremist actor from disappearing simply because they have not yet had the authority to execute their agenda, while also preventing rhetoric from being numerically treated as equivalent to actual deaths, imprisonment, dispossession, or deprivation.

## Core locks

```text
intent != realized harm
failed attempt != no evidence about actor
statement != implementation
implementation != every downstream harm
foreseeability != desire
continuation after notice may strengthen responsibility
protective rhetoric != automatic benign intent
hostile rhetoric != automatic proof of every alleged motive
```
