# Verified Evidence Retention and Re-entry v0.1

**Status:** active repository-wide evidence-retention rule  
**Purpose:** prevent already-verified causal mechanisms from disappearing through summarization, safety filtering, renaming, or repeated re-entry.

## Core invariant

```text
verified relation != disposable summary detail
```

Once a relation, mechanism, objective, source lineage, or transformation has been verified and recorded, later work must **inherit it by default**.

Do not silently downgrade:

```text
verified mechanism -> generic label
verified transformation -> endpoint-only summary
verified source lineage -> "needs rechecking"
verified movement objective -> vague ideological category
```

Re-verification is required only when there is a concrete reason to reopen the edge.

## Re-open conditions

A verified edge may be rechecked when at least one of these applies:

- new contradictory evidence appears;
- source authenticity or integrity is challenged with specific evidence;
- the claim has materially changed in time, jurisdiction, actor, version, or scope;
- exact quotation is needed and the preserved source must be checked for wording;
- a prior record explicitly marked the edge as provisional, incomplete, or citation-lineage uncertain;
- a correction or superseding source changes the evidentiary state;
- the requested publication burden is higher than the prior verification burden and the missing increment is specifically named.

Absent one of those triggers, **reuse the verified record rather than restarting the investigation.**

## Recognition before re-verification

Before asking the user to resend evidence or before launching a new verification pass:

1. search the current repo;
2. search linked/specialist repos;
3. resolve historical names, source bundles, aliases, recovery files, and prior branch surfaces;
4. inspect the recorded claim posture and limitations;
5. only reopen the source if a re-open condition is actually present.

The correct distinction is:

```text
not yet found in current view != not previously verified
```

## Safety-filter preservation rule

Safety constraints may justify omitting operational, tactical, evasion, targeting, or execution detail.

They do **not** justify deleting the existence, target, purpose, role, or causal function of an already-verified mechanism.

Example:

```text
operational recruitment instructions -> may be excluded
existence of recruitment machinery -> must remain
recruitment target -> must remain when causally material
recruitment purpose -> must remain
recruitment's place in the transformation chain -> must remain
```

This applies equally to:
- recruitment;
- normalization;
- financing;
- coordination;
- propaganda;
- lobbying/influence;
- surveillance;
- coercion;
- evasion as an investigated phenomenon;
- redress suppression;
- ownership/control;
- material gain.

## Compression failure test

Before replacing a detailed verified record with a shorter description, ask:

> If I remove this relation, can a reader still reconstruct how the starting condition becomes the observed endpoint?

If no, the relation is not expendable summary detail.

Preserve especially:
- recruitment funnels;
- normalization/optics shifts;
- intermediary gatekeepers;
- ownership reseating;
- material carriers;
- coercive constraint envelopes;
- redress paths;
- version-to-version goal continuity;
- source lineage.

## Version continuity rule

When later documents change language or optics, compare what changed **and what survived**.

Do not treat softer wording as evidence that an earlier objective disappeared when later primary records preserve the objective.

Use:

```text
version A mechanism/objective
-> transformation in presentation or implementation
-> version B surviving invariant
```

This is especially important for movements, corporations, agencies, laws, brands, and political programs that rename or reframe themselves.

## User-resupplied evidence rule

When the user provides evidence that is already represented in the repository:

- use it to strengthen or correct the stored lineage;
- do not behave as though the claim is being encountered for the first time;
- identify the prior record and the incremental information supplied;
- do not make the user repeatedly prove the same verified proposition.

## Publication rule

Publication review may demand stronger sourcing than internal verification, but the burden must be incremental and explicit.

Good:

> The mechanism is already verified internally; for publication we still need the preserved PDF for exact quotations on pages X-Y.

Bad:

> We need to verify whether the mechanism exists again.

## WLM failure-case lock

The White Lives Matter April-2021 initiative is the originating failure case for this rule.

Already-verified records established:
- explicit 99%+ White demographic objective;
- White Nationalist ideological endpoint;
- deliberate mainstream-family normalization strategy;
- approachable public activism as a doorway toward that worldview;
- recruitment/activist-conversion machinery;
- decentralized recurring participation;
- optics discipline separating public-facing presentation from more explicit ideological material.

The error was to preserve the ideological endpoint while compressing away the recruitment/normalization transformation because operational recruitment instructions were not reproduced.

That compression is prohibited going forward.

## Tiny locks

> **Safety may redact tactics; it may not erase causal structure.**

> **Verified edges persist until evidence changes them.**

> **Recognition before re-verification.**
