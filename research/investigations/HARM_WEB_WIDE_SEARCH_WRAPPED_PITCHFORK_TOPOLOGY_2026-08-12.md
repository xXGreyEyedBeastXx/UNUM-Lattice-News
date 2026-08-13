# Harm Web Wide Search — Wrapped Pitchfork Topology — 2026-08-12

```yaml
status: ACTIVE_REVIEW
class: WIDE_HARM_WEB_TOPOLOGY
as_of: 2026-08-12
branch: harm-hierarchy-audit-v0-1
mode: harm_only
publication_status: HUMAN_REVIEW_REQUIRED
topology_hypothesis: wrapped_pitchfork
```

## Purpose

Widen the harm web beyond individual dossiers and test whether recurring public/private/political nodes form a stable topology across immigration detention, surveillance/data systems, military procurement, political influence, welfare/tax allocation, and other high-power domains.

This is a network map, not a conspiracy claim. A documented relation must retain its type. Shared interests, lobbying, campaign support, revolving-door employment, government contracts, policy agreement, or simultaneous benefit are not automatically command, bribery, secret coordination, or legal guilt.

This pass follows:

- `EDITORIAL_STANDARD.md`
- `docs/HARM_HIERARCHY_LEGIBILITY_ADVERSARIAL_AUDIT_v0_1.md`
- `research/investigations/HARM_WEB_NODE_EXPANSION_PASS_2026-08-12.md`
- `research/harm-audit/AIPAC_MONEY_INFLUENCE_HARM_TRACE_2026-08-12.md`
- `research/harm-audit/AIPAC_TWO_HOP_NETWORK_EXPANSION_2026-08-12.md`
- `research/harm-audit/INITIAL_HARM_HIERARCHY_CALIBRATION_PASS_2026-08-12.md`

---

# I. Provisional topology — the wrapped pitchfork

The wide search repeatedly produces three upstream prongs that converge on implementation choke points:

```text
                  [ POLITICAL / IDEOLOGICAL INFLUENCE ]
                    donors / PACs / lobbying / think tanks
                              \       /
                               \     /
[ PRIVATE CAPITAL / FIRMS ] ---> [ POLICY / PROCUREMENT ] <--- [ STATE / EXECUTIVE AUTHORITY ]
 owners / contractors / finance       |                         executive / agencies / Congress
                 |                    |
                 |                    v
                 +----------> [ IMPLEMENTATION CAPACITY ]
                               detention / surveillance /
                               weapons / benefits / enforcement
                                         |
                                         v
                                [ HARMED POPULATIONS ]
```

The shape wraps around because implementation commonly creates money, access, personnel, dependency, or institutional advantage that can return upstream:

```text
wealth / ownership
-> lobbying / PACs / policy organizations
-> personnel / elections / access / agenda pressure
-> public authority / appropriations / procurement
-> contracts / protected markets / revenue / asset value
-> more wealth / institutional capacity
-> renewed influence
```

A second loop can operate through personnel:

```text
public office
-> private contractor / lobbying / consulting
-> public office
```

The topology is therefore better described as a **three-prong recursive braid** than a one-way hierarchy. The user-facing shorthand `wrapped pitchfork` remains useful so long as each arrow is independently evidenced.

## Anti-overclaim lock

```text
network != conspiracy
lobbying != bribery
campaign support != purchased vote
contract award != corrupt award
revolving door != proven favoritism
corporate revenue from state demand != corporate authorship of policy
policy overlap != organizational control
shared donor != command
```

But the inverse erasure is also prohibited:

```text
not proven conspiracy != no network
legal lobbying != no influence
legal contract != no incentive
recusal claim != independently verified recusal
many lawful edges can still create concentrated power
```

---

# II. Strongest closed / near-closed loop — ICE, detention money, contractors, personnel

## A. Public money expands the detention choke point

### CONFIRMED

P.L. 119-21 provides **$45 billion through FY2029 to ICE specifically for detention capacity**. CRS describes total ICE reconciliation funding of about **$74.85 billion**, including the $45 billion detention-capacity appropriation and about $29.85 billion for operations/procurement.

Sources:
- Congress.gov H.R.1 summary: https://www.congress.gov/bill/119th-congress/house-bill/1
- Congress.gov statutory text/committee print: https://www.congress.gov/committee-print/119th-congress/house-committee-print/60587
- CRS R48704: https://www.congress.gov/crs_external_products/R/HTML/R48704.html

Confirmed edge:

```text
Congress + presidential enactment
--APPROPRIATES-->
ICE detention / removal capacity
```

Do not assign the entire appropriation to one person. Individual votes, sponsorship, leadership, presidential advocacy/signature, agency implementation, and contractor awards require contributor-specific records.

## B. GEO Group depends heavily on ICE revenue

### CONFIRMED

GEO Group's 2025 10-K reports:

- ICE supplied **47.6% of total consolidated revenue in 2025**;
- BOP + ICE + U.S. Marshals Service supplied 66.6% of consolidated revenue;
- facility-management revenue is often occupancy-linked and some contracts include guaranteed minimums;
- lower occupancy / supervision participation can reduce revenue/profitability.

Source:
- SEC GEO 2025 10-K: https://www.sec.gov/Archives/edgar/data/923796/000119312526071747/geo-20251231.htm

Confirmed edge:

```text
ICE detention / supervision demand
--CONTRACTS-->
GEO
--GENERATES-->
private revenue
```

This proves a revenue dependence/incentive architecture. It does **not** prove GEO caused federal arrests or detention expansion.

## C. CoreCivic shows the same structural dependency

### CONFIRMED

CoreCivic's 2025 10-K reports:

- federal correctional/detention authorities supplied **54% of total revenue**;
- ICE alone supplied **35% of total 2025 revenue**, about **$770.7 million**;
- ICE share rose from 29% in 2024 to 35% in 2025;
- federal management revenue rose materially in 2025.

Source:
- SEC CoreCivic 2025 10-K: https://www.sec.gov/Archives/edgar/data/1070985/000119312526060669/cxw-20251231.htm

Confirmed edge:

```text
ICE / federal detention demand
--CONTRACTS-->
CoreCivic
--GENERATES-->
private revenue
```

## D. Contractor money returns toward the policy environment

### CONFIRMED for lobbying/PAC activity; PENDING for decision-specific causation

Existing federal lobbying records show GEO and CoreCivic lobby on immigration, DHS/ICE appropriations, detention, alternatives to detention, public-private partnerships, and related federal issues. Both maintain federal PACs.

This supports:

```text
contractor revenue / corporate resources
-> lobbying + PAC activity
-> congressional / executive policy environment
```

It does **not** establish:

```text
lobbying dollar
-> named vote / contract / detention quota
```

without transaction/communication/decision-specific evidence.

PATH_FORWARD:
- build quarter-by-quarter LDA table;
- map named lobbyists and former covered positions;
- map lobbying issue codes to appropriations and procurement windows;
- compare lobbying contacts with specific contract solicitations/awards where records exist;
- map PAC recipients to detention appropriations/votes without assuming purchase.

## E. Personnel completes a visible return path: David Venturella

### CONFIRMED

David Venturella previously worked in ICE, left government for GEO Group, spent roughly 12 years in GEO leadership/business-development roles, then returned to ICE. Reporting in 2025 documented that he had received an ethics waiver permitting work touching GEO matters while ICE said he had no role in reviewing/approving/recommending contracts. In May 2026 DHS announced that Venturella would become acting ICE director.

Sources:
- Washington Post, 2025-08-01: https://www.washingtonpost.com/business/2025/08/01/ice-david-venturella-geo-immigration-detention/
- Reuters, 2026-05-13: https://www.reuters.com/legal/government/us-ice-official-who-worked-private-prison-firm-will-be-agencys-new-acting-head-2026-05-13/

Confirmed personnel path:

```text
ICE
-> GEO Group
-> ICE detention-contract leadership
-> acting ICE director
```

### PENDING — favoritism / improper contracting influence

The revolving-door path and waiver are confirmed. Improper steering of contracts to GEO is **not confirmed** by those facts alone.

PATH_FORWARD:
- recover waiver text;
- procurement recusal/ethics records;
- contract approval chains;
- Venturella communications and calendars where lawfully public;
- source-selection documentation;
- inspector-general / congressional findings.

## F. Tom Homan — adjacent personnel/conflict bridge

### CONFIRMED

Financial-disclosure reporting shows Tom Homan previously received consulting fees from GEO Care before becoming Trump's border czar. The White House says Homan recuses himself from government-contract discussions, and ICE said he had not participated in contract discussions or decisions.

Source:
- Washington Post, 2025-05-27: https://www.washingtonpost.com/business/2025/05/27/border-czar-ethics-consulting-fees/

Confirmed:

```text
GEO-related consulting
-> later high-level immigration-policy authority
```

PENDING:
- whether he influenced any decision that materially benefited GEO despite the stated recusal.

The recusal claim is material counterevidence and must remain attached to the node until independently defeated or verified.

### Current detention-loop read

```text
public authority
-> very large detention appropriation
-> ICE demand
-> GEO / CoreCivic revenue
-> lobbying / PAC / personnel ecosystem
-> public policy / agency environment
-> renewed detention capacity
```

This is presently the **best-supported example of the wrapped pitchfork** because money, authority, contractors, lobbying, and personnel-return edges are all separately visible. The causal contribution of any one lobbying expenditure or individual official to a specific award remains narrower and often pending.

---

# III. Ideology / personnel / executive authority loop — Heritage / Project 2025

## A. Project 2025 explicitly joined policy to personnel and implementation

### CONFIRMED

Heritage described Project 2025 as a four-pillar architecture:

1. policy agenda;
2. personnel recruitment/database;
3. training / Presidential Administration Academy;
4. 180-day implementation playbook.

Heritage also publicly described the project as preparing vetted/trained personnel to enter government and use the mechanisms/levers of power on Day One.

Sources:
- Heritage Project 2025 overview: https://www.heritage.org/conservatism/commentary/project-2025
- Heritage personnel/project announcement: https://www.heritage.org/press/former-trump-appointee-troup-hemenway-joins-heritages-project-2025
- Heritage coalition announcement: https://www.heritage.org/press/project-2025-continues-grow-60-partners-preparing-next-presidential-administration

This supports a stronger edge than ordinary ideological similarity:

```text
Heritage / Project 2025 coalition
--DEVELOPS-->
policy + personnel + training + implementation plans
```

It still does not prove Heritage controls the administration.

## B. Russ Vought is a literal policy-personnel bridge

### CONFIRMED

Heritage's `Mandate for Leadership` author list identifies Russ Vought as author of the Executive Office of the President chapter. The White House currently identifies Vought as OMB director and notes that he previously spent seven years as vice president of Heritage Action for America.

Sources:
- Heritage chapter list: https://www.heritage.org/node/25155114/print-display
- White House Cabinet: https://www.whitehouse.gov/administration/cabinet/

Confirmed path:

```text
Heritage movement / Project 2025 policy work
-> Russ Vought
-> OMB / executive budget-regulatory authority
```

PENDING:
- exact recommendation-by-recommendation causal lineage from his Project 2025 chapter to each current OMB action.

PATH_FORWARD:
- build text-level crosswalk between Vought chapter recommendations and OMB memoranda/executive actions;
- distinguish proposals independently supported by Trump/Republican officials before Project 2025;
- identify implementation records naming Vought or OMB as decision makers.

## C. Stephen Miller is a high-authority implementation node

### CONFIRMED

The White House identifies Stephen Miller as Deputy Chief of Staff for Policy and Homeland Security Advisor. In June 2025 the White House republished Miller's statement that the reconciliation bill would increase "by orders of magnitude" the scope, scale, and speed of removals and described the bill as the vehicle for deportation and welfare-policy changes.

Sources:
- White House role reference: https://www.whitehouse.gov/videos/%F0%9F%94%A5deputy-chief-of-staff-for-policy-and-homeland-security-advisor-stephen-miller-destroys-the-media/
- White House OBBBA statement: https://www.whitehouse.gov/releases/2025/06/icymi-most-essential-piece-of-legislation-in-the-western-world/

Confirmed edge:

```text
White House policy authority + explicit removal-expansion advocacy
-> support for legislation expanding detention / removal capacity
```

Individual downstream detentions/deaths remain shared-harm objects requiring separate attribution.

## Topology read

The Project 2025 lane demonstrates the ideological prong can be more than passive commentary:

```text
think-tank / coalition policy design
-> personnel preparation
-> personnel enter government
-> executive / budget / regulatory authority
-> implementation
```

This is a **documented institutional pipeline**. `Pipeline` does not mean every administration decision originates at Heritage.

---

# IV. Political-money / electoral / military-policy loop — AIPAC / AIPAC PAC / UDP

The branch already contains deeper source-traced AIPAC files. Do not duplicate the entire lane here.

## CONFIRMED current money scale

Existing branch evidence records:

- AIPAC PAC receipts of roughly $43.95 million and disbursements of roughly $42.21 million for 2025 through 2026-05-31;
- United Democracy Project receipts of roughly **$98.63 million** and disbursements of roughly **$34.11 million** in the same period;
- approximately $12.65 million in UDP coded independent expenditures during that period;
- AIPAC's own public claims of electoral interventions and congressional Israel-policy advocacy.

Primary current FEC source for UDP:
- https://www.fec.gov/data/committee/C00799031/

Repository sources:
- `research/harm-audit/AIPAC_MONEY_INFLUENCE_HARM_TRACE_2026-08-12.md`
- `research/harm-audit/AIPAC_TWO_HOP_NETWORK_EXPANSION_2026-08-12.md`

## Confirmed broad path

```text
AIPAC / members / PAC / UDP
-> lobbying + candidate support/opposition
-> electoral opportunity / congressional coalition
-> appropriations / arms / sanctions / accountability policy
-> Israeli military/state capacity
```

The branch has confirmed the advocacy, spending, intervention, and appropriations edges in multiple cases.

## PATH_FORWARD — close candidate-specific harm loops

Do not leap from AIPAC spending to civilian death without the missing connectors.

Required chain:

```text
donor / AIPAC vehicle
-> candidate-specific support/opposition
-> office / committee / vote / sponsorship
-> appropriation / arms / accountability decision
-> weapon / military capacity
-> identified civilian consequence
```

Where this closes, actor-specific contribution can be scored. Where it does not, retain structural/influence edges without inventing direct casualty attribution.

---

# V. Defense-industrial loop — government procurement, contractor revenue, lobbying

## A. Lockheed Martin is highly dependent on public military spending

### CONFIRMED

Lockheed Martin's 2025 10-K reports:

- **72% of $75.0 billion in 2025 sales came from the U.S. Government**;
- 63% came from the Department of Defense;
- international sales include foreign military sales contracted through the U.S. Government;
- U.S. budget/procurement priorities materially affect company performance.

Source:
- SEC Lockheed Martin 2025 10-K: https://www.sec.gov/Archives/edgar/data/936468/000162828026004195/lmt-20251231.htm

Confirmed edge:

```text
Congress / executive military policy
-> appropriations / procurement / FMS
-> Lockheed sales / production demand
```

## B. Israel arms-transfer contractor edges are independently visible

Existing DSCA/arms-sale records identify Lockheed, Boeing, General Dynamics and other firms as principal contractors for major Israel-related munitions, missile, aircraft, or guidance-system sales.

Institutional path:

```text
State / DoD / Congress authorization and funding
-> FMS / procurement
-> defense contractor production/revenue
-> military capability delivered
```

Specific civilian-harm attribution requires weapon-event linkage.

## C. Return path: lobbying / PAC activity

Major defense contractors maintain lobbying operations and PACs and lobby on NDAA, appropriations, weapons programs, export/FMS policy, and related procurement matters.

This supports a return edge:

```text
public-contract revenue / corporate resources
-> lobbying + PAC activity
-> future authorization / appropriation environment
```

It does **not** prove a specific contract or war was purchased.

### PATH_FORWARD

- create one institutional node each for Lockheed, RTX, Boeing, General Dynamics;
- ingest LDA filings by issue/program;
- map PAC recipients to relevant committees/votes;
- trace named systems to arms-transfer notices and delivery dates;
- only then trace named weapons to specific civilian-harm events.

## Topology read

Defense is a second major example of the recursive structure:

```text
public military budget
-> private contractor revenue
-> lobbying / political finance
-> public military budget / procurement environment
```

The current evidence proves the endpoints and influence machinery; decision-specific causal weight remains transaction-specific.

---

# VI. Data / technology contractor loop — Palantir and Musk/SpaceX

## A. Palantir

The existing node pass confirms large U.S.-government revenue and current ICE/defense analytics contracts.

Confirmed:

```text
public coercive / military authority
-> Palantir procurement
-> private revenue + government analytical capacity
```

PATH_FORWARD:
- trace individual systems to operational use and affected people;
- separate data supplier, policy authorizer, operator, and downstream harm.

## B. Musk / SpaceX / DOGE cross-seat architecture

Existing branch evidence identifies Elon Musk as an unusually strong public/private bridge because he simultaneously occupied a high-level government-efficiency influence seat while companies he controlled remained major federal contractors.

The topology of concern is:

```text
private owner / federal contractor
-> temporary executive influence over agencies / contracts / workforce
-> government remains dependent on contractor capabilities
```

That is a confirmed conflict architecture when the roles overlap. Improper favoritism, retaliation, self-dealing, or use of public authority for a specific contract remains transaction-specific and must not be inferred from overlap alone.

PATH_FORWARD:
- contract-by-contract DOGE review records;
- recusal/conflict documents;
- agency dependency analyses;
- SpaceX award decisions during DOGE period;
- Grok/X data-system use and authorization records;
- identify whether any DOGE action directly changed a Musk-company competitor/customer's position.

---

# VII. Allocation loop — tax/benefit policy and concentrated asset ownership

## CONFIRMED — current policy redistributes resources asymmetrically

Existing CBO analysis of P.L. 119-21 finds that households toward the bottom lose resources while middle/upper groups gain resources, with the top income decile receiving a large majority of the modeled net household-resource increase.

Source:
- CBO: https://www.cbo.gov/interactive/2025-reconciliation-act

This provides a clean allocation edge:

```text
Congress + President
-> tax / benefit law
-> lower Medicaid/SNAP/in-kind resources at bottom
+ higher net household resources toward top
```

## PENDING — donor/owner influence on specific provisions

The distributional result is confirmed. It does not by itself identify who caused Congress to choose each tax/benefit provision.

PATH_FORWARD:
- provision-by-provision sponsor/committee history;
- lobbying disclosures by affected industries;
- donor/beneficiary overlap;
- corporate and trade-association advocacy;
- distributional incidence by provision;
- asset ownership concentration as a separate beneficiary map.

This is where the oligarchy hypothesis becomes testable rather than rhetorical:

```text
wealth concentration
-> political spending / lobbying / access
-> provision-level policy
-> increased after-tax / asset-owner resources
-> increased wealth concentration
```

Only close the loop when the provision-level influence edge is evidenced.

---

# VIII. Cross-domain probes that fit the shape but are not yet closed

## Healthcare / Medicare Advantage

Sector-level evidence shows a structure in which public money flows through private insurers while prior authorization can restrict access to care. Current HHS OIG work has raised concerns about high overturn rates for appealed Medicare Advantage skilled-nursing prior-authorization denials.

Current state: **PATH_FORWARD** for firm-specific attribution.

Do not assign sector-wide denial findings to UnitedHealth or another named firm without extracting organization-level data.

Potential path:

```text
CMS public funds
-> private Medicare Advantage plan
-> utilization-management decision
-> denied/delayed care
-> patient consequence
```

Then test return loop:

```text
plan revenue
-> lobbying / PAC / policy advocacy
-> Medicare Advantage rules / rates
```

## Fossil fuel / climate regulation

EPA and White House records show major current changes in methane/waste-emissions and energy-development policy that materially affect oil/gas compliance costs and extraction opportunity.

Current state: **PATH_FORWARD** for named corporate influence loops.

Potential path:

```text
fossil company / trade association
-> lobbying / political finance
-> regulatory rollback / leasing / permitting
-> corporate savings / production opportunity
-> emissions / ecological consequence
```

Do not infer the lobbying edge until LDA/campaign/meeting/decision records are attached.

---

# IX. Node-promotion queue after wide search

## Highest-priority institution nodes

### Tier A — already high connectivity / strong evidence

1. **DHS / ICE** — coercive authority + procurement + detention + surveillance/data + contractor dependence.
2. **GEO Group** — detention/monitoring contractor; very high ICE revenue exposure.
3. **CoreCivic** — detention contractor; high federal/ICE revenue exposure.
4. **Palantir Technologies** — analytics/data capacity for ICE and defense.
5. **Heritage Foundation / Project 2025 coalition** — documented policy/personnel/training implementation pipeline.
6. **AIPAC / AIPAC PAC / UDP** — lobbying + electoral finance + Israel-policy advocacy network; already split into separate legal entities in branch files.
7. **Defense-industrial cluster** — Lockheed / RTX / Boeing / General Dynamics as separate actors linked by public procurement/FMS.

### Tier B — structural probes needing more actor-specific closure

8. Medicare Advantage / insurer administrative-power cluster.
9. Fossil-fuel lobbying/regulatory cluster.
10. Asset-management / institutional ownership layer — must distinguish beneficial ownership, index stewardship, proxy voting, and actual control before drawing power conclusions.

## Highest-priority person nodes

### Promote now

1. **Stephen Miller** — high-level White House policy/homeland-security authority + explicit removal-expansion advocacy.
2. **Russ Vought** — Project 2025/Heritage lineage + current OMB authority.
3. **David Venturella** — unusually strong public-private-public revolving-door node; now acting ICE director.
4. **Tom Homan** — former GEO Care consultant + current border-policy authority; recusal claims must remain attached.

### Existing high-connectivity anchors

5. Donald Trump.
6. Elon Musk.
7. Peter Thiel.
8. Joe Biden — continuity/partial-restraint comparison seat.
9. Kamala Harris — normalization/policy-position comparison seat with lower direct operational attribution so far.

### Next-wave candidates

- relevant congressional architects/vote leaders for the $45B ICE detention appropriation;
- defense authorization/appropriation committee leaders;
- AIPAC-identified congressional policy partners, evaluated individually;
- major contractor CEOs only where decision authority and conduct can be separated from corporate adjacency;
- named lobbyists/revolving-door officials with actual issue/contract overlap.

---

# X. Centrality must be separate from harm

A node can be highly connected without having a high confirmed RHS. Do not convert graph degree into moral guilt.

Recommended separate topology vector:

```yaml
centrality_vector:
  authority_edges: 0
  money_edges: 0
  procurement_edges: 0
  implementation_edges: 0
  personnel_edges: 0
  lobbying_electoral_edges: 0
  oversight_edges: 0
  harm_domains_reached: 0
```

Then keep existing harm tuple independent:

```text
HR = [RHS, SHS, CRS]
```

This permits distinctions such as:

```text
high harm + high connectivity      -> major structural harm node
high harm + low connectivity       -> severe localized actor
low confirmed harm + high capacity -> enabling / chokepoint node requiring investigation
high centrality + pending causation -> do not prematurely score realized harm
```

---

# XI. Current topology finding

The wide search does **not** support a single-mastermind model.

It does support a recurring architecture in which:

1. **state authority** supplies coercion, law, appropriations, procurement, enforcement, war-making, detention, and benefit eligibility;
2. **private capital and contractors** supply detention beds, weapons, analytics, logistics, communications, healthcare administration, and other implementation capacity while receiving public revenue;
3. **political/ideological influence systems** supply lobbying, campaign money, candidate selection pressure, policy blueprints, personnel pipelines, and public normalization;
4. **money and personnel can return upstream**, strengthening the same nodes that benefited from the public decisions;
5. **human consequences remain downstream**, often concentrated among people with the least exit power.

Provisional recursive shape:

```text
CAPITAL / OWNERSHIP
      |
      v
LOBBYING / PACs / THINK TANKS / ACCESS
      |
      v
POLICY / PERSONNEL / ELECTIONS
      |
      v
STATE AUTHORITY / APPROPRIATIONS / PROCUREMENT
      |
      +--------------------------+
      |                          |
      v                          v
CONTRACTOR REVENUE         COERCIVE CAPACITY
      |                          |
      +---------> wealth         v
      ^                    HARMED POPULATIONS
      |                          |
      +---- influence loop ------+
```

The final arrow from harmed populations back to influence is **not** a benefit loop; it represents political reaction, criminalization, dependency, emergency spending, backlash, or other consequences that may itself become input to the next policy cycle. Those return routes require domain-specific evidence.

---

# XII. Re-entry queue

1. **ICE detention appropriation contributor map** — sponsor/committee/leadership/vote/signature attribution for the $45B detention line.
2. **Venturella ethics-waiver packet** — exact scope, recusal, contract authority, GEO-related decisions.
3. **Homan conflict packet** — disclosure, recusal terms, communications, contractor-policy overlap.
4. **GEO/CoreCivic lobbying population** — LDA + PAC recipients + contract timing.
5. **Project 2025 implementation crosswalk** — recommendation -> official -> executive/OMB/agency action.
6. **AIPAC candidate-to-policy closure** — money -> candidate -> vote -> appropriation/arms -> capacity -> civilian consequence.
7. **Defense contractor loop** — firm-specific lobbying/PAC -> committee/appropriation -> contract/FMS -> weapon delivery -> event-level harm.
8. **Palantir field-use trace** — contract deliverables -> data source -> user -> target -> enforcement outcome -> correction/appeal.
9. **Musk/SpaceX/DOGE conflict trace** — public decision -> contractor/competitor effect -> recusal/knowledge/benefit.
10. **Healthcare** — MA organization-level denial/overturn data -> patient consequences -> CMS money -> lobbying.
11. **Fossil/climate** — API/company lobbying -> named rule/lease decision -> financial benefit -> ecological/health consequence.
12. **Wealth-policy return loop** — identify exact tax provisions and trace beneficiary industries/donors/lobbying rather than assuming aggregate top-decile benefit proves influence.

## Re-entry discriminator

For every suspected wraparound loop ask:

```text
What edge is merely adjacent?
What edge is confirmed?
What money changed hands?
What authority changed hands?
What personnel crossed the membrane?
What policy changed?
Who implemented it?
Who received revenue / power / protection?
Who was harmed?
What evidence would sever the proposed loop?
```

The web should grow by closing those arrows, not by adding unlabeled names.
