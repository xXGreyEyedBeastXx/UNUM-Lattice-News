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

The target is not to preserve every historical wording or literally merge every branch. The target is to recover evidence, provenance, useful geometry, claims, nodes, source lineage, and accountability machinery while removing older balancing behavior that interrupted harm investigations with unrelated positive material.

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

The audit is intentionally one-sided in subject matter: bad, ugly, harmful conduct, harmful machinery, concentrated power, corruption/capture hypotheses, coercion, exploitation, deprivation, civilian/ecological consequence, accountability bypass, and actors who gain from or sustain those mechanisms.

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
statehood != innocence
designation != proof
identity != ideology != conduct
human dignity != immunity from accountability
```

## Reconciliation completed in this branch

### 1. Methodology

Rewrote `docs/NEWS_OPERATIONS_v0_2.md`:

- removed the mandatory `charitable / legitimate-governance model` seat;
- replaced it with a claim-specific counterevidence / falsification seat;
- replaced `harm_benefit_map` with `harm_consequence_beneficiary_map`;
- defined beneficiary as an evidenced gain from the mechanism under study, not positive moral credit;
- removed positive-balance conclusions as a required endpoint;
- retained direct falsification, necessity, attribution, scope, chronology, causal-mechanism, and reliability testing.

### 2. Schema recovery and reconciliation

Recovered from `reconcile-node-schema-v0-1`:

- `schemas/NODE_TYPE_REGISTRY_v0_1.yaml`
- `schemas/CLAIM_TEST_RECORD_v0_1.yaml`

The node registry was extended with:

- `analysis_framework` for reusable causal/accountability operators that are maps rather than worldly evidence;
- `network` for typed political/institutional/influence/security/media meshes that do not imply common command, shared intent, conspiracy, or equal responsibility.

Recovered from `trust-threat-infrastructure-2026-08-11`:

- `schemas/assessment-record.schema.yaml`

Updated `docs/TRUST_THREAT_ASSESSMENT_FIELD_v0_1.md` so:

```text
trust = claim-local epistemic weight
trust != moral goodness
trust != harm offset
```

### 3. Main-only recovery

Recovered from `main`:

- `briefings/review/2026-08-12_DAILY_TRUTH_BRIEFING_REVIEW.md`

This was the known substantive main-only file that originally left the harm-audit branch one commit behind main.

### 4. Geometry/operator recovery

Recovered and reconciled from `reconcile-node-schema-v0-1`:

- `nodes/harm-domination-protection-weighting.yaml`
  - retained legacy ID for relation compatibility;
  - migrated to `analysis_framework/causal_accountability_operator`;
  - removed older life-serving positive-comparison machinery;
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

### 5. Actor / money-network recovery

Recovered as exact dated historical blobs from `actor-network-seed-2026-08-10`:

- `lattice/ACTOR_NETWORK_SEED_2026-08-10.yaml`
- `lattice/MONEY_INFLUENCE_ENRICHMENT_2026-08-10.yaml`
- `research/investigations/LAVENA_JOHNSON_PETE_HEGSETH_LEAD_v0_1.md`

Recovered and reconciled:

- `research/media/THE_GUARDIAN_NETWORK_AUDIT_v0_1.md`

The Guardian audit now treats ownership structure, correction behavior, or reporting that cuts against a capture hypothesis as claim-local evidence, not reputation credit.

### 6. Tennessee power / money / education cluster

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

### 7. File Library provenance bridge

Recovered intact:

- `intake/FILE_LIBRARY_POWER_ACCOUNTABILITY_REPORTS_2026-08-07_SOURCE_INDEX_v0_1.md`

This preserves identities and high-level structures for three earlier power/accountability reports while explicitly retaining the raw-body hold: the complete original File Library bodies are not yet certified as byte-faithfully captured in GitHub.

### 8. Judicial / Supreme Court network cluster

Recovered and reconciled:

- `sources/source-supreme-court-ethics-network.yaml`
- `nodes/institutions/us-supreme-court.yaml`
- `nodes/people/leonard-leo.yaml`
- `reports/2026-08-09-supreme-court-network-first-sweep.yaml`

The judicial geometry is now explicit:

```text
selection / confirmation pipeline
 -> donor / ideological / access network
 -> appointment / life-tenure authority
 -> disclosure / recusal / ethics boundary
 -> ruling / judicial gate
 -> constraint removed, preserved, or redirected
```

Safeguard:

```text
gift / travel / access / ideology != purchased vote
no proven quid pro quo != irrelevant financial/access network
```

Provenance debt was preserved instead of hidden:

- legacy source ID `source-supreme-court-current-members` was referenced by the old material but not recovered by filename/search;
- marked `SEARCHED_NOT_FOUND` rather than silently replaced.

### 9. HHS / EPA / RFK / autism / environmental claim-testing cluster

Recovered exact evidence/story records:

- `sources/source-cdc-autism-data-2025.yaml`
- `sources/source-nimh-autism-overview.yaml`
- `sources/source-reuters-2026-08-06-autism-vaccine-order.yaml`
- `stories/2025-04-15-cdc-autism-prevalence-update.yaml`
- `stories/2026-08-06-autism-vaccine-policy-watch.yaml`

Recovered/reconciled nodes:

- `nodes/autism.yaml`
- `nodes/environmental-pollution-exposure.yaml`
- `nodes/people/robert-f-kennedy-jr.yaml`
- `nodes/institutions/us-department-health-human-services.yaml`
- `nodes/institutions/us-environmental-protection-agency.yaml`

Recovered/reconciled claim test:

- `claims/rfk-hhs-autism-environmental-cause.yaml`

Key distinctions:

```text
identified prevalence != biological incidence
association != general causation
government investigation != evidentiary support
pollution neurodevelopmental harm != proof pollution generally causes autism
autism condition != actor / accusation / single acquired injury
```

The inherited broad environmental-autism causal assessment is retained as `unsupported` at the restored evidence level with `PARTIAL_SOURCE_RELINK` rather than treated as fully sourced.

Missing inherited source IDs are explicitly typed in the relevant nodes/claim, including HHS/EPA/NIEHS/PolitiFact records that were referenced historically but are not currently recovered.

Old HHS language describing `legitimate care and research goals` as a balancing frame was removed. EPA retained-protection material now appears only when it narrows a specific deregulation claim, not as general moral credit.

### 10. Organic-lattice structural recovery

Recovered intact because they already strengthen harm-audit discrimination:

- `docs/IDENTITY_IDEOLOGY_CONDUCT_CLASSIFICATION_v0_1.md`
- `docs/DISSENT_REFORM_AND_INTERNAL_CORRECTION_DIAGNOSTIC_v0_1.md`

Recovered/reconciled:

- `docs/ORGANIC_LATTICE_GROWTH_MODEL_v0_1.md`

The identity/conduct classifier preserves:

```text
IDENTITY != IDEOLOGY != ORGANIZATION != ROLE != TACTIC != SPONSORSHIP != EVIDENTIARY STATUS
```

This blocks both collective guilt and state/institutional laundering.

The dissent diagnostic adds **correction permeability**:

```text
accurate criticism
 -> can it cross the institutional boundary?
 -> investigation or suppression?
 -> leadership accountability or insulation?
 -> correction or harm persistence?
```

The organic growth model now uses `beneficiary gain` rather than moral-sounding benefit and promotes recurring harm mechanisms, gates, loss paths, shared-harm objects, and accountability failures into reusable structure.

### 11. Organic AIPAC and Project 2025 investigations

Recovered/reconciled:

- `research/investigations/AIPAC_POLITICAL_SOCIAL_BUSINESS_CAPTURE_SYSTEM_CASE_v0_1.md`
- `research/investigations/PROJECT_2025_HERITAGE_TRUMP_POLICY_ROUTING_v0_1.md`

AIPAC investigation now uses:

```text
money / independent spending / lobbying / donor network
 -> access / electoral pressure
 -> legislative or institutional gate
 -> policy / speech constraint / military-policy pathway
 -> harmed population or democratic consequence
```

with beneficiary gain, failed influence, independent causal drivers, and claim-specific falsifiers. Generic positive counterexamples are not accumulated.

Project 2025 investigation preserves:

```text
policy blueprint
 + personnel recruitment
 + training
 + early-action playbook
 -> appointment
 -> agency authority
 -> implementation
```

while distinguishing direct shaping, shared coalition origin, personnel circulation, and superficial overlap.

### 12. Blue / Green / Left accountability case

Recovered/reconciled:

- `research/investigations/BLUE_GREEN_LEFT_ACCOUNTABILITY_SYSTEM_CASE_v0_1.md`

The legacy file contained an explicit `Mandatory positive / exculpatory lane` requiring general beneficial conduct such as healthcare expansion, labor protections, environmental regulation, anti-monopoly policy, and other positive achievements.

That section was removed and replaced with:

```text
claim-specific exculpatory / falsification lane
```

Only evidence that materially weakens a specific capture/harm claim remains, for example:

- resistance to the allegedly controlling donor network;
- member governance overriding executive/funder preference;
- grantee action against funder preference;
- independent causal origin;
- repeated failure of an alleged influence mechanism;
- documented retaliation risk explaining anonymity.

Generic good policy is out of scope and does not offset harm.

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

Do not create two Donald Trump nodes.

## Current recovered geometry

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

### Correction permeability

```text
CRITICISM / WHISTLEBLOWING / DISSENT
      |
      v
INSTITUTIONAL BOUNDARY
      |
      +--> evidence review -> correction -> repair / changed policy
      |
      X--> stigma / retaliation / expulsion / criminalization
                         |
                         v
               leadership insulation
                         |
                         v
                   harm persistence
```

### Electoral / donor influence

```text
MONEY / DONOR NETWORK / OUTSIDE SPENDING
      |
      v
ACCESS / CANDIDATE PRESSURE / AGENDA GATE
      |
      v
POLICY / LEGISLATION / INSTITUTIONAL SIGNAL
      |
      v
HARM / SPEECH CONSTRAINT / MILITARY OR MATERIAL EFFECT
```

### Ideological implementation infrastructure

```text
BLUEPRINT
 + PERSONNEL DATABASE
 + TRAINING
 + EARLY-ACTION PLAN
      |
      v
APPOINTMENT
      |
      v
AGENCY AUTHORITY
      |
      v
IMPLEMENTATION
```

### Judicial gate

```text
SELECTION NETWORK
 -> APPOINTMENT / TENURE
 -> DONOR / ACCESS / DISCLOSURE / RECUSAL FIELD
 -> JUDICIAL DECISION
 -> CONSTRAINT ON OR EXPANSION OF OTHER POWER
```

### Identity / conduct discriminator

```text
IDENTITY
  != IDEOLOGY
  != ORGANIZATION
  != ROLE
  != TACTIC / CONDUCT
  != SPONSORSHIP / AUTHORITY
  != EVIDENTIARY STATUS
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

## Branch recovery map

### `harm-hierarchy-audit-v0-1`
Role: methodological/current investigative spine.  
Disposition: base of reconciliation; preserve and advance.

### `main`
Role: nominal canonical branch.  
Disposition: known main-only briefing recovered; do not allow older main methodology to override harm-audit corrections.

### `reconcile-node-schema-v0-1`
Role: large stranded ontology/evidence island.

Recovered major families:

- schemas and operators;
- Tennessee power/education core;
- Supreme Court / Leonard Leo cluster;
- HHS / EPA / RFK / autism / environmental claim-test cluster.

Still important:

- other federal/appointee person nodes and Trump-appointee sweep;
- Tennessee reports and source bundles;
- source-bundle actor/relation sweep;
- Israel/Trump appointee source bundle/report;
- physics-of-harm / interlocking-domination historical reports after redundancy review;
- old template changes after compatibility review.

Disposition: continue semantic mining, not blind merge.

### `organic-lattice-sorting-2026-08-11`
Recovered:

- three structural docs;
- AIPAC capture case;
- Project 2025 routing case.

Still important:

- Christianity and political-power workbench;
- LGBTQIA2S/trans-youth rhetoric/reality workbench and article;
- Zionism origins note;
- Sharia comparative/multilingual notes;
- humanitarian, left-solidarity, Sharia, supremacism, Zionism scenes;
- Christian Trump coalition seed.

Disposition: inspect individually. Structural core is recovered; narrative/religion/identity files require careful separation of source evidence, ideology, conduct, collective guilt, and harm mechanisms.

### `actor-network-seed-2026-08-10`
All four unique semantic artifacts are recovered or reconciled:

- actor-network seed: exact historical blob;
- money-influence enrichment: exact historical blob;
- LaVena/Hegseth lead: exact historical blob;
- Guardian audit: reconciled.

Disposition: `SEMANTICALLY_ABSORBED_PENDING_BRANCH_RETIREMENT_REVIEW`.

### `trust-threat-infrastructure-2026-08-11`
Recovered assessment schema. Older lattice-model change is superseded by newer harm-audit model.

Disposition: `SEMANTICALLY_ABSORBED_PENDING_BRANCH_RETIREMENT_REVIEW`.

### `blue-green-left-accountability-2026-08-11`
Trust/threat field already present and tightened. Remaining system case recovered and its mandatory positive lane removed.

Disposition: `SEMANTICALLY_ABSORBED_PENDING_BRANCH_RETIREMENT_REVIEW`.

### `migration/library-intake-2026-08-11`
Sole unique source index recovered intact.

Disposition: `SEMANTICALLY_ABSORBED_PENDING_BRANCH_RETIREMENT_REVIEW`.

### older seed / PCLocal branches
Many commits were merged historically. Inspect surviving branch-tip artifacts only; divergence does not imply every historical commit is missing.

## Typed disposition vocabulary

```text
SUPERSEDED
DUPLICATE
LAUNDERING_REMOVED
SCHEMA_OBSOLETE
EVIDENCE_FAILED
OUT_OF_SCOPE
HISTORICAL_ONLY
SEMANTICALLY_ABSORBED_PENDING_BRANCH_RETIREMENT_REVIEW
```

A discarded wording does not imply its underlying evidence was discarded.

## Immediate queue

1. Inspect federal/appointee duplicates before importing old people nodes: Alina Habba, Netanyahu, Jared Kushner, Lindsey Graham, Marco Rubio, Mike Huckabee, Pete Hegseth, Stephen Miller, Steve Witkoff.
2. Recover `sources/source-bundle-2026-08-09-actor-relation-sweep.yaml` before the actor-relation report.
3. Recover/reconcile `sources/source-bundle-2026-08-09-israel-trump-appointee-sweep.yaml` and corresponding report.
4. Recover Tennessee source bundles before old public-facing Tennessee reports.
5. Inspect old `physics-of-harm` and `interlocking-domination` reports for geometry not already promoted into operators.
6. Continue organic branch through Christianity / Christian Trump coalition first, then Zionism/Sharia/supremacism scenes with identity/conduct classifier enforced.
7. Inspect older seed/PCLocal branch-tip survivors.
8. Compare the reconciliation branch to `main` for the eventual promotion surface.
9. Do not promote to `main` until coherence, duplicate, provenance, and laundering checks are complete.

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
- typed provenance debt;
- a clear re-entry queue for anything still unresolved.
