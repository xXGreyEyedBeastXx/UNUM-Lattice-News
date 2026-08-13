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

The reconciliation target is not to preserve every historical wording. The target is to recover evidence, provenance, useful geometry, claims, nodes, source lineage, and accountability machinery while removing the older balancing behavior that interrupted harm investigations with unrelated positive material.

## Governing rule

```text
preserve evidence
preserve provenance
preserve claim-specific counterevidence
preserve uncertainty
preserve useful geometry

remove laundering
remove unrelated positive balancing
remove net-morality offsets
remove obsolete duplicated schema when a stronger representation exists
```

The audit is intentionally one-sided in subject matter: bad, ugly, harmful conduct, harmful machinery, concentrated power, corruption/capture hypotheses, coercion, exploitation, deprivation, civilian/ecological consequence, accountability bypass, and the actors who gain from or sustain those mechanisms.

The evidence standard remains two-sided. Evidence that directly weakens, narrows, falsifies, or reattributes a harm claim must remain.

## Canonical semantic locks

```text
unrelated beneficial conduct != counterevidence
beneficial act != offset for unrelated harm
beneficiary != morally good
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

- Rewrote `docs/NEWS_OPERATIONS_v0_2.md`.
- Removed the mandatory `charitable / legitimate-governance model` seat.
- Replaced it with a claim-specific counterevidence / falsification seat.
- Replaced `harm_benefit_map` with `harm_consequence_beneficiary_map`.
- Defined beneficiary as an evidenced gain from the mechanism under study, not positive moral credit.
- Removed positive-balance conclusions as a required endpoint.

### Schema recovery

Recovered from `reconcile-node-schema-v0-1`:

- `schemas/NODE_TYPE_REGISTRY_v0_1.yaml`
- `schemas/CLAIM_TEST_RECORD_v0_1.yaml`

Then extended the node registry with an `analysis_framework` family so methodological/operator nodes do not masquerade as worldly evidence nodes.

### Main-only recovery

Recovered from `main`:

- `briefings/review/2026-08-12_DAILY_TRUTH_BRIEFING_REVIEW.md`

This removes the only known substantive main-only gap that originally left the harm-audit branch one commit behind main.

### Geometry/operator recovery

Recovered and reconciled from `reconcile-node-schema-v0-1`:

- `nodes/harm-domination-protection-weighting.yaml`
  - retained legacy ID for relation compatibility;
  - migrated to `analysis_framework/causal_accountability_operator`;
  - removed life-serving positive-comparison machinery;
  - retained causal source -> propagation -> boundary -> harmed absorber -> feedback/accountability geometry.
- `nodes/institutions-gates-leaders-levers.yaml`
  - migrated to `analysis_framework/institutional_accountability_operator`;
  - preserves institutions, gates, officeholders, levers, beneficiaries, and loss-bearers as distinct seats.
- `nodes/interlocking-domination.yaml`
  - preserves multi-system domination without reducing all harm to one cause.
- `nodes/situated-relational-analysis.yaml`
  - preserves embodied/situated evidence without granting evidentiary exemption.
- `nodes/money-flow-benefit-enforced-loss.yaml`
  - migrated to `analysis_framework/resource_distribution_operator`;
  - renamed semantics internally from moral-sounding benefit to beneficiary gain;
  - preserves gain/loss, burden ratios, federal/state control attribution, cost externalization, and accountability return.

## Current recovered geometry

The recovered lattice now supports multiple simultaneous projections:

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

with parallel gain and feedback paths:

```text
MECHANISM -----------------------> BENEFICIARY GAIN
   |                               money / access / authority /
   |                               capacity / insulation / assets
   v
LOSS EXTERNALIZED DOWNWARD
   |
   v
AFFECTED PARTICIPANT

ACCOUNTABILITY / FEEDBACK
   ^
   |
   X  blocked, weakened, delayed, captured, or returned
   |
CAUSAL SOURCE
```

and an interlocking-structure projection:

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

Role: methodological and current investigative spine.

Disposition: base of reconciliation. Preserve and advance.

### `main`

Role: nominal canonical branch.

Known unique substantive item at reconciliation start: August 12 Daily Truth Briefing review.

Disposition: recovered into this branch. Do not let older main methodology override harm-audit corrections.

### `reconcile-node-schema-v0-1`

Role: large stranded ontology/evidence island.

Observed unique families include:

- people and institution nodes;
- Tennessee power network;
- Tennessee education funding/routing;
- Supreme Court network sweep;
- Trump/appointee sweep;
- money/power/harm reports;
- claim/source bundles;
- older schema/template changes.

Disposition: mine semantically, do not blind-merge.

### `organic-lattice-sorting-2026-08-11`

Role: ideology/conduct/identity and organic-growth research family.

Observed unique files include:

- dissent/reform/internal-correction diagnostic;
- identity/ideology/conduct classification;
- organic lattice growth model;
- AIPAC political/social/business capture case;
- Project 2025 / Heritage / Trump policy routing;
- Christianity and political power workbench;
- LGBTQIA2S/trans-youth rhetoric/reality workbench;
- Zionism, Sharia, supremacism, humanitarian, and left-solidarity scene/notes.

Disposition: recover classification and domination geometry first; review narrative/scenes individually for evidentiary and laundering seams.

### `actor-network-seed-2026-08-10`

Role: machine-readable actor/money network and focused investigations.

Observed unique files:

- `lattice/ACTOR_NETWORK_SEED_2026-08-10.yaml`
- `lattice/MONEY_INFLUENCE_ENRICHMENT_2026-08-10.yaml`
- Lavena Johnson / Pete Hegseth lead
- Guardian network audit

Disposition: high-priority recovery after schema compatibility review.

### `trust-threat-infrastructure-2026-08-11`

Role: threat/assessment structure.

Observed unique file:

- `schemas/assessment-record.schema.yaml`

Also contains an older `LATTICE_MODEL.md` modification.

Disposition: recover schema if compatible; do not overwrite newer lattice model blindly.

### `blue-green-left-accountability-2026-08-11`

Role: trust/threat assessment plus cross-spectrum accountability case.

Observed unique files:

- `docs/TRUST_THREAT_ASSESSMENT_FIELD_v0_1.md`
- `research/investigations/BLUE_GREEN_LEFT_ACCOUNTABILITY_SYSTEM_CASE_v0_1.md`

Disposition: inspect for symmetric-evidence machinery and any residual balancing requirement before recovery.

### `migration/library-intake-2026-08-11`

Role: file-library provenance/intake bridge.

Observed unique file:

- `intake/FILE_LIBRARY_POWER_ACCOUNTABILITY_REPORTS_2026-08-07_SOURCE_INDEX_v0_1.md`

Disposition: likely direct recovery after inspection.

### older seed/PCLocal branches

Role: historical operating-model, automation-roadmap, and story-node lineage.

Disposition: many commits were merged historically. Inspect only surviving unique branch-tip artifacts before retirement; do not assume branch-tip divergence means all commits are missing.

## Immediate queue

1. Inspect/recover `assessment-record.schema.yaml` and trust/threat field without restoring positive balancing.
2. Inspect/recover actor-network and money-influence machine-readable seeds.
3. Recover high-value old schema-branch nodes in clusters:
   - Tennessee power/governance;
   - federal/appointee network;
   - Supreme Court/judicial network;
   - HHS/EPA/autism/environment claim-testing cluster.
4. Recover corresponding source bundles before or with public-facing reports.
5. Review organic-lattice classification docs before narrative/workbench files.
6. Maintain a typed disposition for anything deliberately not recovered:
   - `SUPERSEDED`
   - `DUPLICATE`
   - `LAUNDERING_REMOVED`
   - `SCHEMA_OBSOLETE`
   - `EVIDENCE_FAILED`
   - `OUT_OF_SCOPE`
7. Only after the reconciliation surface is coherent should it be promoted to `main`.

## Promotion test

Do not call reconciliation complete until a fresh reviewer can recover:

- what branches existed;
- what unique material each contained;
- what was imported;
- what was rewritten;
- what was deliberately discarded and why;
- the evidence lineage for consequential claims;
- the current harm-audit rules;
- the wider lattice geometry beyond any single projection such as the wrapped pitchfork.
