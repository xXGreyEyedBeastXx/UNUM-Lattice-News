# AIPAC Two-Hop Network Expansion — 2026-08-12

```yaml
status: ACTIVE_RESEARCH_NOTE
class: NETWORK_TRAVERSAL
anchor: AIPAC
as_of: 2026-08-12
scope: direct and two-hop evidenced relations
```

## Purpose

Test the lattice as a network rather than as a stack of dossiers.

A network requires documented relations. A conspiracy requires stronger evidence of coordinated secret or unlawful purpose. Do not collapse the two.

## Anchor

AIPAC is selected as the current anchor because it already has high-weight direct edges in lobbying, campaign finance, electoral intervention, congressional advocacy, military-aid policy, Iran policy, and organizational governance.

## One-hop neighbors

### AIPAC PAC

FEC committee `C00797670` is explicitly connected to AIPAC. For 2025 through 2026-05-31 it reported approximately $43.95m in receipts and $42.21m in disbursements.

Source: https://www.fec.gov/data/committee/C00797670/

Relation:
```text
AIPAC --CONNECTED_ORGANIZATION--> AIPAC PAC
```

### United Democracy Project (UDP)

FEC committee `C00799031` is an independent-expenditure-only super PAC. For 2025 through 2026-05-31 it reported approximately $98.63m in receipts and $34.11m in disbursements, including about $12.65m in coded independent expenditures during that period.

Existing branch evidence separately confirms AIPAC transferred $30m to UDP during the current cycle.

Sources:
- https://www.fec.gov/data/committee/C00799031/
- repository contribution record: `contributions/aipac/2025-aipac-funds-udp-30m.yaml`

Relation:
```text
AIPAC --FUNDS / BACKS--> UDP
```

### AIPAC Board / leadership

AIPAC's current board page says organizational decisions are set by its Board of Directors and identifies:
- Bernie Kaminetsky — President;
- Michael Tuchin — Board Chair;
- Elliot Brandt — CEO / professional staff leader.

AIPAC's 2024 succession announcement says Brandt had been central to policy discussion, worked directly with policymakers, and helped drive AIPAC's political strategy and fundraising growth.

Sources:
- https://aipac.org/board
- https://aipac.org/press-release/ceo-elliot-brandt

Relations:
```text
AIPAC Board --SETS POLICY / POLITICAL DIRECTIVES--> AIPAC
Elliot Brandt --LEADS PROFESSIONAL STAFF--> AIPAC
```

### Formal federal lobbying

Senate LDA records identify AIPAC as a registered lobbying organization focused on U.S. Middle East foreign policy.

Reported lobbying amounts include:
- 2025 Q1: $963,135
- 2025 Q2: $880,060
- 2025 Q3: $940,000
- 2025 Q4: $973,910
- 2026 Q1: $844,410
- 2026 Q2: $810,990

This yields approximately $3.76m reported for 2025 and $1.66m for the first half of 2026.

Sources:
- https://lda.senate.gov/filings/public/filing/search/?affiliated_organization=&affiliated_organization_country=&client=&client_country=&client_ppb_country=&client_state=&foreign_entity=&foreign_entity_country=&foreign_entity_ownership_percentage_max=&foreign_entity_ownership_percentage_min=&foreign_entity_ppb_country=&lobbyist=&lobbyist_conviction_date_range_from=&lobbyist_conviction_date_range_to=&lobbyist_conviction_disclosure=&lobbyist_covered_position=&registrant=american+israel&registrant_country=&registrant_ppb_country=&report_amount_reported_max=&report_amount_reported_min=&report_dt_posted_from=&report_dt_posted_to=&report_filing_uuid=&report_house_doc_id=&report_issue_area_description=&report_period=&report_year=&search=search
- https://lda.senate.gov/filings/public/filing/3cf55620-b4ec-4bf7-9c23-771dbe9a4681/print/

Relation:
```text
AIPAC --LOBBIES--> U.S. Congress / federal executive policy process
```

### Congressional candidate network

AIPAC's own 2024 retrospective states:
- 361 candidates endorsed;
- 326 endorsed candidates won general elections;
- 120 Democratic winners and 206 Republican winners;
- AIPAC members contributed more than $53m through its political portal;
- AIPAC described its members as top funders for members of multiple Democratic and Republican caucuses.

Source: https://www.aipac.org/memos/policy-politics-congress-israel

Relation:
```text
AIPAC / members / AIPAC PAC --SUPPORT--> large bipartisan congressional candidate population
```

Do not infer that every supported candidate is controlled by AIPAC.

## Two-hop paths

### UDP -> electoral targets / beneficiaries

AIPAC's own 2024 memo claims UDP/AIPAC intervention helped defeat:
- Jamaal Bowman;
- Cori Bush;
- David Kim;
- Bob Good.

The same memo identifies George Latimer, Wesley Bell, Jimmy Gomez, and John McGuire as the pro-Israel beneficiaries/opponents in those races.

Existing branch records already cover Bowman and Bush. Bob Good is particularly useful as a cross-partisan case because AIPAC says he was targeted after voting against a $14.3b Israel emergency-funding package.

Source: https://www.aipac.org/memos/policy-politics-congress-israel

Two-hop examples:
```text
AIPAC -> UDP -> opposes Bowman -> Latimer wins
AIPAC -> UDP -> opposes Bush -> Bell wins
AIPAC -> UDP -> opposes Bob Good -> McGuire wins
```

### AIPAC -> Congress -> Israel military capacity

AIPAC says it worked with Congress on the 2024 Israel package and describes $18.1b in security-related funding. Public Law 118-50 included, among other items:
- $4.4b Defense-Wide operation/maintenance funds tied to replacement/repair of defense articles and services for Israel;
- $3.5b Foreign Military Financing for Israel;
- additional missile-defense and related cooperation funding elsewhere in the division.

Sources:
- https://www.aipac.org/memos/policy-politics-congress-israel
- https://www.congress.gov/118/plaws/publ50/PLAW-118publ50.htm
- https://www.congress.gov/bill/118th-congress/house-bill/815/text

Two-hop path:
```text
AIPAC --ADVOCATES / LOBBIES--> Congress
Congress --APPROPRIATES--> Israel military / defense capacity
```

Civilian-harm attribution requires later weapon/event/capacity tracing; the appropriations edge itself is confirmed.

### AIPAC -> Congress -> FY2026 / FY2027 defense cooperation

AIPAC states it worked with pro-Israel congressional leaders to include more than $4b in FY2026 U.S.-Israel programs, including $3.3b security assistance without added conditions and $500m missile-defense cooperation.

In July 2026 AIPAC praised House passage of FY2027 NDAA provisions authorizing $750m for U.S.-Israel cooperative programs and specifically thanked House leadership, HASC Chair Mike Rogers, Ranking Member Adam Smith, and bill champions including Ronny Jackson and Don Davis.

Sources:
- https://www.aipac.org/memos/4-billion-america-israel-appropriations
- https://www.aipac.org/press-release/israel-defense-fiscal-year-27-ndaa

Candidate second-hop nodes:
- Mike Rogers
- Adam Smith
- Ronny Jackson
- Don Davis
- House leadership relevant to the enacted/authorized provisions

These names enter the queue because AIPAC itself identifies them as policy partners; individual responsibility requires vote/sponsorship/committee tracing.

### AIPAC -> Iran-war policy network

AIPAC's 2026 public statements praised the joint U.S.-Israeli military campaign against Iran, described military integration as unprecedented, and urged Congress to preserve diplomatic, economic, and military leverage. AIPAC also praised President Trump and Secretary Rubio in subsequent regional agreements.

Sources:
- https://www.aipac.org/press-release/iran-ceasefire-announcement
- https://www.aipac.org/press-release/iran-mou
- https://www.aipac.org/memos/prevent-nuclear-iran

Two-hop path:
```text
AIPAC --ADVOCACY / NORMALIZATION--> Congress / Trump administration
U.S. government --MILITARY / SANCTIONS / DIPLOMATIC POWER--> Iran and regional war field
```

AIPAC's advocacy is confirmed. Causal contribution to specific strikes/deaths requires action-level evidence.

## Degree / weight assessment

Current high-value neighbor classes:

1. **Congressional policy coalition** — highest downstream state power; converts advocacy and electoral support into appropriations, sanctions, arms policy, and oversight.
2. **UDP** — highest visible electoral-money router; large cash base and explicit candidate support/opposition function.
3. **AIPAC PAC / Political Portal** — broad bipartisan candidate funding and access surface.
4. **Board / CEO** — organizational decision and strategy layer.
5. **Major donors** — upstream capital providers; currently incomplete population.

## Recommended next anchor

The next anchor should not simply be the node with the most headlines. It should be the node with the strongest combination of:

```text
degree
edge weight
control over coercive/material flows
cross-study reuse
recoverable evidence
```

By that rule, the strongest next anchor is provisionally:

> **the congressional Israel-aid / defense-cooperation policy coalition**

because it sits between political money/advocacy and actual appropriations, weapons, sanctions, military cooperation, and oversight decisions.

UDP should remain a parallel electoral-money anchor.

## Expansion rule

At every hop preserve relation type:

```text
funds
endorses
opposes
lobbies
appoints
sets_policy
votes
sponsors
appropriates
authorizes
transfers
contracts
operates
benefits_from
causes
```

Never replace these with an unlabeled `connected_to` edge when a more precise relation is known.

## Network / conspiracy lock

```text
network != conspiracy
shared donor != command
shared policy preference != secret coordination
lobbying != bribery
campaign support != purchased vote
policy alignment != identical intent
```

But the inverse error is also prohibited:

```text
not proven conspiracy != no network
legal funding != no influence
public coordination != irrelevant coordination
many individually lawful edges can still create concentrated political power
```

The lattice should model the evidenced network first and reserve stronger labels for stronger proof.
