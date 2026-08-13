# Reconciliation Checkpoint — 2026-08-13

```yaml
working_lineage: reconcile/harm-audit-canonicalization-2026-08-13
canonical_branch: main
old_main_sha: 32873817a81ade7e40527b301b69d10fda27fdb9
old_main_archive: archive/main-pre-harm-reconciliation-2026-08-13
promoted_reconciliation_sha: 519590fcc66df90999a2017d94a3c229085de5c1
promotion_status: COMPLETE
promotion_receipt: docs/CANONICAL_PROMOTION_RECEIPT_2026-08-13.md
known_semantic_old_main_gap: none
historical_recovery_complete: false
historical_recovery_continues_on_main: true
```

## Canonical state

`main` has been intentionally replaced by the reconciled harm-audit lineage.

The previous `main` remains recoverable at:

```text
archive/main-pre-harm-reconciliation-2026-08-13
```

The replacement is documented in:

- `docs/CANONICAL_MAIN_PROMOTION_PROTOCOL_v0_1.md`
- `docs/CANONICAL_PROMOTION_RECEIPT_2026-08-13.md`
- `docs/CANONICAL_RECONCILIATION_LEDGER_2026-08-13.md`

## Why historical recovery continues after promotion

Earlier in this reconciliation, promotion was held until the remaining historical branches were substantially mined. That lock is superseded.

The active rule is:

```text
make the strongest currently reconciled surface canonical
preserve the old canonical state by archive ref
preserve all historical recovery surfaces
record unresolved recovery debt
continue recovering into canonical main
```

Historical incompleteness is not, by itself, a reason to leave a methodologically weaker historical `main` in authority.

## Guard layer

Canonical recovery is now governed by:

- `agents/CANONICAL_RECONCILIATION_STEWARD_v0_1.md`
- `agents/PROVENANCE_CLAIM_INTEGRITY_AGENT_v0_1.md`
- `agents/LATTICE_RESURFACING_AGENT_v0_2.md`

The older `agents/LATTICE_RESURFACING_AGENT_v0_1.md` remains historical lineage; v0.2 supersedes it operationally.

## Canonical methodological direction

The active surface preserves:

- harm-first / negative-only subject selection;
- claim-specific falsification rather than mandatory charitable balancing;
- typed source, claim, relation, contribution, assessment, and missingness states;
- distinction among allegation, finding, causal contribution, enablement, intent, and realized harm;
- authority / gate / lever / implementation geometry;
- beneficiary gain / enforced loss / cost externalization geometry;
- donor / access / electoral-pressure geometry;
- blueprint / personnel / appointment / agency-authority routing;
- judicial selection / access / disclosure / recusal / ruling geometry;
- identity / ideology / organization / role / conduct / sponsorship separation;
- correction permeability and retaliation mapping;
- branch and provenance re-entry.

The wrapped pitchfork remains a useful projection, not the entire lattice.

## Remaining historical recovery debt

Promotion does **not** mean these are discarded.

### `reconcile-node-schema-v0-1`

Continue inspecting/recovering:

- federal/appointee people nodes after duplicate checks;
- actor-relation source bundle and report;
- Israel/Trump-appointee source bundle and report;
- Tennessee source bundles and reports;
- older physics-of-harm/interlocking-domination renditions for geometry not already promoted;
- remaining template deltas after compatibility review.

### `organic-lattice-sorting-2026-08-11`

Continue inspecting/recovering:

- Christianity and political-power workbench;
- Christian Trump coalition seed;
- trans-youth rhetoric/reality workbench and article;
- Zionism origins note;
- Sharia comparative and multilingual notes;
- humanitarian, left-solidarity, Sharia, supremacism, and Zionism scenes.

### historical seed / PCLocal branch tips

Inspect surviving unique artifacts only. Do not re-import already recovered history merely because branch ancestry differs.

## Recovery rule after promotion

Historical branches are evidence and recovery surfaces, not competing automatic authorities.

```text
recover -> compare -> type -> reconcile -> compile into main
```

Do not blind-merge a historical branch merely to make Git history look simpler.

## Tiny lock

> The canonical surface can move before historical recovery is finished, provided the old surface and unfinished paths remain recoverable.
