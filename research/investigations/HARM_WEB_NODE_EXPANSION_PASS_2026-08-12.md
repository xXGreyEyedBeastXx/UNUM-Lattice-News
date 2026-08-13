# Harm Web Node Expansion Pass — 2026-08-12

```yaml
status: ACTIVE_REVIEW
class: HARM_WEB_NODE_EXPANSION
as_of: 2026-08-12
branch: harm-hierarchy-audit-v0-1
mode: harm_only
public_projection: HUMAN_REVIEW_REQUIRED
scope:
  institutions: 2
  people: 5
institutions:
  - GEO Group
  - Palantir Technologies
people:
  - Donald Trump
  - Joe Biden
  - Kamala Harris
  - Elon Musk
  - Peter Thiel
```

## Purpose

This pass extends the existing harm-first topology by adding two high-connectivity private institutions and five named people occupying different seats in the public/private power web.

The assignment is not to produce a net-moral biography. Unrelated beneficial conduct is excluded. Counterevidence is retained only where it changes the identity, scope, mechanism, chronology, attribution, or magnitude of a harm claim.

This pass follows:

- `EDITORIAL_STANDARD.md`
- `docs/HARM_HIERARCHY_LEGIBILITY_ADVERSARIAL_AUDIT_v0_1.md`
- the existing Trump system topology rather than duplicating it.

Core trace:

```text
HARMED PERSON / POPULATION
        ^
        |
      HARM
        ^
        |
    MECHANISM
        ^
        |
   IMPLEMENTER
        ^
        |
   AUTHORIZER
        ^
        |
FUNDER / ENABLER / PROTECTOR / NORMALIZER
```

A relation is not automatically coordination, guilt, conspiracy, or command. The edge type must remain explicit.

---

# I. Institution node — GEO Group

## Working seat

```yaml
actor_class: institution
node_type: private_contractor
primary_functions:
  - detention
  - transportation
  - electronic monitoring
  - case management / supervision
  - skip tracing / location research
public_private_bridge: strong
```

## CONFIRMED — government detention is a central revenue dependency

GEO Group's 2025 Form 10-K reports that ICE accounted for **47.6% of total consolidated revenue in 2025**, up from 41.5% in 2024. The Bureau of Prisons, ICE, and U.S. Marshals Service together accounted for 66.6% of total 2025 consolidated revenue.

The same filing describes 2025 ICE-linked expansion including:

- activation of the 1,800-bed North Lake facility;
- a 15-year ICE contract for the 1,000-bed Delaney Hall facility;
- continued Karnes ICE processing-center operations;
- an ICE electronic-monitoring / case-management contract through BI Incorporated;
- a skip-tracing contract involving identifiable-information research, commercial-data verification, and physical observation;
- secure transportation and contract-detention-officer work.

Source:
- SEC, GEO Group 2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/923796/000119312526071747/geo-20251231.htm

### Confirmed causal shape

```text
federal immigration-enforcement policy
-> ICE detention / supervision demand
-> government contract
-> GEO / BI service provision
-> revenue linked to detention, monitoring, supervision, transport, or location work
```

This does not require a claim that GEO controls federal immigration policy. The confirmed edge is **state coercive demand -> private revenue opportunity**.

## CONFIRMED — occupancy and participation create revenue incentives

GEO's 10-K states that most facility-management revenue is generated under per-diem arrangements based on daily occupancy, while some contracts contain guaranteed minimum occupancy payments. It separately warns that lower occupancy or lower participation in the Intensive Supervision Appearance Program can decrease revenue and profitability.

This establishes an incentive architecture in which detention/supervision utilization and company revenue are positively linked.

It does **not** by itself prove that GEO caused arrests or detention to increase.

## CONFIRMED — current ICE detention awards continue in 2026

USAspending records show current 2026 ICE task orders to GEO for detention services, including Delaney Hall and Mesa Verde / Golden State facilities.

Sources:
- Delaney Hall award: https://www.usaspending.gov/award/CONT_AWD_70CDCR26FR0000050_7012_70CDCR25D00000007_7012/
- Mesa Verde / Golden State award: https://www.usaspending.gov/award/CONT_AWD_70CDCR26FR0000042_7012_70CDCR20D00000008_7012/

## PENDING — Delaney Hall detainee death / civil-rights responsibility

New Jersey opened a civil-rights investigation in August 2026 after the death of detainee Edwin Lopez-Cornejo. His family alleges inadequate medical care; ICE says appropriate treatment was provided.

Investigation state: **PENDING**.

Do not convert the existence of the investigation or family allegation into a confirmed finding against GEO.

Source:
- Reuters, 2026-08-07: https://www.reuters.com/world/us/new-jersey-opens-civil-rights-probe-privately-run-ice-detention-center-newark-2026-08-07/

### PATH_FORWARD

Recover:

- New Jersey AG investigative findings;
- medical records and timelines if publicly filed;
- ICE mortality review / detainee death report;
- GEO staffing and medical-service records subject to lawful disclosure;
- court records or settlement filings;
- inspection reports and contract-compliance records.

## Structural position

```text
ICE authority
-> detention / monitoring population
-> GEO contracts
-> private revenue
```

GEO therefore sits at a high-conductance public/private hinge: **public coercive authority is monetized through private service contracts**.

---

# II. Institution node — Palantir Technologies

## Working seat

```yaml
actor_class: institution
node_type: data_analytics_and_government_contractor
primary_functions:
  - case management
  - investigative analytics
  - military / defense analytics
  - immigration-enforcement systems
  - government data integration
public_private_bridge: very_strong
```

## CONFIRMED — large and rapidly growing government business

Palantir's 2025 Form 10-K reports:

- $2.402 billion in 2025 government revenue, up 53% from 2024;
- $1.9 billion in 2025 U.S.-government revenue;
- $4.4 billion in remaining deal value from U.S. and allied government agencies at year-end 2025, up from $2.3 billion a year earlier.

Source:
- SEC, Palantir 2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm

## CONFIRMED — current defense contract surface

A Department of Defense award to Palantir USG beginning October 2025 has a current award amount of about **$602.9 million** and extends to 2029.

Source:
- USAspending: https://www.usaspending.gov/award/CONT_AWD_W9128Z26FA001_9700_W519TC25D0039_9700

## CONFIRMED — current ICE investigative/case-management contract surface

A June 2026 ICE award to Palantir for Homeland Security Investigations system modernization carries an obligated/current amount of about **$45.85 million** and describes investigative case management and investigative analytics.

Source:
- USAspending: https://www.usaspending.gov/award/CONT_AWD_70CTD026FC0000018_7012_70RTAC26A00000001_7001

Additional USAspending records describe Palantir work supporting enforcement/removal case-management modernization. Public reporting also documents a 2025 ICE ImmigrationOS contract intended to improve identification-to-removal workflows.

## CONFIRMED — coercive capability edge; PENDING — person-level harm attribution

Confirmed:

```text
ICE / DHS authority
-> government procurement
-> Palantir data / analytics / case-management capability
-> increased informational and operational capacity available to immigration enforcement
```

Not automatically confirmed:

```text
specific Palantir tool
-> specific arrest / detention / deportation error / rights violation
```

The latter requires tool-use evidence, individual case linkage, error data, policy configuration, or other specific causal proof.

### PATH_FORWARD

Recover:

- statement of work and deliverables for ICE case-management awards;
- ImmigrationOS deliverables and acceptance records;
- ICE training materials and usage guidance;
- system audit logs where legally/publicly accessible;
- documented false-positive / mistaken-target cases;
- data-source provenance and correction channels;
- procurement modifications and performance reports;
- court records tying particular enforcement events to the software.

## Structural position

Palantir is not merely adjacent to government coercion. It is a **paid capability supplier** to military and immigration-enforcement institutions. The harm audit must therefore separate:

1. capability supplied;
2. government policy selecting the target;
3. operational use;
4. downstream consequence;
5. Palantir's knowledge and control over the relevant configuration.

---

# III. Person node — Donald Trump

## Working seat

```yaml
actor_class: leader
seat: executive_authorizer
current_status: President of the United States
existing_repo_depth: high
this_pass: connective_only
```

Trump already has a deep repository topology. This pass adds connective edges to the new institution/person nodes rather than duplicating that record.

## CONFIRMED — immigration enforcement creates contractor demand

Current Trump-administration immigration expansion routes public appropriations and executive enforcement priorities into increased detention, tracking, surveillance, transport, and data-system demand.

GEO's 2025 filing directly describes expanded ICE facility activation and supervision contracts. Palantir has received large 2025-26 ICE enforcement/case-management awards.

Confirmed topology:

```text
Trump administration immigration policy / appropriations / executive direction
-> DHS / ICE enforcement expansion
-> detention + tracking + data-infrastructure demand
-> GEO / Palantir contract opportunities
```

Actor-specific attribution for each individual detention, deportation, or injury remains case-specific.

## CONFIRMED — upward-resource / downward-benefit allocation under P.L. 119-21

CBO concludes that the 2025 reconciliation law reduces household resources toward the bottom of the income distribution while increasing resources toward the middle and top; the highest income decile receives 63.9% of the modeled net household-resource increase, while the lowest decile loses resources, largely through Medicaid/SNAP changes.

Source:
- CBO: https://www.cbo.gov/interactive/2025-reconciliation-act

This contribution belongs to a **shared harm object** involving Congress and the executive; it must not be counted as though Trump alone produced every downstream loss.

## CONFIRMED — USAID freeze / dismantling authority chain

Trump ordered a freeze on most U.S. foreign aid on January 20, 2025. Reuters reported that Musk was entrusted by Trump with government-efficiency work around USAID and that hundreds of programs halted while staff and contractors were locked out or placed on leave.

Source:
- Reuters, 2025-02-04: https://www.reuters.com/world/us/usaids-dc-office-shuts-day-musk-trump-ramp-up-attacks-2025-02-03/

Trump occupies the higher formal authority seat in this chain.

---

# IV. Person node — Joe Biden

## Working seat

```yaml
actor_class: former_leader
seat: former_executive_authorizer
time_window: 2021-2025 presidency
working_pattern: partial_restraint_with_preserved_channels
pattern_status: SUPPORTED_INFERENCE
motive_status: UNKNOWN
```

Do not use `line rider` as a motive claim. The inspectable question is whether Biden repeatedly adopted a restraint or humanitarian layer while preserving a major mechanism producing the harm under review.

## CONFIRMED — private-prison restriction stopped at DOJ boundary

Executive Order 14006 ordered the Attorney General not to renew Department of Justice contracts with privately operated criminal detention facilities.

The order applied to DOJ. It did **not** apply to DHS/ICE immigration detention.

Sources:
- GovInfo EO 14006: https://www.govinfo.gov/app/details/DCPD-202100088
- Reuters, 2021-01-27: https://www.investing.com/news/stock-market-news/us-private-prison-revenue-under-pressure-from-new-biden-rules-2400154

Reuters reported at the time that ICE was the largest federal customer for both GEO and CoreCivic and that Biden's order did not reach DHS/ICE facilities.

### Supported inference

```text
stated concern about profit-based incarceration
-> DOJ private-prison restriction
-> DHS / ICE private detention channel preserved
```

That is a confirmed policy-boundary asymmetry. Whether it reflects compromise, political caution, legal strategy, institutional inertia, competing priorities, or another motive remains **UNKNOWN** without stronger evidence.

## CONFIRMED — Israel arms-review system identified serious concerns while transfers continued

GAO reports that under NSM-20 the Biden administration required written assurances concerning international humanitarian law and humanitarian-aid access. State assessed that U.S.-origin defense articles were likely involved in numerous concerning incidents and that it was reasonable to assess covered defense articles had been used by Israel inconsistently with human-rights obligations.

GAO also reports that State did **not pause arms transfers** under NSM-20 and did not curtail security assistance to Israel on that basis.

Sources:
- GAO: https://www.gao.gov/products/gao-25-107077
- GAO full report: https://files.gao.gov/reports/GAO-25-107077/index.html

CRS separately records that the administration paused one shipment of 2,000-pound and 500-pound bombs over Rafah concerns; the 500-pound bombs were later released while the 2,000-pound shipment remained under review at that time.

Source:
- CRS: https://www.congress.gov/crs-products/product/pdf/R/R47828/2

### Supported inference — restraint/continuity pattern

```text
civilian-harm concern recognized
-> review / assurance mechanism created
-> limited shipment restraint
-> broader military-support channel remains open
```

This is stronger support for a **policy line-riding / partial-restraint pattern** than for a claim that Biden did not care about civilians. Private motive remains unproven.

---

# V. Person node — Kamala Harris

## Working seat

```yaml
actor_class: former_leader
seat:
  - former_vice_president
  - 2024 presidential nominee
current_evidence_role: rhetorical_and_policy_position
working_pattern: dual_commitment / continuity_under_pressure
motive_status: UNKNOWN
```

## CONFIRMED — simultaneous ceasefire / Palestinian-dignity rhetoric and continued Israel-defense commitment

In her August 2024 convention speech, Harris called for a Gaza ceasefire and hostage-release deal, described Gaza's suffering as devastating, and said Palestinians should have dignity, security, freedom, and self-determination. In the same speech she said she would continue to stand up for Israel's right to defend itself.

Source:
- Reuters, 2024-08-22: https://www.investing.com/news/politics-news/kamala-harris-says-now-is-the-time-for-gaza-ceasefire-and-hostage-release-deal-3584426

## CONFIRMED — campaign did not adopt an Israel arms-embargo position

After Uncommitted activists said Harris had shown openness to discussing an arms embargo, a Harris aide said she had **not** agreed to discuss imposing an arms embargo and reiterated the campaign's existing position.

Source:
- Reuters, 2024-08-08: https://www.reuters.com/world/democrat-harris-didnt-agree-discuss-israel-arms-embargo-aide-says-2024-08-08/

## Attribution lock

Do **not** automatically assign Biden's presidential arms-transfer authorization to Harris merely because she was vice president.

Current evidence in this pass supports:

- R1/R2-type normalization / formal policy support edges for her stated positions;
- a confirmed tension between humanitarian rhetoric and refusal to adopt the embargo demanded by anti-war activists;
- **not** a confirmed finding that she personally commanded or approved particular weapons transfers.

### PENDING — `line rider` as character diagnosis

The observable dual-position pattern is real. The stronger claim that Harris was trying to please incompatible constituencies rather than act from principle is **PENDING / motive unknown**.

PATH_FORWARD:

- internal campaign / administration records if public;
- documented meeting notes on arms-policy debates;
- delegated vice-presidential foreign-policy roles;
- contemporaneous staff testimony;
- later position changes that discriminate sincere evolution from tactical adaptation.

---

# VI. Person node — Elon Musk

## Working seat

```yaml
actor_class: nontraditional_public_private_leader
seats:
  - billionaire_owner / executive
  - government_contractor ecosystem
  - temporary executive-branch influence / DOGE
bridge_type: private_wealth_to_public_authority
```

## CONFIRMED — private actor received unusually high governmental agenda access

Reuters reported in February 2025 that Trump had tasked Musk with downsizing government and entrusted him with efficiency work concerning USAID. Musk publicly called for USAID to be shut down. DOGE personnel gained access to sensitive Treasury payment systems, while USAID staff and contractors were locked out or put on leave and hundreds of programs halted.

Source:
- Reuters, 2025-02-04: https://www.reuters.com/world/us/usaids-dc-office-shuts-day-musk-trump-ramp-up-attacks-2025-02-03/

Confirmed structural shape:

```text
private wealth / corporate power
+ presidential delegation / access
-> influence over public staffing, payment, and program machinery
```

This is a high **power_concentration** signal independent of whether every proposed cut was harmful.

## CONFIRMED — humanitarian program disruption; PENDING — full mortality attribution

Reuters documented hundreds of USAID programs halting after the foreign-aid freeze and shutdown push. Experts warned of lethal consequences because USAID was a major global humanitarian-aid provider.

Confirmed:

```text
Trump aid freeze + Musk/DOGE shutdown pressure
-> administrative disruption / staff lockout / program interruption
```

Still requiring contribution-specific proof:

```text
Musk decision X
-> identified person/population death Y
```

That person-level mortality chain remains **PATH_FORWARD/PENDING** unless and until outcome studies, program records, clinical data, or other evidence close it.

### PATH_FORWARD

Recover:

- DOGE decision logs / tasking records;
- payment-block chronology;
- program-level stop-work and waiver records;
- mortality/morbidity studies tied to specific interrupted programs;
- Treasury access/authorization records;
- conflict-of-interest records involving Musk-controlled government contractors.

---

# VII. Person node — Peter Thiel

## Working seat

```yaml
actor_class: corporate_leader / political_donor
seats:
  - Palantir cofounder
  - Palantir board chairman
  - founder-control structure participant
  - political funding/network node
bridge_type: concentrated_private_control_to_state_contracting_and_politics
```

## CONFIRMED — concentrated Palantir governance power

Palantir's 2025 Form 10-K identifies Peter Thiel as chairman of the board and one of three founders participating in the Founder Voting Trust / Founder Voting Agreement. The filing states that the Class F structure can give the founders the ability to control up to **49.999999% of total voting power** while the ownership threshold is satisfied.

Source:
- SEC, Palantir 2025 Form 10-K: https://www.sec.gov/Archives/edgar/data/1321655/000132165526000011/pltr-20251231.htm

This establishes concentrated governance power. It does not establish that Thiel personally selects ICE targets or directs day-to-day Palantir operations.

## CONFIRMED — political-network adjacency with material funding significance

Reuters documented Thiel as a prominent backer of the Rockbridge Network, a donor network co-founded by JD Vance and organized to push U.S. politics rightward.

Source:
- Reuters, 2024-08-20: https://www.reuters.com/world/us/tech-donor-network-co-founded-by-jd-vance-seeks-push-america-right-2024-08-20/

## CONFIRMED — Palantir public-contract nexus; PENDING — Thiel-specific operational responsibility

Given Thiel's chairman/founder-control role and Palantir's large government-contract portfolio, there is a confirmed structural relation:

```text
Thiel governance/control seat
-> Palantir institutional strategy / oversight environment
-> government-contract business
```

But the stronger chain:

```text
Thiel personally
-> ICE product decision
-> specific enforcement harm
```

is **PENDING** absent board records, directives, communications, or other decision-specific evidence.

This distinction is important because `governance power != direct operational control`.

---

# VIII. Cross-node topology

## A. Immigration detention / surveillance / data loop

```text
Donald Trump / executive policy
        |
        v
DHS / ICE authority + appropriations
        |
        +--------------------------+
        |                          |
        v                          v
   GEO Group                   Palantir
 detention / transport        data / analytics /
 monitoring / tracking        case management
        |                          |
        v                          v
 captive / supervised / targeted immigrant population
```

The state supplies legal/coercive authority. Private firms supply capacity and receive revenue.

## B. Cross-administration continuity diagnostic

The contractor ecology is not reducible to one party.

```text
Biden:
private-prison concern
-> DOJ restriction
-> ICE private-detention channel remains

Trump:
ICE expansion
-> larger detention / tracking / contractor opportunity surface
```

This produces a useful distinction:

```text
system continuity != equal responsibility
```

A preserved channel and an aggressively expanded channel are related but not identical conduct.

## C. Israel-policy line-riding diagnostic

```text
Biden:
civilian-harm concern / NSM-20 review
+ limited bomb-shipment pause
+ broader arms channel continues

Harris:
ceasefire / Palestinian dignity rhetoric
+ continuing Israel self-defense commitment
+ no arms-embargo adoption
```

Observed dual commitments are confirmed. Motive claims such as cowardice, constituency pleasing, indifference, or deception remain separate hypotheses requiring evidence.

## D. Oligarchic public/private bridge

```text
Musk private wealth / corporate power
-> presidential access / DOGE influence
-> public administrative machinery

Thiel founder-control / donor-network power
-> Palantir governance + political network
-> public contract / policy environment
```

The common structural question is not whether rich people are inherently harmful. It is:

> How much consequence-imposing public power can private wealth acquire without reciprocal exposure, democratic authorization, or ordinary accountability?

---

# IX. Working placement — who stands where

This is **not** a moral leaderboard. It is a topology placement based on the evidence recovered in this pass.

| Node | Strongest confirmed seat in this pass | Directness to coercive/harm machinery | Main unresolved question |
|---|---|---:|---|
| Donald Trump | executive authorizer / enforcement and allocation amplifier | very high | contribution-specific causation across each shared harm object |
| Joe Biden | executive authorizer with partial-restraint / continuity pattern | high | why restraint repeatedly stopped before closing major harmful channels |
| Kamala Harris | policy-normalization / dual-position node | moderate-to-low direct operational attribution in current packet | whether dual commitments reflect principle, constraint, adaptation, or constituency management |
| Elon Musk | private-wealth -> public-authority bridge / agenda influence | high structural; case-specific realized harm pending | program-level mortality and conflict-of-interest chains |
| Peter Thiel | concentrated corporate-governance + donor-network bridge | high structural; operational harm attribution pending | decision-specific role in Palantir coercive contracts and political-policy pathways |
| GEO Group | monetized detention / supervision / tracking contractor | very high institutional exposure | facility-specific harm, medical negligence, oversight failures |
| Palantir | state data / military / investigative capability contractor | very high capability exposure | person-level enforcement harms and internal control/knowledge |

---

# X. First synthesis

The initial seven-node pass supports a broader architecture:

```text
POLITICAL AUTHORITY
        |
        v
LAW / EXECUTIVE DIRECTION / APPROPRIATION
        |
        v
AGENCY COERCIVE OR ADMINISTRATIVE DEMAND
        |
        +---------------------+
        |                     |
        v                     v
DETENTION CONTRACTOR      DATA / TECH CONTRACTOR
        |                     |
        +----------+----------+
                   |
                   v
      HUMAN CONSEQUENCE / LOSS OF EXIT
                   ^
                   |
       PRIVATE REVENUE / ASSET VALUE
                   ^
                   |
     OWNERS / EXECUTIVES / INVESTORS
```

A second loop connects wealth back to authority:

```text
wealth / ownership
-> donations / networks / access / agenda power
-> policy and procurement environment
-> contracts / tax treatment / market opportunity
-> additional wealth / ownership
```

This pass does **not** establish a single coordinated conspiracy. It establishes multiple documented conduits through which concentrated private power and concentrated public authority can reinforce one another.

The important investigative seam is **reciprocal exposure**:

```text
power to impose consequences
--------------------------------
exposure to those consequences
```

Nodes with a high ratio warrant the most aggressive evidence recovery.

---

# XI. Re-entry queue

Next searches should rotate between institution and person nodes rather than staying in one silo.

Priority paths:

1. GEO / ICE revolving-door personnel, especially contract and ethics-waiver chronology.
2. Palantir ICE product deliverables, error correction, data provenance, and actual field-use records.
3. Musk-controlled federal-contractor conflicts during DOGE access/decision periods.
4. Thiel / Palantir governance records around immigration and defense contracts.
5. Biden-era private immigration-detention contract renewals and closure decisions facility by facility.
6. Harris delegated authority and internal arms-policy role rather than public rhetoric alone.
7. Shared-harm dedup across presidents, Congress, agencies, contractors, and operational actors.

Do not score a global hierarchy until shared-harm objects and contribution records are deduplicated.
