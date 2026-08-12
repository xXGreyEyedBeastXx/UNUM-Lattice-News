# American Israel Public Affairs Committee (AIPAC)

**Node type:** institution / advocacy / lobbying / political influence  
**Status:** active  
**Last reviewed:** 2026-08-12

## Current bounded summary

AIPAC is a U.S. pro-Israel advocacy and lobbying organization that works to maintain and expand U.S. political, military, diplomatic, and financial support for Israel. Its current political influence surface includes direct lobbying and advocacy, a connected federal PAC (`AIPAC PAC`), and an aligned independent-expenditure super PAC (`United Democracy Project`, UDP).

These must remain separate records:

```text
AIPAC
  |-- advocacy / lobbying / member mobilization
  |-- AIPAC PAC -> candidate contributions
  `-- United Democracy Project -> independent expenditures
```

Do not collapse AIPAC, AIPAC PAC, UDP, Jewish people, Judaism, Zionism, the Israeli government, or individual donors into one node.

## Current financial scale

### AIPAC PAC

FEC committee `C00797670` is a qualified lobbyist/registrant membership-organization PAC connected to AIPAC.

For 2025 through 2026-05-31, the FEC reported approximately:

- $43.95 million total receipts;
- $41.99 million contributions;
- $42.21 million total disbursements.

### United Democracy Project

FEC committee `C00799031` is an independent-expenditure-only super PAC. For 2025 through 2026-05-31, the FEC reported approximately:

- $98.63 million total receipts;
- $95.80 million contributions;
- $34.11 million total disbursements;
- $12.65 million independent expenditures during the reported period;
- about $93.32 million cash on hand at period end.

These are financial-capacity facts. They do not by themselves establish that any candidate vote was purchased or controlled.

## Confirmed political objectives and electoral intervention

AIPAC's own public materials state that in 2024 it worked with Congress to pass what it described as the largest funding package in Israel's history and that UDP/AIPAC engagement helped defeat Representatives Jamaal Bowman and Cori Bush, whom it characterized as anti-Israel candidates/critics.

Reuters independently documented UDP spending against Bowman during his 2024 primary while Bowman was calling for a permanent Gaza ceasefire and describing Israel's conduct as genocide and ethnic cleansing.

AIPAC's own claim of helping defeat Bowman and Bush is therefore `CONFIRMED` as AIPAC's stated political role; exact causal contribution to the election result remains multi-factor and must not be represented as sole causation.

## Gaza / genocide evidence context

By December 2024 Amnesty International concluded that Israel was committing genocide against Palestinians in Gaza. In 2025 the UN Independent International Commission of Inquiry concluded that Israeli authorities and security forces had committed genocide against Palestinians in Gaza and possessed the required specific intent under the Genocide Convention.

This repository records those findings as major evidence objects even though a final ICJ merits judgment is a distinct legal event.

Therefore, post-finding political funding and advocacy for continued Israeli military support is a mandatory high-priority harm/complicity trace. It is **not automatic proof** that every AIPAC-backed candidate intended genocide, knew every military consequence, or is legally complicit. Each actor requires a separate contribution record.

## Harm / power lanes

### Electoral power concentration

Large-scale outside spending can materially alter the opportunity structure of congressional primaries. The harm audit should trace:

```text
donor
-> AIPAC / AIPAC PAC / UDP
-> candidate support or opposition
-> election outcome
-> office gained / lost
-> relevant votes / appropriations / arms policy
-> civilian consequence
```

The first three edges may be confirmed without assuming the later edges.

### Targeting critics of Israeli military policy

Confirmed cases requiring individual contribution records include:

- Jamaal Bowman — targeted by UDP/AIPAC in 2024; Bowman supported a permanent Gaza ceasefire and publicly accused Israel of genocide/ethnic cleansing;
- Cori Bush — AIPAC states UDP involvement helped defeat her after she became one of Congress's most outspoken critics of Israeli military conduct and an early ceasefire advocate;
- Abdul El-Sayed — in the 2026 Michigan Democratic Senate primary, AP reported AIPAC and affiliated groups spent close to $30 million backing Haley Stevens in an effort to defeat El-Sayed, who advocated ending U.S. military aid to Israel. El-Sayed nevertheless won.

The El-Sayed case is especially useful for the intent model:

```text
large attempted electoral intervention
-> CONFIRMED political intent / capability
-> intended candidate defeat did not occur
-> no false realized-outcome score
```

### Military aid and accountability policy

AIPAC publicly advocates U.S. military aid to Israel and political support for Israeli security policy. The harm audit must separately trace:

- appropriations promoted;
- arms-transfer votes;
- conditions or oversight opposed/supported;
- sanctions or accountability measures;
- ICC/ICJ-related policy;
- settlement/occupation policy;
- congressional letters and resolutions;
- candidate funding before/after relevant votes.

Funding is an influence lead, not proof of purchase.

## Required donor map

`PATH_FORWARD`:

- itemized AIPAC PAC donors;
- itemized UDP donors;
- repeat donors across election cycles;
- donors funding both pro-Israel and unrelated partisan causes;
- corporate/executive/foundation relationships where public;
- donor -> candidate / donor -> PAC / donor -> advocacy route separation;
- policy requests and known access;
- timing around arms votes, appropriations, sanctions, and accountability measures.

Do not infer ethnicity, religion, or collective identity from donor participation.

## Candidate-recipient audit rule

AIPAC support should trigger review, not automatic conviction.

For every recipient:

```text
amount / form of support
support source: AIPAC PAC | UDP | member bundling | other
candidate's Israel/Gaza position before support
candidate's position after support
arms / aid / sanctions / accountability votes
leadership or committee authority
public statements
material benefit to Israeli state/military policy
civilian-harm linkage
alternative explanations / contrary votes
```

A candidate who received AIPAC support but later opposed an arms transfer is not identical to one who repeatedly facilitated transfers after notice of civilian harm.

## Current investigation states

```text
AIPAC PAC and UDP large financial capacity:                 CONFIRMED
AIPAC/UDP intervention against Bowman and Bush:            CONFIRMED
AIPAC/affiliate major 2026 spending in Michigan primary:   CONFIRMED
AIPAC advocacy for large U.S. support package to Israel:   CONFIRMED
AIPAC money automatically purchases every recipient vote:  NOT CONFIRMED
AIPAC is controlled by Israeli government:                 PENDING / not established by these records
Every AIPAC-backed official legally complicit in genocide: case-specific / PENDING
```

## Sources

Primary / direct:
- FEC, AIPAC PAC, committee C00797670: https://www.fec.gov/data/committee/C00797670/
- FEC, United Democracy Project, committee C00799031: https://www.fec.gov/data/committee/C00799031/
- AIPAC, `United Democracy Project | Taking The Fight To Anti-Israel Candidates`: https://www.aipac.org/memos/policy-politics-congress-israel

Independent reporting:
- Reuters, New York race / AIPAC-UDP intervention against Jamaal Bowman, 2024-05-17: https://www.reuters.com/world/us/new-york-race-us-house-becomes-latest-israel-lobby-battleground-2024-05-17/
- Reuters, Democratic primary conflict over AIPAC, 2026-05-07: https://www.reuters.com/world/us/tensions-over-pro-israel-lobbying-group-highlight-rifts-democratic-primaries-2026-05-07/
- AP, AIPAC spending in Michigan Senate primary, 2026-07-19: https://apnews.com/article/588bb869eb557643950bf68d6a0d7a10

Genocide evidence anchors:
- Amnesty International, 2024-12-05: https://www.amnesty.org/en/documents/mde15/8668/2024/en/
- UN Independent International Commission of Inquiry, A/HRC/60/CRP.3, 2025-09-16: https://www.un.org/unispal/document/commission-of-inquiry-report-genocide-in-gaza-a-hrc-60-crp-3/

## Core locks

```text
AIPAC != Jewish people.
AIPAC != Judaism.
AIPAC != every Zionist current.
AIPAC != Israeli government.
Funding != automatic control.
Independent expenditure != direct candidate contribution.
Legal campaign spending != absence of democratic or human consequences.
Criticism of AIPAC or Israeli state policy != antisemitism by definition.
Antisemitism remains separately identifiable and investigable where evidence supports it.
```
