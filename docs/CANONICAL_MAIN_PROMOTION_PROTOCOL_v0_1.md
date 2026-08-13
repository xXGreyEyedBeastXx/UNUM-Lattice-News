# Canonical Main Promotion Protocol v0.1

Status: active canonicalization protocol
Date: 2026-08-13

## Purpose

This protocol defines how `main` may be replaced by a reconciled canonical surface without erasing recoverability, provenance, or the ability to return to an earlier repository state.

`main` is an active working canonical surface. It is not an authority that outranks better evidence, later correction, or a better-reconciled branch merely because it is named `main`.

## Canonical rule

```text
canonical != infallible
historical != authoritative
honest attempt != final truth
preserve provenance != preserve every old framing
correction != erasure
```

A prior canonical model may be superseded when it blocks a more accurate or more legible evidence structure. The old state must remain recoverable, but obsolete framing does not receive permanent authority merely because it once occupied `main`.

## Harm-audit rule

The repository may be one-sided in subject matter and still rigorous in evidence.

```text
unrelated good news != required balance
unrelated beneficial conduct != counterevidence
positive reputation != reduced causal responsibility
claim-specific falsification remains mandatory
```

Good or beneficial conduct belongs in a harm investigation only when it materially changes the scoped claim: attribution, causation, mechanism, chronology, scope, magnitude, necessity, identity, evidentiary reliability, or a proposed control/capture relation.

## Promotion sequence

Before replacing `main`:

1. Record the exact old `main` commit SHA.
2. Create a durable archive branch pointing to that exact SHA.
3. Verify the known `main`-only content has either been recovered or explicitly typed as intentionally excluded.
4. Ensure the reconciliation ledger and checkpoint exist in-repo.
5. Ensure canonical stewardship and provenance/claim-integrity agents exist in-repo.
6. Verify the reconciliation surface does not contain an accidental deletion wave.
7. Record unresolved historical recovery work as a re-entry queue rather than blocking canonical promotion indefinitely.
8. Move `main` to the reconciled canonical commit only after steps 1-7 are satisfied.
9. Write a promotion receipt recording old `main`, archive ref, promoted commit, and remaining recovery debt.

## Archive rule

The pre-promotion `main` state must remain addressable by a stable branch such as:

```text
archive/main-pre-harm-reconciliation-2026-08-13
```

The archive is evidence of repository history, not a competing current canonical authority.

Do not delete the old branch ecology merely because `main` has been replaced. Historical branches may still contain unrecovered source bundles, old reports, narrative workbenches, or useful failed models.

## Reconciliation rule after promotion

Once the reconciled surface becomes `main`, remaining historical branches are recovery sources.

Use:

```text
recover -> compare -> type -> reconcile -> compile
```

Do not use:

```text
old branch -> blind merge -> canonical
```

For each recovered object, preserve a disposition where useful:

- `RECOVERED`
- `RECONCILED`
- `SUPERSEDED`
- `DUPLICATE`
- `LAUNDERING_REMOVED`
- `SCHEMA_OBSOLETE`
- `HISTORICAL_ONLY`
- `EVIDENCE_FAILED`
- `OUT_OF_SCOPE`
- `PROVENANCE_MISSING`

## Main overwrite authority

A force update of `main` is permitted when all of the following are true:

- the repository owner has explicitly authorized replacement;
- the old tip is preserved by an archive ref;
- the promoted surface carries the reconciliation documentation and agent rules;
- known semantic gaps are documented;
- the action improves canonical coherence rather than hiding evidence.

The overwrite must never be used to conceal criticism, delete adverse evidence, remove correction history, or manufacture a cleaner-looking past.

## Post-promotion rule

After promotion:

- `main` becomes the canonical active recovery surface;
- the reconciliation branch may remain as a named historical/recovery lineage or be fast-forwarded to the promotion receipt;
- old branches remain available until their unique content has been typed and recovered or intentionally retired;
- later evidence may correct `main` again;
- no agent may resurrect mandatory positive balancing merely because older files used it.

## Minimal promotion receipt

```yaml
promotion:
  date: ""
  old_main_sha: ""
  archive_ref: ""
  promoted_from_ref: ""
  promoted_sha: ""
  post_promotion_receipt_sha: ""
  semantic_main_gap: ""
  unresolved_recovery_queue: []
  notes: []
```

## Tiny lock

> Preserve the old state as evidence. Do not preserve its mistakes as authority.
