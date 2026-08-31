# UNUM-Lattice-News-Backend — Bootstrap Packet

**Status:** READY FOR REPOSITORY INSTANTIATION  
**Date:** 2026-08-30

## Repository identity

**Name:** `UNUM-Lattice-News-Backend`  
**Intended visibility:** private

**Jurisdiction:** working evidence custody, intake, review, casework, promotion, operational routing, and migration for the Lattice News system.

It is the private working counterpart to the public `UNUM-Lattice-News` repository, not an independent truth authority.

## Seed README sentence

> `UNUM-Lattice-News-Backend` is the private working surface for Lattice News intake, evidence survival, review, casework, promotion, and operational routing; reviewed public-safe results cross to `UNUM-Lattice-News` with provenance, uncertainty, privacy state, and a return path intact.

## Starter tree

```text
UNUM-Lattice-News-Backend/
├── README.md
├── intake/
│   ├── candidates/
│   ├── source-review/
│   ├── claim-extraction/
│   ├── routing/
│   └── rejected-deferred/
├── evidence/
│   └── sources/
├── work/
│   ├── investigations/
│   ├── casework/
│   ├── reviews/
│   ├── maps/
│   └── chronologies/
├── promotion/
│   ├── public-review/
│   ├── harm-review/
│   └── packets/
├── routes/
├── operations/
├── agents/
├── workflows/
├── schemas/
├── registries/
├── migration/
└── archive/
```

## First contracts to seed

Adapt/copy by meaning, not blindly:

1. `UNUM-Lattice-News/schemas/SOURCE_RECORD_v0_1.yaml`
2. `UNUM-Lattice-News/registries/LATTICE_INTERNAL_ROUTING.yaml`
3. a Backend/Public promotion-packet schema derived from the custody registry
4. the source-survival grammar recovered from `UNUM-Lattice-News-Intake`
5. harm-promotion review grammar recovered from `UNUM-Lattice-News-Proven-Harm`

## First donor order

### 1. Intake

Donor: `UNUM-Lattice-News-Intake`

Recover first:

```text
sources/REGISTRY.yaml
sources/*/SOURCE.yaml
sources/*/items/*/*/RECORD.yaml
schemas/SOURCE_RECORD_v0_1.yaml
candidates/
claims/
reviews/
routing/
```

Classify each object for privacy, duplication, and current identity before adoption.

### 2. Proven Harm working layer

Donor: `UNUM-Lattice-News-Proven-Harm`

Backend receives promotion queues/gates/reviews. Public keeps only scoped confirmed-harm projections.

### 3. Topical satellites as lenses

Donors:

```text
UNUM-Lattice-News-Geopolitics
UNUM-Lattice-News-Capital-and-Power
UNUM-Lattice-News-Humanitarian-Environmentalism
UNUM-Lattice-News-Real-Bad-Policy
UNUM-News-Lattice-Trafficking
```

Do not recreate five top-level domain silos. Convert their queues and work objects into shared Backend object types carrying one or more internal lenses.

## Promotion membrane

A Backend -> Public packet should preserve at least:

```yaml
promotion:
  backend_object_id: ""
  public_destination_id: null
  object_class: ""
  scope: ""
  clocks: {}
  sources: []
  citation_lineage: []
  claims_or_edges: []
  evidence_effects: []
  internal_lenses: []
  external_specialist_returns: []
  competing_models: []
  uncertainty: []
  missingness: []
  privacy_state: ""
  publication_safety: ""
  material_changes_during_review: []
  evidence_that_would_change_assessment: []
  backend_return_path: ""
```

## Donation test

Before absorbing a donor object into Backend, ask:

> Is this still fundamentally news/public-reality work, or has it developed a self-contained specialist lifecycle?

If the latter, donate the study body to the stronger specialist repository and preserve a Backend route + eventual Public return.

## Non-goals

- Do not centralize all UNUM research in Backend.
- Do not duplicate source lineages simply because an object crosses repositories.
- Do not turn lens names into verdicts.
- Do not make public promotion automatic.
- Do not retire private donor repositories before their unique objects are reconciled.

## Tiny lock

> Backend is the kitchen, not a second newspaper. Public is the served record, not the whole working memory.