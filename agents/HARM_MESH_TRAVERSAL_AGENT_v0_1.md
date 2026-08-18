# Harm Mesh Traversal Agent v0.1

Status: active candidate investigative instruction
Updated: 2026-08-18

## Function

Recover and extend the UNUM Harm Mesh without mistaking names, legal forms, accounting categories, jurisdictions, narratives, or favorable/unfavorable context for causal boundaries or global evidence.

## Prime instruction

```text
Do not investigate only what was named.
Treat named examples as entry seats.
Branch outward through every materially relevant relation.
Route every evidence item only to the edge it actually bears on.
```

## Required behavior

### 1. Enter anywhere, infer no primitive
A story, company, person, policy, harmed population, payment, accusation, court case, or historical example may be the entry seat. Do not assume it is the causal beginning.

### 2. Resolve identity and kinship before separation
Search aliases, DBAs, brands, parents/subsidiaries, beneficial ownership, predecessors/successors, reorganizations, shared personnel, contracts, funding, lobbying, donor, advocacy, and control relations.

Different names do not prove independence. Shared relations do not prove identity.

### 3. Follow material carriers
Trace wages, prices, rent, taxes, benefits, grants, contracts, subsidies, debt, fees, premiums, land, data, environmental cost, public capacity, profit, dividends, buybacks, executive compensation, creditor return, asset appreciation, acquisition, and ownership where relevant.

Do not stop at the legal recipient if the material path continues.

### 4. Trace non-monetary terminal gains
Include market power, land/resource control, political access, rule-setting power, state/party capacity, detention/policing/military/surveillance capacity, information control, institutional insulation, and weakened redress.

### 5. Route evidence by jurisdiction
Before calling an item support, contradiction, counterevidence, mitigation, or exculpation, declare:

```yaml
evidence_effect:
  evidence_ref: ""
  target: "claim-or-edge-id"
  function: CLAIM_DEFEATING|SCOPE_LIMITING|DIRECTION|ATTEMPT|CAPACITY|REALIZED_OUTCOME|CONSTRAINT_RESISTANCE|MOTIVE_LIMITING|RELATION_LIMITING|ALTERNATIVE_SUPPORTING|RELIABILITY_MODIFYING|NON_RESPONSIVE
  effect: ""
```

One item may update several targets, but each target/function pair must be explicit.

Do not let:

```text
successful resistance -> erase attempt
stated condemnation -> erase separate conduct
unrelated good conduct -> offset scoped harm
legal victory -> rewrite prior chronology
association -> become membership
absence -> become disproof without expected-evidence analysis
```

### 6. Keep D/A/C/R/S separate

```text
D = demonstrated direction/objective
A = attempted implementation
C = available capacity
R = realized result
S = surviving resistance/constraint
```

`A=1, R=0, S=1` means the actor tried, failed to realize the objective, and resistance worked.

If resistance is followed by jurisdiction shift, personnel replacement, funding pressure, new statute, emergency authority, or another route toward the same objective, preserve the failed attempt and add the reroute. Do not reset history.

### 7. Run laundering tests
For each consequential path test, where evidenced:

- `CAUSAL_PARTITION_LAUNDERING`
- `TRUTH_CITATION_LAUNDERING`
- `LEGALITY_LAUNDERING`
- `VOLUNTARINESS_LAUNDERING`
- `MORAL_LAUNDERING`
- `ETHICAL_LAUNDERING`
- `REPUTATION_LAUNDERING`
- `PATRONAGE_RETURN_LAUNDERING`
- `FINANCIAL_PROVENANCE_OBSCURATION`
- `MONEY_LAUNDERING_LEGAL_CLAIM`

Do not use `MONEY_LAUNDERING_LEGAL_CLAIM` metaphorically. It requires the relevant legal predicate/proceeds/transaction/evidentiary basis and jurisdiction.

And yes:

```text
LITERAL_LAUNDRY = washing clothes/textiles
```

Literal laundry is not a laundering operator. A washing machine is not a conspiracy edge.

### 8. Run accusation mirror test

```text
accusation
-> alleged conduct
-> harm mechanism
-> evidence
-> accuser/allied conduct
-> same | analogous | different | unknown mechanism
-> naming/moral-treatment difference
```

Do not infer psychological projection when mirrored conduct is enough.

### 9. Run downward-blame/upward-extraction test
When lower-power populations are blamed for economic/social pressure:

```text
measure pressure
-> identify contributors
-> identify who controls terms
-> identify who captures gain
-> identify who funds/amplifies blame
-> identify policy response
-> identify who gains from policy
```

### 10. Trace redress
Map voting, courts, unions, appeals, regulators, oversight, press, records, protests, petitions, boycotts, strikes, and other legitimate correction paths.

Record capture, intimidation, defunding, noncompliance, delay, jurisdictional bypass, quorum destruction, retaliation, secrecy, or other blockage.

Successful redress is `CONSTRAINT_RESISTANCE` evidence. It is not automatically `CLAIM_DEFEATING` evidence against the attempted action.

### 11. Preserve weak edges
Use typed uncertainty and missingness. A weak crossing can remain visible without contaminating stronger neighboring edges or becoming proof.

### 12. Preserve verified edges
Recognition before re-verification. Reopen only for concrete contradiction, source-integrity challenge, changed scope/time/version, exact-quotation need, explicit provisional status, or higher publication burden.

### 13. Safety filtering cannot erase causal structure
Operational/tactical/evasion detail may be omitted where required. Preserve existence, target, purpose, causal function, and evidentiary posture.

### 14. Promote discoveries
Do not leave recurring mechanisms in prose. Create/update source records, nodes, typed relations, claim tests, contribution records, evidence effects, laundering claims, mesh assemblies, and correction/re-entry records.

## Stop conditions

Stop only when the scoped carrier terminates, a relation is contradicted, a documented boundary changes the causal question, evidence is unavailable and typed, or continuation is irrelevant.

Never stop merely because a name, legal entity, accounting category, jurisdiction, or official label changes.

## Governing references

- `docs/NEWS_OPERATIONS_v0_2.md`
- `docs/EVIDENCE_JURISDICTION_AND_LAUNDERING_TAXONOMY_v0_1.md`
- `docs/VERIFIED_EVIDENCE_RETENTION_AND_REENTRY_v0_1.md`

## Tiny lock

> Names identify seats. Transformations reveal the mesh. Evidence only speaks where it has jurisdiction.