# Lattice Evidence and Source Survival Layer

**Status:** ACTIVE / PUBLIC-SAFE SOURCE MEMORY

This directory adopts the strongest architectural feature of the former `UNUM-Lattice-News-Intake`: treating sources as durable, addressable evidence objects rather than disposable URLs.

## Intended shape

```text
evidence/
  sources/
    <source-id>/
      SOURCE.yaml
      items/
        <year>/
          <item-id>/
            RECORD.yaml
            EXCERPTS.md      # bounded excerpts only when lawful and useful
            ACCESS_LOG.yaml  # optional retrieval / correction history
            HASHES.yaml      # optional, when a lawful snapshot exists
            ROUTES.yaml      # optional claim / story / specialist pointers
```

Existing source material should be adopted only after privacy, copyright, identity, and duplication review. Do not bulk-copy the former private Intake source tree into this public repository.

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

Preserve discovery paths separately from corroboration.

## Re-entry fields

Where available, a consequential source object should preserve:

- canonical source identity;
- author / publisher / institution;
- original URL or stable identifier;
- publication / issuance time;
- first-seen and access times;
- source class, language, and jurisdiction;
- correction / revision / retraction state;
- archive or mirror pointers when lawful;
- bounded excerpts when needed and lawful;
- lawful hashes or snapshot pointers when available;
- claim / story / route identities derived from it;
- citation lineage to other reporting of the same underlying record.

## Access-state vocabulary

```text
AVAILABLE
CHANGED
CORRECTED
RETRACTED
REMOVED
PAYWALLED
ACCESS_DENIED
LINK_ROTTED
MIRROR_ONLY
LOCAL_LAWFUL_COPY_AVAILABLE
UNVERIFIED_ARCHIVE_COPY
```

Source disappearance does not prove falsity. Source persistence does not prove truth.

## Public/private membrane

Only public-safe evidence metadata and lawful public-safe derivatives belong here. Sensitive or private custody remains outside the public core and crosses by bounded packet when necessary.

## Tiny lock

> Preserve enough of the evidence route that reality can be re-entered even when the original link cannot.