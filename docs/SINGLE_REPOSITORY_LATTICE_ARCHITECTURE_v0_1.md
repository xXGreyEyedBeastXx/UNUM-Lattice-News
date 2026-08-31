# UNUM Lattice News — Public / Backend Architecture v0.3

**Status:** ACTIVE ARCHITECTURE / MIGRATION IN PROGRESS  
**Updated:** 2026-08-30

## Purpose

UNUM Lattice News is consolidating from a family of narrowly separated Lattice repositories into **one Lattice system with two active surfaces**:

```text
UNUM-Lattice-News-Backend   # active private working/evidence surface
        |
        | reviewed public-safe promotion
        v
UNUM-Lattice-News           # active public durable evidence/reporting surface
```

The Backend now exists. The consolidation remains semantic rather than a blind file move.

```text
recover donor function
-> identify lifecycle and authority
-> adopt / adapt / donate
-> preserve provenance and return path
-> verify privacy / evidence state / links
-> retire duplicate active authority only when replacement is live and verified
```

## Two surfaces, one Lattice identity

The public and backend repositories are two custody/lifecycle surfaces of the same Lattice News center.

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

Backend existence alone does not earn public projection. Public projection changes reviewed custody and expression while preserving the underlying evidence lineage unless new evidence is actually added.

## Repository boundaries, lenses, and specialist lifecycles

These are different architectural dimensions:

```text
Lattice Public / Backend split
  = visibility + lifecycle + custody membrane

external specialist repository
  = genuinely distinct study lifecycle / instruments / authority

internal Lattice lens
  = traversal and classification grammar across Lattice work
```

Geopolitics, capital/power, humanitarian-environmental analysis, trafficking, and policy-mechanism review are now treated as **Lattice routing lenses**, able to cross the same working object without forcing separate evidence copies.

Medical, Earth/Environmental Ecology, Governance, Human Relations, Chemistry, Engineering, Translation, Extremism Watch, Laundering Map, Hierarchy/Supremacy Studies, Epstein Discovery, and other wider UNUM repositories remain external specialist owners when a substantive study develops its own lifecycle.

`UNUM-Research` remains the ecology-wide external retrieval, request identity, provenance, routing, and re-entry head.

## Active Backend architecture

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
├── routes/
├── operations/
├── agents/
├── workflows/
├── schemas/
├── registries/
├── migration/
└── archive/
```

Only folders that gain durable content need to be instantiated. Backend may contain private or sensitivity-controlled material only within actual authorization/privacy rules. Private custody still requires dignity, source protection, lawful custody, and minimization.

### Already seeded

As of this update, Backend contains:

- an active front door;
- Backend source/provenance schema;
- Backend -> Public promotion packet schema;
- active Lattice internal routing registry;
- Intake-derived source identity registry under `evidence/sources/`;
- Intake-derived specialist return ledger under `routes/`;
- intake, work, promotion, and migration lifecycle front doors.

## Active Public architecture

```text
UNUM-Lattice-News/
│
├── README.md
├── EDITORIAL_STANDARD.md
├── CORRECTIONS.md
├── stories/
├── claims/
├── nodes/
├── lattice/
├── harm/
│   └── confirmed/
├── maps/
├── reviews/
├── briefings/
├── contributions/
├── evidence/
├── schemas/
├── registries/
├── docs/
└── archive/
```

Public remains the durable reviewed projection surface; raw working intake and unresolved sensitive casework route through Backend.

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

The active grammar lives at `UNUM-Lattice-News-Backend/schemas/PUBLIC_PROMOTION_PACKET_v0_1.yaml`.

Promotion is object- and claim-specific. Candidates can remain Backend-only, reviews can narrow or merge objects, and scoped harm can enter the public `CONFIRMED_HARM` state only when the exact edge earns it.

## Internal routing lenses

A Lattice object may carry multiple lenses:

```text
GEOPOLITICS
CAPITAL_POWER
HUMANITARIAN_ENVIRONMENTAL
TRAFFICKING
POLICY_MECHANISM
```

A lens selects questions, relationships, and discriminators. It can overlap another lens and does not multiply the underlying evidence lineage.

Examples:

```text
war + water + procurement
-> GEOPOLITICS + HUMANITARIAN_ENVIRONMENTAL + CAPITAL_POWER

remote extractive workforce + coercive recruitment + jurisdictional gaps
-> TRAFFICKING + CAPITAL_POWER + POLICY_MECHANISM
```

## Adopt, adapt, donate

Every donor object is classified by the lifecycle it actually needs:

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

Use when the function genuinely belongs to the Lattice center: source survival in Backend, public event records in Public, harm promotion review in Backend, scoped confirmed harm in Public.

### Adapt

Use when useful machinery exists but its old repository-specific assumptions should change. Geopolitics queues can become shared Backend routes carrying the `GEOPOLITICS` lens; capital/power maps can use common map grammar with multi-lens metadata; policy review can retain policy-mechanism analysis without inheriting a verdict-bearing repository title.

### Donate

Use when an object has developed a stronger specialist lifecycle: clinical mechanism to Medical, ecological mechanism to Earth/Environmental Ecology, authority/procedure study to Governance, relational coercion study to Human Relations, reusable generic tooling to Tools/Utilities, and so on.

Donation preserves the Lattice question, evidence route, and expected return edge.

## Former satellite disposition

The existing Lattice satellites are now active donor/recovery surfaces while Backend receives their shared working functions:

```text
UNUM-Lattice-News-Intake
UNUM-Lattice-News-Proven-Harm
UNUM-Lattice-News-Humanitarian-Environmentalism
UNUM-Lattice-News-Real-Bad-Policy
UNUM-Lattice-News-Geopolitics
UNUM-Lattice-News-Capital-and-Power
UNUM-News-Lattice-Trafficking
```

Backend existence removes the former custody blocker. It does **not** by itself authorize retiring a donor: each unique object/function still needs a verified destination, privacy/custody resolution, pointer repair, and workflow re-routing.

## Completion condition

A satellite is ready to become historical/recovery-only when:

1. each unique object/function has a Public, Backend, or external specialist owner;
2. private and sensitive custody has been resolved;
3. duplicate identities have been merged without multiplying evidence;
4. inbound/outbound pointers are repaired;
5. active agents/workflows no longer write to the old repository as authority;
6. the old front door points clearly to the new lifecycle.

## Center direction

Lattice is now serving as the first practical **center-formation** experiment: use temporary differentiation to discover real functions, then consolidate shared lifecycle machinery into a small number of meaningful custody surfaces while donating mature specialist bodies outward.

Repository count can fall while relational and evidentiary richness increases.

## Tiny lock

> One Lattice identity, two active surfaces. Backend metabolizes working reality; Public preserves what has earned durable public form. Donate when another lifecycle is genuinely stronger; keep the return path alive.