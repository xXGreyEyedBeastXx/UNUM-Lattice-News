# AIPAC / United Democracy Project Donor Map Seed — 2026-08-12

```yaml
status: ACTIVE_RESEARCH_NOTE
class: DONOR_FUNDING_NETWORK_SEED
as_of: 2026-08-12
scope: 2025-2026 cycle, initial high-value receipts only
```

## Purpose

Move one level upstream from `AIPAC/UDP spent money` to the actual funding routes.

The donor map is not a guilt map. Each donor edge records money, date, vehicle, and later independently evidenced political or material relationships.

## Confirmed direct AIPAC -> UDP funding

Raw FEC electronic filing data for United Democracy Project (`C00799031`) show:

```text
2025-09-25  American Israel Public Affairs Committee -> UDP  $25,000,000
2025-12-23  American Israel Public Affairs Committee -> UDP   $5,000,000
cycle-to-date shown after second transfer                       $30,000,000
```

The Washington Post's 2026 large-donor analysis independently lists AIPAC as a $30 million donor to United Democracy Project.

**Investigation state:** `CONFIRMED` for the $30m direct funding route.

Sources:
- Raw FEC filing display: https://capitolhillaccess.com/tr/tr_ef_receipts?sCycle=2026&sFECFrm=F3X&sFECID=C00799031
- FEC committee overview: https://www.fec.gov/data/committee/C00799031/
- Washington Post 2026 donor analysis: https://www.washingtonpost.com/elections/interactive/2026/06/25/these-are-biggest-individual-donors-2026-election-cycle/

## Other high-value current receipts exposed in initial filing pass

The same raw FEC filing display shows:

```text
2025-07-29  Paul Singer / Elliott Investment Management -> UDP       $2,500,000
2026-04-15  Manzanita Action Fund -> UDP                              $1,600,000
```

These are `CONFIRMED` as reported receipts. The identities, source capital, broader political networks, and policy motivations must be separately traced.

## Paul Singer path

Current high-value facts:

- raw UDP filings show a $2.5m contribution in the current cycle;
- Washington Post's 2026 donor analysis separately identifies Singer as one of the country's largest political donors and reports large giving to Republican Senate/House groups and pro-Trump congressional efforts;
- historical UDP records also show Singer as a repeat major donor.

### Why this matters

This is a cross-party political-money node:

```text
Paul Singer
   |-- Republican electoral funding
   `-- UDP pro-Israel Democratic-primary intervention
```

That does not prove a unified partisan command structure. It shows that the Israel-policy funding network crosses ordinary party boundaries.

### Path forward

- full FEC contribution history;
- Elliott Management public holdings and relevant Israeli/defense/energy exposures only where material and evidenced;
- Republican Jewish Coalition role/history where current records support it;
- specific access or policy advocacy;
- candidate recipients supported through multiple Singer-funded vehicles.

## Manzanita Action Fund path

Raw FEC data show $1.6m to UDP in April 2026.

Independent reporting links Manzanita Action Fund to WhatsApp cofounder Jan Koum, but that beneficial-owner/source-capital claim should remain `PATH_FORWARD` until reconstructed from primary organizational, IRS, or FEC records.

Public nonprofit records also show Manzanita Action Fund made a $2.6m grant to AIPAC in FY2024, making the provisional route potentially:

```text
source capital / donor
-> Manzanita Action Fund
-> AIPAC and/or UDP
-> electoral / lobbying activity
```

The source of Manzanita's own funds must not be inferred from its grants alone.

## Current donor topology

```text
                    individual / organizational donors
                              |
              +---------------+----------------+
              |                                |
              v                                v
            AIPAC ---------------------------> UDP
              |                                |
              v                                v
          AIPAC PAC                     independent spending
              |                                |
              v                                v
     candidate contributions          support / oppose candidates
              \                                /
               \                              /
                v                            v
                 elected political authority
                           |
                           v
                  Israel/Gaza policy acts
```

Every crossing requires its own evidence.

## Full extraction queue

The current raw filing display reports 1,454 UDP receipt records for the cycle. A complete donor population should be exported and normalized before ranking donors.

Required fields:

```yaml
donor_id: ""
donor_name_reported: ""
donor_type: individual | organization | PAC | nonprofit | other
vehicle: UDP | AIPAC_PAC | AIPAC_direct | other
date: ""
amount: 0
cycle_to_date: 0
employer_reported: ""
occupation_reported: ""
other_political_giving: []
public_business_relations: []
explicit_israel_policy_advocacy: []
access_relations: []
recipient_candidate_relations: []
source_lineage: []
unknowns: []
```

## Harm-audit rule

Donor contribution is normally an upstream material-facilitation edge, not a direct civilian-harm edge.

The stronger causal chain is:

```text
donor funding
-> political vehicle capacity
-> specific electoral intervention
-> office / policy authority
-> specific military/aid/accountability act
-> civilian consequence
```

A donor's responsibility grade rises only when additional evidence establishes knowledge, explicit advocacy, repeated pressure, requested outcomes, or more direct material participation.

## Identity lock

Never infer religion, ethnicity, citizenship, dual loyalty, or foreign-government control from a donor's name or participation.

The object is the documented political-money relation.
