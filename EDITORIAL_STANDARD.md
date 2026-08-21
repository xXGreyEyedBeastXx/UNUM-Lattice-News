# Editorial and Evidence Standard

Updated: 2026-08-21

## Purpose

UNUM Lattice News is an evidence-traced relational reporting and analysis surface. Its credibility depends on preserving the difference between evidence, allegation, inference, uncertainty, judgment, and the exact evidentiary function a fact performs.

Repository-wide investigations should follow `docs/NEWS_OPERATIONS_v0_2.md` and `docs/EVIDENCE_JURISDICTION_AND_LAUNDERING_TAXONOMY_v0_1.md`.

Harm-first investigations should additionally follow `docs/HARM_HIERARCHY_LEGIBILITY_ADVERSARIAL_AUDIT_v0_1.md`, `docs/HARMFUL_INTENT_AND_TRAJECTORY_MODEL_v0_1.md`, and `docs/HARM_MESH_OPERATING_MODEL_v0_1.md`.

## Claim posture

Use explicit posture when it matters:

- **Observed** — directly documented event or consequence.
- **Stated** — attributable public statement or published institutional position.
- **Adjudicated** — a formal finding by a court, tribunal, agency, or other competent adjudicative body, with jurisdiction and procedural status preserved. Adjudicated does not mean metaphysical certainty or immunity from appeal, reversal, or later evidence.
- **Supported inference** — conclusion derived from cited evidence; reasoning should be inspectable.
- **Potential** — capability could produce a named consequence under identifiable conditions.
- **Possible** — a supported causal route exists.
- **Probable / likely** — evidence supports a stronger expectation in a stated scope and horizon.
- **Alleged** — sourced but not independently established.
- **Disputed** — credible evidence or sources materially conflict.
- **Ambiguous** — the recovered evidence supports more than one materially plausible classification, meaning, identity, or causal reading that has not yet been resolved.
- **Unknown** — insufficient evidence for a responsible conclusion.

Do not silently promote one posture into another.

## Evidence jurisdiction

Prime law:

> **Evidence updates only the claim, edge, variable, or model component it actually bears on.**

For consequential evidence, name both the target and function. Preferred functions:

`CLAIM_DEFEATING | SCOPE_LIMITING | DIRECTION | ATTEMPT | CAPACITY | REALIZED_OUTCOME | CONSTRAINT_RESISTANCE | MOTIVE_LIMITING | RELATION_LIMITING | ALTERNATIVE_SUPPORTING | RELIABILITY_MODIFYING | NON_RESPONSIVE`

A true fact may be non-responsive to a nearby claim. Do not let favorable or unfavorable facts bleed across unrelated edges.

Examples:

```text
court blocks an order
-> CONSTRAINT_RESISTANCE + REALIZED_OUTCOME
!= evidence that the order was not attempted

explicit condemnation of extremist group
-> CLAIM_DEFEATING for "never condemned"
-> possibly MOTIVE_LIMITING for a specific endorsement claim
!= erasure of independently evidenced policy, amplification, clemency, appointment, or reception edges
```

### Direction / attempt / capacity / result / resistance

Keep separate:

```text
D = demonstrated direction/objective
A = attempted implementation
C = available capacity
R = realized result
S = surviving resistance/constraint
```

Failure of an attempted objective limits realized harm and demonstrated capacity. It does not retroactively defend the attempt.

## Investigation state for adversarial harm review

Use:

- **PENDING** — unresolved.
- **PATH_FORWARD** — concrete evidence route identified but incomplete.
- **CONFIRMED** — scoped claim sufficiently established for repository use.
- **DEBUNKED** — scoped claim affirmatively defeated after reconstructing its strongest form.

`DEBUNKED` carries a higher burden than failure to confirm.

```text
NOT_SEARCHED != DEBUNKED
SEARCHED_NOT_FOUND != DEBUNKED
EXPECTED_BUT_MISSING != DEBUNKED
authority denial != DEBUNKED
lack of charges != DEBUNKED
procedural dismissal != automatic factual DEBUNKING
successful resistance != DEBUNKING of the attempt
```

## Adversarial search posture

Power-bearing actors do not receive a charitable presumption merely because conduct is official, legal, bipartisan, allied, popular, profitable, contractual, market-normal, or described as security policy.

Adversarial investigation does not authorize predetermined guilt.

```text
suspicion != finding
harmful consequence != proof of private intent
institutional authority != credibility privilege
profitability != legitimacy
legality != harmlessness
```

## Intent, knowledge, and accountability

Where these questions matter, keep separately evidenced:

```text
intentional action / term-setting
intended gain / cost reduction / capacity increase
intent to cause the downstream harmful endpoint
knowledge / notice
capacity to know
foreseeability
capacity to correct
response after notice
realized harm
gain or insulation retained after notice
repair or mitigation
```

An actor does not have to desire every downstream injury for a deliberately chosen wage, price, rent, fee, access condition, policy, contract, staffing rule, or other term to be intentional.

At the same time, profit or gain alone does not prove extraction. Where extraction or capture is alleged, trace the loss-bearer, mechanism, costs or productive contribution, counterfactual, gain, and terminal or reseated beneficiary.

Greater power does not prove actual knowledge or guilt. It may increase practical capacity to investigate, model, receive warning, change course, and repair. Continued conduct after credible notice is a separate accountability fact when evidenced.

```text
intentional term-setting != harmful-endpoint intent
lack of harmful-endpoint intent != accidental mechanism
capacity_to_know != actual_knowledge
foreseeability != desire
credible_notice != proof of secret motive
deliberate_avoidance requires evidence
```

Uncertainty on the motive or knowledge edge must not leak into neighboring mechanism, outcome, loss, gain, or beneficiary edges as generalized exculpation.

## Source discipline

Prefer primary/direct evidence where available. Preserve source, date, institution/author, context, and claim lineage.

Repeated reports are not automatically independent corroboration. Citation inheritance must remain visible.

## Relational mapping

A documented relationship is not automatically coordination, control, guilt, conspiracy, membership, or causation.

Distinguish ownership, investment, contract, employment, partnership, dependency, infrastructure, public statement, regulatory authority, litigation, technical integration, chronological proximity, material term-setting, cost externalization, notice, persistence, mitigation, repair, and terminal gain.

## Laundering classification discipline

Use laundering labels only as typed transformation claims.

Recognized classes include causal-partition, truth/citation-lineage, legality, voluntariness, moral, ethical, reputation, patronage-return, financial-provenance obscuration, and legally grounded money-laundering claims.

`MONEY_LAUNDERING_LEGAL_CLAIM` is reserved for an actual legal/financial claim with the required jurisdiction-specific elements. Do not use it as metaphor for ordinary conflicts, donations, shell structures, opacity, or disliked financial conduct.

`LITERAL_LAUNDRY` means washing textiles. It is not evidence of any other laundering class.

## Human and ecological protection

Analysis should examine consequences for dignity, consent, refusal, exit, appeal, bodily/cognitive sovereignty, labor, material security, democratic accountability, plural life, ecological continuity, and sustaining material environments.

Institutions, governments, movements, ethnic groups, religions, populations, and individuals are not interchangeable categories. Collective blame and dehumanization are prohibited.

### Negative-only harm ledger rule

A harm audit is not a net-morality ledger. Beneficial conduct elsewhere does not cancel documented harm.

Do not add unrelated accomplishments merely for rhetorical balance.

Evidence that bears on the scoped claim must be preserved under its actual jurisdiction. Unrelated favorable conduct is `NON_RESPONSIVE`, not counterweight.

## Harm hierarchy discipline

Harm rankings must be time-bounded and category-bounded. Separate institutions, leaders, non-leader actors, and affected populations where necessary.

Shared underlying harms must not be multiplied across every responsible actor.

The public harm rating is a four-axis accountability surface:

```text
[realized harm, structural harm, catastrophic risk, harmful intent / trajectory]
```

The harmful-intent/trajectory axis does not turn rhetoric into realized injury and does not substitute for the separate knowledge/notice/accountability fields.

A harm rating is an accountability summary, not criminal liability and not permission for punishment.

## Privacy and safety

Do not publish private addresses, credentials, unnecessary medical/family information, protected source identities, or operational detail whose primary value is facilitating violence, stalking, sabotage, or abuse.

Opacity is not itself wrongdoing. Distinguish protective privacy from accountability-shielding secrecy.

## Copyright and provenance

Prefer links, citations, short necessary quotations, and original synthesis. Preserve third-party provenance and rights.

## Corrections

Correct material errors visibly. Preserve what changed, why, and what remains unresolved.

A `CONFIRMED` claim may return to `PENDING` or become `DEBUNKED` when evidence actually defeats its basis. Status changes retain lineage.

## Agent boundary

Automated or AI-assisted research may locate, compare, organize, calculate, cluster, map, and draft. It must not independently publish consequential accusations, fabricate citations, erase uncertainty, infer private facts, expose protected identities, use evidence outside its declared jurisdiction, convert capacity-to-know into actual knowledge, or infer secret motive solely from harmful outcome or persistence.

Human review remains required for consequential public claims until governance explicitly grants narrower safe authority.

## Tiny lock

> A fact may be true and still be answering the wrong question. Route it before you weigh it. And do not let uncertainty about motive make the mechanism disappear.
