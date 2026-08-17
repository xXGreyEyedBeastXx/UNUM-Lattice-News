# Main Landing and Branch Disposition Audit — 2026-08-17

Status: COMPLETED / ACCEPTED WORK LANDED / HISTORICAL EXPERIMENTS TYPED

## Purpose

Verify that completed and accepted work recovered during the 2026-08-17 retention audit is present on `main`, while distinguishing genuinely missing work from historical, superseded, or deliberately rejected branch experiments.

This audit follows:

```text
BRANCH EXISTS != MAIN IS MISSING WORK
HISTORICAL UNIQUE COMMIT != ACCEPTED CURRENT CONTENT
MERGED ONCE != STILL PRESENT AFTER A LATER MAIN REWRITE
SUPERSEDED-BUT-PRESERVE != SHOULD BE BLIND-MERGED
```

## Canonical posture

`main` is the active canonical working surface. Historical branches can remain recovery surfaces, but accepted current work should not depend on an unmerged branch.

## Recovery findings

### `actor-node-dossiers-v0-1`

Historical state:
- its 17-commit body had previously been merged in PR #46;
- later canonical rewriting/promotion caused its additive dossier files to disappear from the then-current `main` even though Git history still considered the branch merged.

Retention review found the work valuable and non-destructive:
- node dossier topology;
- correction-response primitive and schema;
- reproductive-autonomy living dossier;
- RFK Jr./autism/eugenics/cultural-capture addressing surfaces;
- bridge/stitch/correction directories.

The branch explicitly retained useful ideas from older Talos proposals while rejecting destructive replacement of the broad controversy membrane and obsolete feed coupling.

**Disposition:** `RECOVERED_TO_MAIN` through PR #48.

Verification after landing:
`main...actor-node-dossiers-v0-1 = ahead_by 0`; branch is fully contained by `main`.

### `investigation/wealth-grievance-routing-2026-08-16`

Historical state:
- 39 unique commits / roughly 120 changed paths had remained on the investigation branch during the audit;
- the work included the Harm Mesh recovery manifest, proof-dossier standard, verified-evidence retention rule, source bundles, claims, nodes, lattice/mesh surfaces, whole-circuit economic traces, WLM causal-retention work, entity-kinship material, and article-readiness packages.

Representative retention review confirmed that this was detailed evidence-preservation work rather than a compressed summary layer. In particular:
- `docs/HARM_MESH_THREAD_RECOVERY_2026-08-16.md` preserves operators, corrections, open edges, whole-circuit examples, historical-mechanism discoveries and re-entry state;
- `docs/HARM_AUDIT_PROOF_DOSSIER_STANDARD_v0_1.md` requires inspectable causal arrows, edge ledgers, source lineage, identity/ownership tracing, countercases and falsifiers;
- `docs/VERIFIED_EVIDENCE_RETENTION_AND_REENTRY_v0_1.md` explicitly prohibits verified mechanisms disappearing through summarization, safety filtering, renaming or repeated re-entry.

**Disposition:** `RECOVERED_TO_MAIN` through PR #49.

Verification after landing:
`main...investigation/wealth-grievance-routing-2026-08-16 = ahead_by 0`; branch is fully contained by `main`.

### `constitutional-safeguard-trajectory-2026-08-13`

Comparison after recovery:
- ahead of main: 0
- behind main: yes
- unique file delta: none

**Disposition:** `FULLY_CONTAINED / STALE HISTORICAL REF`.

### `extract-constraint-evidence-2026-08-13`

Comparison after recovery:
- ahead of main: 0
- behind main: yes
- unique file delta: none

**Disposition:** `FULLY_CONTAINED / STALE HISTORICAL REF`.

### `sync/mesh-enclosure-convergence-v0-1`

Comparison after recovery:
- ahead of main: 0
- behind main: yes
- unique file delta: none

**Disposition:** `FULLY_CONTAINED / STALE HISTORICAL REF`.

## Talos experimental branches

These branches remain ahead by one historical commit each, but the audit does **not** classify that as accepted work missing from `main`.

### `talos/bounty-33-1786431663652`

Unique delta:
- modifies `docs/CONTROVERSY_MEMBRANE_v0_1.md` with approximately 48 additions and 308 deletions.

Review posture:
- this is a destructive replacement/compression experiment;
- its useful reproductive-autonomy ideas (minor privacy, surveillance distinctions, factual-vs-normative separation, contested contraception handling) are already retained in the restored reproductive-autonomy dossier and node topology;
- the destructive replacement of the broad controversy membrane was explicitly rejected by the later reconciled architecture.

**Disposition:** `SUPERSEDED-BUT-PRESERVE / DO NOT MERGE`.

The historical branch is evidence of a tried model, not current canonical content.

### `talos/bounty-36-1786433951172`

Unique delta:
- adds a small `docs/CORRECTION_RESISTANCE_LEDGER_v0_1.md` template;
- performs a large rewrite of `scripts/collect_feed_candidates.py`.

Review posture:
- the ledger's useful concepts — actor lineage, correction attempts, response states, retaliation/repair, source-backed recurrence — are explicitly inherited and expanded in `schemas/CORRECTION_RESPONSE_STITCH_v0_1.yaml` and `docs/CORRECTION_RESPONSE_PRIMITIVE_v0_1.md`;
- the modern schema adds stronger evidentiary posture, counterevidence, partial update, apology/repair, disputed correction, insufficient evidence, nonclaims, reform/counterexamples, and relation-owned rather than actor-owned topology;
- the old feed-collector coupling was explicitly discarded as obsolete infrastructure.

**Disposition:** `SUPERSEDED-BUT-PRESERVE / DO NOT MERGE`.

## 2026-08-17 Israel / Nova retention repairs

The branch landing pass was also checked not to overwrite the current-thread repairs. Current `main` retains:

- `docs/EXTENSIBLE_EVIDENCE_GRAMMAR_v0_1.md` with propagated audience, kinship, accountability, command, protection-allocation, operational-narrative and foreknowledge types;
- `lattice/ISRAEL_SECURITY_KINSHIP_NARRATIVE_ACCOUNTABILITY_EXTENSION_2026-08-17.yaml` with corrected Smotrich typing and Netanyahu paired-surface propagation;
- `sources/source-oct7-nova-foreknowledge-border-allocation-2018-2026.yaml` for machine-readable source custody;
- `docs/RETENTION_AUDIT_ISRAEL_NOVA_THREAD_2026-08-17.md`;
- `research/investigations/OCT7_NOVA_CLUE_RETENTION_LEDGER_2018_2023.md`;
- `docs/CLUE_RETENTION_AND_NONCOMPRESSION_v0_1.md`.

## Final branch-state conclusion

Accepted/recovered substantive work is on `main`.

Branches still not fully equal to `main` fall into two categories:

1. **behind-only historical refs** — no unique work missing from `main`;
2. **Talos superseded experiments** — unique historical commits intentionally not merged because their useful invariants have been re-expressed in richer current surfaces while destructive/obsolete implementation choices were rejected.

Therefore:

```text
ACCEPTED CURRENT WORK DEPENDS ON UNMERGED BRANCH = NO
KNOWN MATERIAL RETENTION GAP AFTER AUDIT = NONE FOUND
TALOS HISTORICAL EXPERIMENTS = PRESERVED, NOT CANONICAL
MAIN = CURRENT RE-ENTRY SURFACE
```

## Cleanup note

The connector available during this audit does not expose branch deletion as an action. Historical branch refs therefore remain visible. Their existence should not be interpreted as unfinished landing work; the dispositions above control until a branch-cleanup-capable surface removes stale refs.
