# AIPAC Political Action Committee (AIPAC PAC)

**Node type:** institution / federal PAC / campaign-finance mechanism  
**Status:** active  
**Last reviewed:** 2026-08-12

## Identity

AIPAC PAC is the federal political action committee formally connected to the American Israel Public Affairs Committee.

FEC committee:

```text
name: AMERICAN ISRAEL PUBLIC AFFAIRS COMMITTEE POLITICAL ACTION COMMITTEE
id: C00797670
type: Membership Organization PAC - Qualified
designation: Lobbyist/Registrant PAC
connected_organization: AMERICAN ISRAEL PUBLIC AFFAIRS COMMITTEE
```

It is distinct from United Democracy Project, which makes independent expenditures.

## Current financial scale

For 2025 through 2026-05-31, FEC data reported approximately:

- $43.95 million total receipts;
- $41.99 million contributions;
- $42.21 million total disbursements.

Source:
- https://www.fec.gov/data/committee/C00797670/

## Harm-audit purpose

AIPAC PAC should be used to trace direct candidate contribution pathways:

```text
donor / member
-> AIPAC PAC
-> candidate committee
-> office / committee authority
-> vote / appropriation / policy action
-> civilian-harm or power consequence
```

Candidate receipt is an investigation trigger, not proof of control, corruption, or agreement on every policy.

## Required population audit

For each cycle:

1. export all candidate/committee disbursements;
2. separate party and chamber;
3. join to candidate Israel/Gaza/arms positions;
4. join to votes on military aid, arms transfers, sanctions, ceasefire, settlements, ICC/ICJ, Iran war, and humanitarian aid;
5. preserve timing before and after key votes;
6. identify recipients who depart from AIPAC-preferred policy as counterexamples;
7. build contribution records only where a meaningful policy/harm edge is supported.

## Locks

```text
PAC contribution != purchased vote
PAC recipient != AIPAC employee
PAC contribution != legal or moral innocence
AIPAC PAC != UDP
AIPAC PAC != Jewish people / Judaism / Israeli government
```
