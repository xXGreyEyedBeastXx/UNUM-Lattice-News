# Reconciliation Checkpoint — 2026-08-13

```yaml
working_branch: reconcile/harm-audit-canonicalization-2026-08-13
old_main_sha: 32873817a81ade7e40527b301b69d10fda27fdb9
old_main_archive: archive/main-pre-harm-reconciliation-2026-08-13
status: PROMOTION_AUTHORIZED_AFTER_GUARDS
known_semantic_main_gap: none
historical_recovery_complete: false
historical_recovery_may_continue_after_promotion: true
```

## Changed promotion rule

Earlier in this reconciliation, promotion was held until the remaining historical branches were substantially mined.

That lock is superseded.

The canonical objective is now:

```text
make the strongest currently reconciled surface canonical
preserve the old canonical state by archive ref
preserve all historical recovery surfaces
record unresolved recovery debt
continue recovering into canonical main
```

Historical incompleteness is not, by itself, a reason to keep an older and methodologically weaker `main` in authority.

## Old `main` preservation

The pre-promotion `main` tip is:

```text
32873817a81ade7e40527b301b69d10fda27fdb9
```

It is preserved at:

```text
archive/main-pre-harm-reconciliation-2026-08-13
```

The old state remains recoverable for audit, comparison, or rollback. It is historical evidence, not the intended current canonical methodology.

The August 12 Daily Truth Briefing review that existed uniquely in the old `main` history has already been recovered onto the reconciliation surface, so the earlier one-commit-behind state represented Git ancestry rather than a known semantic content hole.

## Guard layer now present

Canonical promotion requires and now has:

- `docs/CANONICAL_MAIN_PROMOTION_PROTOCOL_v0_1.md`
- `docs/CANONICAL_RECONCILIATION_LEDGER_2026-08-13.md`
- this checkpoint
- `agents/CANONICAL_RECONCILIATION_STEWARD_v0_1.md`
- `agents/PROVENANCE_CLAIM_INTEGRITY_AGENT_v0_1.md`
- `agents/LATTICE_RESURFACING_AGENT_v0_2.md`

The README now links these canonical recovery surfaces and uses `harm/consequence/beneficiary` rather than the obsolete `harm/benefit` entrypoint wording.

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

The lattice is therefore not a single wrapped pitchfork. That shape remains one projection inside a larger multiplex accountability geometry.

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

## Promotion conditions

The reconciliation branch may replace `main` when:

1. the old `main` archive ref exists and resolves to the recorded SHA;
2. the guard documents and agents above exist;
3. a fresh comparison shows no accidental deletion wave or unexpected missing old-main semantic content;
4. the promoted commit is recorded in a post-promotion receipt.

Remaining historical branch debt is a re-entry queue, not a promotion veto.

## After promotion

`main` becomes the active canonical recovery surface.

Historical branches remain evidence and recovery surfaces until reconciled or explicitly retired. Agents should continue recovering evidence and geometry into `main` while preventing obsolete positive-balancing methodology from returning.

## Tiny lock

> Archive the old authority. Promote the better map. Keep recovering what the better map has not yet absorbed.
