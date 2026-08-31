# UNUM Lattice News — Public / Backend Architecture v0.2

**Status:** ACTIVE MIGRATION TARGET  
**Updated:** 2026-08-30

## Purpose

UNUM Lattice News is consolidating from a family of narrowly separated Lattice repositories into **one Lattice system with two active surfaces**:

```text
UNUM-Lattice-News-Backend   # private working/evidence surface
        |
        | reviewed public-safe promotion
        v
UNUM-Lattice-News           # public durable evidence/reporting surface
```

This supersedes the earlier one-public-repository target. The correction preserves the same consolidation goal while giving private, sensitive, provisional, and operational material a real home instead of forcing it through a public membrane.

The consolidation remains semantic, not a blind file move.

```text
recover donor function
-> identify lifecycle and authority
-> adopt / adapt / donate
-> preserve provenance and return path
-> verify privacy / evidence state / links
-> retire duplicate active authority only when replacement is live
```

## Two surfaces, one Lattice identity

The public and backend repositories are not competing truth authorities.

```text
BACKEND
= working custody
= ingestion
= source survival
= private/sensitive evidence
= drafts and queues
= unresolved reviews
= promotion machinery
= operational agents/workflows
= migration/reconciliation work

PUBLIC
= reviewed public-safe evidence
= durable public events and claims
= public causal maps / meshes
= scoped confirmed-harm states
= corrections
= public briefings and inspectable analysis
```

A backend object does not become public merely because it exists. A public projection does not become independent corroboration merely because it crossed repositories.

## Prime distinction

Repository boundaries and routing lenses do different jobs.

```text
Lattice Public / Backend split
  = visibility + lifecycle boundary

external specialist repository
  = genuinely distinct domain study authority

internal Lattice lens
  = traversal/routing grammar across either Lattice surface
```

Geopolitics, capital/power, humanitarian-environmental analysis, trafficking, and policy-mechanism review therefore remain **Lattice routing lenses**, not separate truth systems.

Medical, Earth/Environmental Ecology, Governance, Human Relations, Chemistry, Engineering, Translation, Extremism Watch, Laundering Map, Hierarchy/Supremacy Studies, and other wider UNUM repositories remain external specialist owners when the substantive study has its own lifecycle.

`UNUM-Research` remains the ecology-wide external retrieval, request identity, provenance, routing, and re-entry head.

## Target backend architecture

```text
UNUM-Lattice-News-Backend/
│
├── README.md
├── intake/
│   ├── candidates/
│   ├── source-review/
│   ├── claim-extraction/
│   ├── routing/
│   └── rejected-deferred/
│
├── evidence/
│   └── sources/
│       └── <source-id>/
│           ├── SOURCE.yaml
│           └── items/<year>/<item-id>/...
│
├── work/
│   ├── investigations/
│   ├── casework/
│   ├── reviews/
│   ├── maps/
│   └── chronologies/
│
├── promotion/
│   ├── public-review/
│   ├── harm-review/
│   └── packets/
│
├── routes/                 # internal lenses + specialist crossings
├── operations/
├── agents/
├── workflows/
├── schemas/
├── registries/
├── migration/
└── archive/
```

Backend may contain private or sensitivity-controlled material only within the actual authorization/privacy rules of that repository. "Private repository" does not erase the need for dignity, source protection, lawful custody, or minimization.

## Target public architecture

```text
UNUM-Lattice-News/
│
├── README.md
├── EDITORIAL_STANDARD.md
├── CORRECTIONS.md
│
├── stories/                # reviewed public events/state transitions
├── claims/                 # reviewed bounded claims
├── nodes/                  # public-safe addressable mesh seats
├── lattice/                # durable public meshes/causal ecologies
├── harm/
│   └── confirmed/          # scoped public high-confidence harm states
├── maps/                   # reviewed reusable public maps
├── reviews/                # reviewed public analytical returns
├── briefings/              # dated synthesis
├── contributions/          # bounded public contributions
├── evidence/               # reviewed public source metadata / lineage projection
├── schemas/
├── registries/
├── docs/
└── archive/                # only when historical public state matters
```

The public repository should **not** become the raw intake workbench.

## Public/backend promotion membrane

Every crossing from Backend to Public should preserve:

```text
object identity
source lineage
exact claim / event / relation / harm edge
scope
relevant clocks
internal lenses used
external specialist returns used
uncertainty / typed missingness
privacy / publication-safety state
evidence effects / competing models when material
what changed during review
backend return pointer
public destination identity
```

Promotion is object- and claim-specific.

```text
backend source record -> public source metadata projection
backend candidate -> may never promote
backend review -> may narrow / merge / reject
backend confirmed-harm review -> public CONFIRMED_HARM state only if earned
```

## Internal routing lenses

A Lattice object may carry multiple lenses on either surface:

```text
GEOPOLITICS
CAPITAL_POWER
HUMANITARIAN_ENVIRONMENTAL
TRAFFICKING
POLICY_MECHANISM
```

A lens selects questions and discriminators; it does not create an independent evidence lineage or establish the conclusion named by the lens.

Examples:

```text
war + water + procurement
-> GEOPOLITICS + HUMANITARIAN_ENVIRONMENTAL + CAPITAL_POWER

remote extractive workforce + coercive recruitment + jurisdictional gaps
-> TRAFFICKING + CAPITAL_POWER + POLICY_MECHANISM
```

## Adopt, adapt, donate

Every donor object should be classified by what lifecycle it actually needs:

```text
ADOPT_BACKEND
ADOPT_PUBLIC
ADAPT_AND_MERGE_BACKEND
ADAPT_AND_MERGE_PUBLIC
PROMOTE_BACKEND_TO_PUBLIC_AFTER_REVIEW
DONATE_TO_EXTERNAL_SPECIALIST
KEEP_AS_PROVENANCE_ONLY
KEEP_PRIVATE_AND_POINT
SUPERSEDED_AFTER_RECOVERY
REJECT_AS_DUPLICATE_OR_OBSOLETE
NEEDS_REVIEW
```

### Adopt

Use when the function genuinely belongs to the Lattice system.

Examples:
- source survival -> Backend;
- public event ledger -> Public;
- harm promotion gate -> Backend;
- confirmed scoped harm state -> Public.

### Adapt

Use when useful machinery exists but its old repository-specific assumptions should be removed.

Examples:
- Geopolitics repository queue -> common Backend route queue with `GEOPOLITICS` lens;
- Capital-and-Power maps -> shared map grammar with multi-lens metadata;
- Real-Bad-Policy review -> policy-mechanism review without verdict-bearing repository identity.

### Donate

Use when an object has developed a lifecycle that belongs to a genuine specialist repository.

Examples:
- clinical mechanism -> Medical;
- ecological mechanism -> Earth/Environmental Ecology;
- authority/procedure/enforcement study -> Governance;
- trafficking-specific relational coercion may route to Human Relations when the study becomes fundamentally relational rather than news-specific;
- reusable generic tooling -> Tools/Utilities.

Donation preserves the Lattice return edge; it does not erase where the question came from.

## Former satellite disposition

The existing Lattice satellites remain donor/recovery surfaces until Backend exists and each unique function/object has a live destination:

```text
UNUM-Lattice-News-Intake
UNUM-Lattice-News-Proven-Harm
UNUM-Lattice-News-Humanitarian-Environmentalism
UNUM-Lattice-News-Real-Bad-Policy
UNUM-Lattice-News-Geopolitics
UNUM-Lattice-News-Capital-and-Power
UNUM-News-Lattice-Trafficking
```

Do not retire a private donor merely because the public repository now understands its function. Backend custody must exist first for material that should remain working/private.

## Completion condition

A satellite is ready to become historical/recovery-only when:

1. each unique object/function has a Public, Backend, or external specialist owner;
2. private and sensitive custody has been resolved;
3. duplicate identities have been merged without multiplying evidence;
4. inbound/outbound pointers are repaired;
5. active agents/workflows no longer write to the old repository as authority;
6. the old front door points clearly to the new lifecycle.

## Tiny lock

> One Lattice identity, two surfaces. Backend metabolizes reality; Public shows what has earned durable public form. Donate only when another lifecycle is genuinely stronger.