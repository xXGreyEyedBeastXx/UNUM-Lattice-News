# Lattice Public Evidence Projection

**Status:** ACTIVE / REVIEWED PUBLIC-SAFE SOURCE MEMORY

The complete working source-survival lifecycle is intended to live in `UNUM-Lattice-News-Backend` once that private repository exists.

This public directory preserves only the part of the evidence route that is appropriate and useful for public re-entry: reviewed source identity, lineage, correction/access state, bounded lawful excerpts when needed, and pointers connecting public records back to their evidentiary basis.

## Public shape

```text
evidence/
  sources/
    <source-id>/
      SOURCE.yaml
      items/
        <year>/
          <item-id>/
            RECORD.yaml
            EXCERPTS.md      # bounded, lawful, publication-appropriate only
            ACCESS_LOG.yaml  # when useful to public correction/re-entry
            ROUTES.yaml      # public claim / story / map pointers
```

Backend may retain richer working metadata, discovery paths, sensitivity-controlled material, draft reliability notes, internal hashes/snapshots where lawful, and unresolved review state.

## Source identity is not endorsement

```text
source_exists != source_reliable_on_every_claim
primary_source != neutral_source
official_source != independent_adjudication
publisher_reputation != claim_truth
mailbox_delivery != independent_corroboration
```

## Evidence lineage

One underlying record carried through multiple channels remains one evidentiary lineage unless materially independent evidence is added.

Promotion from Backend to Public is a projection of the same lineage, not new corroboration.

## Public/private membrane

```text
working / sensitive / unresolved evidence -> Backend
reviewed public-safe evidence projection -> Public evidence/
```

Until Backend exists, private donor repositories may retain working custody. Do not bulk-copy them here.

## Tiny lock

> Public preserves the inspectable evidence route. Backend preserves the fuller working memory.