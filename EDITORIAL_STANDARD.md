# Editorial and Evidence Standard

## Purpose

UNUM Lattice News is an evidence-traced relational reporting and analysis surface. Its credibility depends on preserving the difference between evidence, allegation, inference, uncertainty, and judgment.

Repository-wide investigations should also follow [docs/NEWS_OPERATIONS_v0_2.md](docs/NEWS_OPERATIONS_v0_2.md). That operations layer coordinates this evidence standard with power, constraint/agency, harm/benefit, missingness, competing-model, oversight, correction, and re-entry review. It does not override this standard.

Harm-first investigations should additionally follow [docs/HARM_HIERARCHY_LEGIBILITY_ADVERSARIAL_AUDIT_v0_1.md](docs/HARM_HIERARCHY_LEGIBILITY_ADVERSARIAL_AUDIT_v0_1.md).

## Claim posture

Use explicit posture when it matters:

- **Observed** — directly documented event or consequence.
- **Stated** — attributable public statement or published institutional position.
- **Supported inference** — conclusion derived from cited evidence; reasoning should be inspectable.
- **Potential** — capability could produce a named consequence under identifiable conditions.
- **Possible** — a supported causal route exists.
- **Probable / likely** — evidence supports a stronger expectation in a stated scope and horizon.
- **Alleged** — sourced but not independently established.
- **Disputed** — credible evidence or sources materially conflict.
- **Unknown** — insufficient evidence for a responsible conclusion.

Do not silently promote one posture into another.

When absence itself matters, use the typed missingness states defined in `NEWS_OPERATIONS_v0_2.md` rather than collapsing all absence into `Unknown` or `no evidence`.

## Investigation state for adversarial harm review

Claim posture and investigation state are independent fields.

Use exactly four top-level investigation states for harm-audit workflow:

- **PENDING** — unresolved; evidence, attribution, mechanism, scope, or causation remains insufficient or materially conflicted.
- **PATH_FORWARD** — a concrete recoverable evidence route is identified but not completed.
- **CONFIRMED** — the scoped claim is sufficiently established for repository use under this standard.
- **DEBUNKED** — the scoped claim has been affirmatively defeated after reconstructing the strongest version of the claim and documenting why the recovered evidence contradicts or makes it untenable.

`DEBUNKED` carries a higher burden than failure to confirm.

```text
NOT_SEARCHED != DEBUNKED
SEARCHED_NOT_FOUND != DEBUNKED
EXPECTED_BUT_MISSING != DEBUNKED
authority denial != DEBUNKED
lack of charges != DEBUNKED
procedural dismissal != automatic factual DEBUNKING
```

A debunking record should preserve the claim tested, strongest support, expected evidence, recovered evidence, decisive failure, explanation, and any narrower residual claim that survives.

Only `CONFIRMED` contributions may add to the confirmed harm hierarchy. Pending and path-forward material remains visible for investigation but does not count as confirmed realized harm.

## Adversarial search posture

Power-bearing actors do not receive a charitable presumption merely because their conduct is official, legal, bipartisan, allied, popular, or described as security policy.

The harm audit may intentionally search for the strongest negative case first, especially where civilians, vulnerable populations, public rights, land, ecology, or democratic accountability bear the downside.

This search posture does not authorize a predetermined factual or legal conclusion.

The repository must distinguish:

```text
adversarial investigation != presumption of legal guilt
suspicion != finding
harmful consequence != proof of private intent
institutional authority != credibility privilege
```

## Threat assessment

Threat records should separate at least three dimensions:

1. **Likelihood / evidence posture** — how supported or expected is the causal route?
2. **Consequence** — what happens if it occurs, and to whom or what?
3. **Confidence** — how confident are we in the assessment given source quality and missing information?

A low-confidence catastrophic possibility may deserve investigation without being presented as established fact. Observed harm does not automatically prove universal intent.

Threat assessment is not enemy designation and does not itself authorize intervention.

## Source discipline

Prefer primary and direct evidence where available. Preserve enough information to recover the source, date, author or institution, and relevant context.

Useful source classes include:

- primary documents and datasets;
- legislation, court records, regulatory filings, and public records;
- official statements;
- peer-reviewed or technically inspectable research;
- high-quality investigative reporting;
- direct interviews and testimony;
- secondary analysis and commentary, clearly identified as such.

When sources materially disagree, expose the disagreement rather than manufacturing certainty.

Repeated reports are not automatically independent corroboration. Where later accounts inherit a claim from the same upstream source, preserve that claim lineage rather than counting repetition as independent evidence.

## Relational mapping

A documented relationship is not automatically evidence of coordination, control, guilt, or conspiracy.

Maps should distinguish relationships such as ownership, investment, contract, employment, partnership, dependency, infrastructure, public statement, regulatory authority, litigation, technical integration, and chronological proximity.

Do not collapse distinct relation types into an unlabeled edge.

For mature investigations, also distinguish the relation's function within the linked power, constraint/agency, and harm/benefit maps defined in `NEWS_OPERATIONS_v0_2.md`.

## Human and ecological protection

Analysis should examine consequences for dignity, consent, refusal, exit, appeal, bodily and cognitive sovereignty, labor, democratic accountability, plural life, ecological continuity, and sustaining material environments.

Institutions, corporations, governments, movements, ethnic groups, religions, populations, and individuals are not interchangeable categories. Collective blame and dehumanization are prohibited.

Accountability attaches to evidenced conduct, participation, authority, causal contribution, and institutional machinery. Human dignity remains under consequence.

### Negative-only harm ledger rule

A harm audit is not a net-morality ledger. Beneficial conduct elsewhere does not cancel or numerically offset a documented harm.

Do not add unrelated accomplishments merely to create rhetorical balance.

Counterevidence must still be preserved when it bears on the claim's identity, chronology, mechanism, scope, causation, magnitude, attribution, or evidentiary reliability.

## Harm hierarchy discipline

Harm rankings must be time-bounded and category-bounded.

Maintain separate hierarchy surfaces for institutions, leaders, and non-leader actors. Do not force unlike actor classes into one scalar ranking when that destroys legibility.

Every ranked entry should remain traceable to individual confirmed contribution records and affected populations.

Where multiple actors contributed to the same underlying death, deprivation, displacement, or other harm, preserve the shared harm object and actor-specific responsibility instead of multiplying the underlying victim count across every actor.

A harm rating is an accountability summary, not a finding of criminal liability and not permission for punishment.

## Privacy and safety

Do not publish private addresses, credentials, private medical or family information, unnecessary identifying information, private source identities without consent, or operational details whose primary value would be facilitating violence, sabotage, stalking, or abuse.

Opacity is not itself wrongdoing. Distinguish privacy that protects vulnerable people or sources from secrecy that shields concentrated power or accountability bypass. Transparency pressure should be proportional to power and public consequence.

## Copyright and provenance

Do not reproduce complete copyrighted articles or substantial protected works merely because they are relevant. Prefer links, citations, short necessary quotations, and original synthesis.

Third-party material must retain its provenance and applicable rights information.

## Corrections

Material errors should be corrected visibly. Preserve the correction trail and explain what changed when practical.

A consequential conclusion should retain a re-entry path: what evidence would change the assessment, what remains missing, and how a later reviewer can reconstruct the source lineage and reasoning.

A claim previously marked `CONFIRMED` may return to `PENDING` or become `DEBUNKED` if new evidence actually defeats the earlier basis. Status changes must retain lineage.

## Agent boundary

Automated or AI-assisted research may locate, compare, organize, calculate, cluster, map, and draft from sources. It must not independently publish accusations, erase uncertainty or material counterevidence, fabricate citations, infer private facts, expose protected identities, or convert threat classification into permission for punitive action.

Human review remains required for public claims that could materially affect identifiable people or organizations until a later governance process explicitly establishes a narrower safe authority.

Automation may support a public-record investigation by producing candidate entities, typed relations, chronologies, money/resource traces, source-lineage comparisons, missingness ledgers, harm vectors, provisional hierarchy views, and competing-model discriminators. These outputs remain review objects until promoted under the repository's explicit gates.
