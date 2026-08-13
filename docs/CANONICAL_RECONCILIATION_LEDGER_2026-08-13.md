# Canonical Reconciliation Ledger — 2026-08-13

```yaml
status: ACTIVE_RECONCILIATION
working_branch: reconcile/harm-audit-canonicalization-2026-08-13
methodological_base: harm-hierarchy-audit-v0-1
target: main
mode: semantic_integration_not_blind_merge
publication_authority: none
```

## Purpose

This ledger exists so branch recovery does not depend on chat context or memory.

The target is not to preserve every historical wording or literally merge every branch. The target is to recover evidence, provenance, useful geometry, claims, nodes, source lineage, and accountability machinery while removing the older balancing behavior that interrupted harm investigations with unrelated positive material.

## Governing rule

```text
preserve evidence
preserve provenance
preserve claim-specific counterevidence
preserve uncertainty
preserve useful geometry
preserve correction / re-entry

remove laundering
remove unrelated positive balancing
remove net-morality offsets
remove obsolete duplicated schema when a stronger representation exists
```

The audit is intentionally one-sided in subject matter: bad, ugly, harmful conduct, harmful machinery, concentrated power, corruption/capture hypotheses, coercion, exploitation, deprivation, civilian/ecological consequence, accountability bypass, and the actors who gain from or sustain those mechanisms.

The evidence standard remains adversarial in both directions. Evidence that directly weakens, narrows, falsifies, or reattributes a harm claim remains mandatory.

## Canonical semantic locks

```text
unrelated beneficial conduct != counterevidence
beneficial act != offset for unrelated harm
beneficiary != morally good
trust != moral goodness
public framing != moral credit
association != culpability
network != conspiracy
money relation != command
formal title != operational responsibility
delegation != absence of responsibility
institutional complexity != immunity
searched-not-found != debunked
human dignity != immunity from accountability
```

## Reconciliation completed in this branch

### Methodology

Rewrote `docs/NEWS_OPERATIONS_v0_2.md`:

- removed the mandatory `charitable / legitimate-governance model` seat;
- replaced it with a claim-specific counterevidence / falsification seat;
- replaced `harm_benefit_map` with `harm_consequence_beneficiary_map`;
- defined beneficiary as an evidenced gain from the mechanism under study, not positive moral credit;
- removed positive-balance conclusions as a required endpoint;
- retained direct falsification, necessity, attribution, scope, chronology, causal-mechanism, and reliability testing.

### Schema recovery and reconciliation

Recovered from `reconcile-node-schema-v0-1`:

- `schemas/NODE_TYPE_REGISTRY_v0_1.yaml`
- `schemas/CLAIM_TEST_RECORD_v0_1.yaml`

The node registry was extended with:

- `analysis_framework` for reusable causal/accountability operators that are maps rather than worldly evidence;
- `network` for typed political/institutional/influence/security/media meshes that do not imply common command, shared intent, conspiracy, or equal responsibility.

Recovered from `trust-threat-infrastructure-2026-08-11`:

- `schemas/assessment-record.schema.yaml`

Updated the already-present `docs/TRUST_THREAT_ASSESSMENT_FIELD_v0_1.md` so:

```text
trust = claim-local epistemic weight
trust != moral goodness
trust != harm offset
```

### Main-only recovery

Recovered from `main`:

- `briefings/review/2026-08-12_DAILY_TRUTH_BRIEFING_REVIEW.md`

This was the known substantive main-only file that originally left the harm-audit branch one commit behind main.

### Geometry/operator recovery

Recovered and reconciled from `reconcile-node-schema-v0-1`:

- `nodes/harm-domination-protection-weighting.yaml`
  - retained legacy ID for relation compatibility;
  - migrated to `analysis_framework/causal_accountability_operator`;
  - removed the older life-serving positive-comparison machinery;
  - retained causal source -> propagation -> boundary -> harmed absorber -> feedback/accountability geometry.
- `nodes/institutions-gates-leaders-levers.yaml`
  - migrated to `analysis_framework/institutional_accountability_operator`;
  - preserves institution, leader, gatekeeper, intermediary, beneficiary, and loss-bearer as distinct seats.
- `nodes/interlocking-domination.yaml`
  - preserves multi-system domination without reducing all harm to one master cause.
- `nodes/situated-relational-analysis.yaml`
  - preserves embodied/situated evidence without granting evidentiary exemption.
- `nodes/money-flow-benefit-enforced-loss.yaml`
  - migrated to `analysis_framework/resource_distribution_operator`;
  - beneficiary/gain semantics explicitly separated from moral benefit;
  - preserves gain/loss, burden ratios, federal/state control attribution, cost externalization, and accountability return.

### Actor / money-network recovery

Recovered as exact dated historical blobs from `actor-network-seed-2026-08-10`:

- `lattice/ACTOR_NETWORK_SEED_2026-08-10.yaml`
- `lattice/MONEY_INFLUENCE_ENRICHMENT_2026-08-10.yaml`

These remain seed surfaces, not verdicts. Their documented / supported / candidate / alleged / rumor / unknown distinctions are retained. Later harm-audit records outrank older shorthand classifications.

Recovered:

- `research/investigations/LAVENA_JOHNSON_PETE_HEGSETH_LEAD_v0_1.md`

This lead was preserved intact because it aggressively tests a severe allegation while explicitly refusing to promote hearsay, shared institutional nodes, other misconduct allegations, settlements, or absence of charges into proof of the LaVena Johnson allegation.

### Media-network recovery

Recovered and reconciled:

- `research/media/THE_GUARDIAN_NETWORK_AUDIT_v0_1.md`

Changes preserve claim-local counterevidence while removing reputation-credit semantics. Scott Trust structure can weaken a specific direct-owner-capture hypothesis without creating generalized moral credit. Reporting that contradicts a specific capture/normalization theory is retained only when it bears on that scoped theory; unrelated good journalism is not collected for balance.

### Tennessee power / money / education cluster

Recovered and reconciled:

- `nodes/tennessee-republican-power-network.yaml`
- `nodes/people/bill-lee.yaml`
- `nodes/people/marsha-blackburn.yaml`
- `nodes/tennessee-education-funding-system.yaml`
- `nodes/tennessee-education-freedom-scholarships.yaml`

The old Tennessee network required claimed ideals, positive counterexamples, and searches for actors displaying repair/restraint/protection. The recovered version keeps:

```text
seat -> gate -> lever -> action -> consequence
```

plus donor/vendor/access, beneficiary gain, enforced loss, burden ratios, and accountability feedback.

Dissent, recusal, correction, or repair is retained only when it materially narrows a specific attribution, mechanism, scope, magnitude, persistence, or shared-responsibility claim.

Bill Lee and Marsha Blackburn were migrated into `nodes/people/`. Their public rhetoric is retained as attributable framing to test against conduct, not as moral credit. Old unrelated positive-policy counterweights were removed.

### File Library provenance bridge

Recovered intact:

- `intake/FILE_LIBRARY_POWER_ACCOUNTABILITY_REPORTS_2026-08-07_SOURCE_INDEX_v0_1.md`

This preserves identities and high-level structures for three earlier power/accountability reports while explicitly retaining the raw-body hold: the complete original File Library bodies are not yet certified as byte-faithfully captured in GitHub.

## Duplicate / supersession decisions

### Donald Trump old node

Old source:

- `reconcile-node-schema-v0-1:nodes/donald-trump.yaml`

Current stronger source:

- `nodes/people/donald-trump.md`

Disposition:

```yaml
status: SUPERSEDED
restore_wholesale: false
extract_unique_evidence_or_source_anchors: true
reason:
  - newer node is explicitly a harm-audit historical index
  - newer node separates contribution records and authority seats
  - newer node explicitly rejects net-goodness biography and unrelated beneficial offsets
  - old node still asks how constructive and domination-oriented promises compare
```

Do not create two Donald Trump nodes. Older unique relations or source anchors may be migrated into the newer node or contribution records after evidence review.

## Current recovered geometry

The recovered lattice supports several simultaneous projections.

### Authority / implementation / harm

```text
CAUSAL CAPACITY
      |
      v
INSTITUTION / LEADER / GATEKEEPER
      |
      v
GATE / LEVER / RULE / BUDGET / CONTRACT
      |
      v
IMPLEMENTATION / ENFORCEMENT
      |
      v
HARM / LOSS / RIGHTS DEPRIVATION / RISK
      |
      v
AFFECTED PERSON / POPULATION / ECOLOGY
```

### Gain / externalization

```text
MECHANISM -----------------------> BENEFICIARY GAIN
   |                               money / access / authority /
   |                               capacity / insulation / assets
   v
LOSS EXTERNALIZED DOWNWARD
   |
   v
AFFECTED PARTICIPANT
```

### Feedback / accountability impedance

```text
ACCOUNTABILITY / FEEDBACK
   ^
   |
   X  blocked, weakened, delayed, captured, displaced, or returned
   |
CAUSAL SOURCE
```

### Interlocking domination

```text
class / race / colonial / patriarchal / nationalist /
religious-authority / ableist / extractive / bureaucratic structures
                         |
                         v
shared mechanisms: hierarchy / coercion / dehumanization /
institutional protection / downward harm transfer
```

Similarity alone does not establish common command, coordination, or equal harm.

### Actor / influence high-recall surface

```text
actor / institution / media / donor / state / military / legal node
        |
        +--> documented connector
        +--> supported connector
        +--> candidate connector
        +--> allegation / rumor / unknown

money / access / lobbying / ownership / contract / donor routing
        |
        v
candidate influence and dependency paths
        |
        v
case-specific causal testing before harm attribution
```

## Branch recovery map

### `harm-hierarchy-audit-v0-1`

Role: methodological and current investigative spine.

Disposition: base of reconciliation. Preserve and advance.

### `main`

Role: nominal canonical branch.

Known main-only briefing recovered. Do not allow older main methodology to override harm-audit corrections.

### `reconcile-node-schema-v0-1`

Role: large stranded ontology/evidence island.

Recovered so far:

- node type registry;
- claim-test schema;
- harm/accountability operator;
- institutions/gates/leaders/levers operator;
- interlocking domination;
- situated relational analysis;
- money/gain/enforced-loss operator;
- Tennessee Republican power network;
- Bill Lee;
- Marsha Blackburn;
- Tennessee education funding system;
- Tennessee Education Freedom Scholarships.

Still important:

- Supreme Court / Leonard Leo / judicial-network cluster;
- other federal/appointee people nodes and Trump-appointee sweep;
- HHS / EPA / RFK / autism / environmental claim-testing cluster;
- Tennessee reports and source bundles;
- source bundles for older federal/appointee work;
- older template changes after compatibility review.

Disposition: mine semantically, do not blind-merge.

### `organic-lattice-sorting-2026-08-11`

Role: ideology/conduct/identity and organic-growth research family.

High-priority structural files:

- `docs/IDENTITY_IDEOLOGY_CONDUCT_CLASSIFICATION_v0_1.md`
- `docs/DISSENT_REFORM_AND_INTERNAL_CORRECTION_DIAGNOSTIC_v0_1.md`
- `docs/ORGANIC_LATTICE_GROWTH_MODEL_v0_1.md`

Then investigate narrative/workbench families:

- AIPAC political/social/business capture;
- Project 2025 / Heritage / Trump policy routing;
- Christianity and political power;
- LGBTQIA2S/trans-youth rhetoric/reality;
- Zionism / Sharia / supremacism / humanitarian / left-solidarity scenes and notes.

Disposition: recover classification/domination geometry first; inspect narratives individually for evidence typing and laundering seams.

### `actor-network-seed-2026-08-10`

Recovered:

- actor-network seed;
- money-influence enrichment;
- LaVena Johnson / Pete Hegseth lead;
- Guardian network audit, reconciled.

Disposition: semantically close to exhausted; verify final compare before marking absorbed.

### `trust-threat-infrastructure-2026-08-11`

Recovered:

- assessment-record schema.

Its older `LATTICE_MODEL.md` did not overwrite the newer harm-audit model.

Disposition: semantically close to exhausted; verify final compare.

### `blue-green-left-accountability-2026-08-11`

Trust/threat document is already present and tightened against moral-credit semantics.

Still unique:

- `research/investigations/BLUE_GREEN_LEFT_ACCOUNTABILITY_SYSTEM_CASE_v0_1.md`

Disposition: inspect for useful cross-spectrum harm machinery without restoring positive balancing.

### `migration/library-intake-2026-08-11`

Recovered:

- `intake/FILE_LIBRARY_POWER_ACCOUNTABILITY_REPORTS_2026-08-07_SOURCE_INDEX_v0_1.md`

Disposition: likely semantically exhausted; verify final compare.

### older seed / PCLocal branches

Many commits were merged historically. Inspect only surviving branch-tip artifacts before retirement; divergence does not imply every historical commit is missing.

## Typed disposition vocabulary

Use one of these when material is deliberately not restored:

```text
SUPERSEDED
DUPLICATE
LAUNDERING_REMOVED
SCHEMA_OBSOLETE
EVIDENCE_FAILED
OUT_OF_SCOPE
HISTORICAL_ONLY
```

A discarded wording does not imply its underlying evidence was discarded.

## Immediate queue

1. Recover the Supreme Court / judicial network cluster with sources attached.
2. Check federal/appointee person-node duplicates before importing old nodes.
3. Recover the HHS / EPA / RFK / autism / environmental claim-testing cluster as a linked source/claim/node family.
4. Recover Tennessee source bundles before or alongside old public-facing reports.
5. Inspect the three organic-lattice structural docs before narrative/workbench files.
6. Inspect the blue/green accountability case for residual balancing and useful cross-spectrum harm mechanics.
7. Verify actor-network, trust-threat, and library-intake branches against the reconciliation branch and mark them absorbed where appropriate.
8. Compare the reconciliation branch to `main` for the eventual promotion surface.
9. Do not promote to `main` until coherence and provenance checks are complete.

## Promotion test

Do not call reconciliation complete until a fresh reviewer can recover:

- what branches existed;
- what unique material each contained;
- what was imported;
- what was rewritten;
- what was deliberately discarded and why;
- the evidence lineage for consequential claims;
- the current harm-audit rules;
- the wider lattice geometry beyond any single projection such as the wrapped pitchfork;
- duplicate/supersession decisions;
- a clear re-entry queue for anything still unresolved.
