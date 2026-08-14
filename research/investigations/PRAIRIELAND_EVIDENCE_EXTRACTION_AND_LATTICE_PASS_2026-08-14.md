# Prairieland Evidence Extraction and Lattice Pass — 2026-08-14

```yaml
status: ACTIVE_INVESTIGATION
class: EVIDENCE_EXTRACTION_AND_LATTICE_PASS
as_of: 2026-08-14
verdict: none
primary_new_source: ICE FOIA 2018-ICFO-45499 responsive spreadsheet
source_bundle: sources/source-prairieland-detention-evidence-2017-2026.yaml
lattice: lattice/PRAIRIELAND_ICE_DETENTION_EVIDENCE_LATTICE_2026-08-14.yaml
```

## Investigation rule

This pass is a journal, not a verdict.

The working obligation is:

```text
lead
-> source provenance
-> exact record
-> actor / authority seat
-> physical conduct
-> institutional classification
-> evidence custody
-> counterevidence
-> missingness
-> next discriminator
```

Do not collapse:

```text
allegation -> finding
Closed -> cleared
facility -> operator -> ICE -> DHS -> White House
protest -> nighttime event -> shooter
anti-fascist -> Antifa -> formal organization -> criminal conspiracy
firework -> bomb
conviction on one count -> guilt on another
missing evidence -> affirmative proof
```

---

## I. What changed when the actual FOIA spreadsheet became available

Before extraction, the Prairieland sexual-abuse branch could only be described as an open lead based on PREA/oversight history and broader ICE records.

ICE FOIA `2018-ICFO-45499` materially changes that posture.

The spreadsheet itself records **explicit staff-on-detainee sexual-assault allegations at Prairieland**.

### A. June 2017 — unnamed contract officer

Spreadsheet index `365`:

```text
Incident: 15-JUN-17
Reported: 17-JUN-17
Facility: PRAIRIELAND DETENTION FACILITY - TX - IGSA
Case Type: Investigation IG
Class: Criminal
Status: Closed
Subject Type: ICE Contractors and Employees
Primary FD: 0612 Detainee/Alien - Sexual Assault (Staff on Detainee)
```

Narrative substance:

> A detainee alleged sexual assault by an unnamed contract officer at Prairieland.

Posture:

```yaml
allegation_exists_in_ICE_record: DOCUMENTED
sexual_assault_occurred: ALLEGED
actor_identity: REDACTED/UNKNOWN
investigative_disposition: MISSING_FROM_SPREADSHEET
meaning_of_closed: ADMINISTRATIVE_STATUS_ONLY
```

### B. December 2017 — male LaSalle guard

Spreadsheet index `95`:

```text
Incident: 11-DEC-17
Facility: PRAIRIELAND DETENTION FACILITY - TX - IGSA
Case Type: Management Inquiry
Class: Non-Criminal (S)
Status: Closed
Primary FD: 0612 Detainee/Alien - Sexual Assault (Staff on Detainee)
```

Case Summary / Synopsis substance:

> A detainee alleged that a male LaSalle detention officer / contract guard groped him during a pat-down.

But the `Topic` field describes inappropriate touching by another detainee.

Therefore the row contains an internal actor-classification conflict:

```text
Topic field
-> another detainee

Case Summary / Synopsis
-> contract detention officer / male LaSalle officer

Primary FD
-> Staff on Detainee
```

Posture:

```yaml
metadata_conflict: DOCUMENTED
staff_allegation_exists: DOCUMENTED
underlying_assault: ALLEGED
final_disposition: UNKNOWN
```

This is not trivia. Any aggregate analysis that groups allegations only through the `Topic` field can misclassify this event.

---

## II. Minimum current Prairieland allegation cluster

Current direct extraction has surfaced at least these Prairieland-linked entries:

```text
2017-03-02 -> detainee-on-detainee sexual assault allegation
2017-06-15 -> unnamed contract officer sexual-assault allegation
2017-07-18 -> detainee alleged sexual assault while sleeping
2017-11     -> detainee-on-detainee harassment / sexual advances record surfaced in extraction
2017-12-11 -> male LaSalle guard groping allegation during pat-down
2018-01-31 -> detainee-on-detainee sexual-assault allegation
2018-03-21 -> unknown detainee allegedly touched chest/buttocks
2018-03-23 -> detainee alleged another detainee touched her inappropriately
```

This is a **minimum**, not a final count.

A previous conversational pass described nine Prairieland-linked records. This journal does **not** preserve that number as canonical until the ninth distinct row is recovered from the workbook and its facility/narrative identity is reconciled.

That correction is intentional:

```text
remembered count
!=
reconstructed source count
```

The current lattice therefore says **multiple / at least eight directly surfaced in the present extraction**, including **two explicit staff-on-detainee allegations**, rather than manufacturing certainty around the larger number.

---

## III. The disposition gap

Every surfaced row can say `Closed` while telling us almost nothing about the investigative outcome.

The spreadsheet does not currently expose a reliable field equivalent to:

```text
substantiated
unsubstantiated
unfounded
criminally referred
prosecution declined
employee disciplined
employee terminated
employee reassigned
victim recanted
insufficient evidence
PREA administrative finding
```

Therefore:

```text
Closed
!=
cleared
```

and:

```text
Closed
!=
substantiated
```

The underlying investigative case file is the next evidentiary layer.

---

## IV. Prairieland is also an evidence-custody node

The 2018 death of Gourgen Mirimanian connects Prairieland to a separate evidence-integrity problem.

Records-based oversight reporting says:

- Mirimanian died at Prairieland on April 10, 2018;
- LaSalle Corrections operated the facility;
- some available dorm surveillance was of limited value because of distance;
- another video was not retained;
- internal reviewers complained that the missing recordings impaired witness-list preparation and review.

This does not prove concealment.

It does establish:

```text
expected evidence
-> incomplete retention
-> impaired later review
```

That changes how much exculpatory weight can responsibly be placed on a later absence of corroborating evidence.

Use:

```text
DOCUMENTED FAILURE OF EVIDENCE PRESERVATION
-> REDUCED EXCULPATORY VALUE OF ABSENCE
```

Do not use:

```text
MISSING EVIDENCE
-> ALLEGATION TRUE
```

---

## V. The private-contractor crossing

Prairieland should not be modeled as one institutional actor.

Minimum seats:

```text
DHS
-> ICE
-> ERO / JIC / OPR / ODO
-> public/private contracting interface
-> LaSalle Corrections
-> Prairieland facility management
-> individual detention officers / medical staff / subcontractors
-> detained people
```

The same ecology can potentially occupy several functions:

```text
custody
care
employment
complaint intake
surveillance control
record retention
internal investigation
inspection
contract renewal
```

The concentration of those functions is an **epistemic chokepoint candidate**.

It is not proof of conspiracy.

The next question is whether independent external seats had enough access and authority to preserve evidence and test internal findings.

---

## VI. The 2025 humanitarian antecedent

Independent reporting before July 4 documented:

```text
Prairieland female holding unit full
-> women sleeping on thin mats on concrete
```

and a former detainee alleged:

```text
denied antibiotics for ear infection
+
denied telephone access
```

The national ICE detention population was expanding rapidly during the same period.

Therefore the July protest did not occur against an empty humanitarian background.

Correct causal posture:

```text
documented detention grievance
-> plausible / supported protest motive context
```

Not:

```text
detention grievance
-> violence justified
```

---

## VII. Day protest, night event, and nested intent

DOJ's own later trial summary distinguishes a peaceful daytime protest from the nighttime event.

It also says some planning occurred in smaller trusted chats and reports cooperating-witness testimony that Song proposed freeing detainees and bringing rifles at a pre-event gear check.

The jury later convicted Song alone on the attempted-murder/firearm counts summarized by DOJ while convicting other defendants on common riot/material-support/fireworks counts.

The correct research object is therefore not:

```text
THE GROUP HAD ONE MIND
```

but:

```text
broad protest layer
superset
armed/self-defense social layer?
superset
trusted planning layer?
superset
Song's own intent?
```

Every `?` requires participant-level evidence.

The verdict is a partial discriminator, not total resolution:

```text
Song-alone attempted-murder conviction
-> legally consequential conduct distinction
```

while:

```text
common-count convictions
-> jury found additional criminal participation by other defendants
```

Both must remain visible.

---

## VIII. Fireworks and lexical inflation

DOJ's public verdict/sentencing account explicitly describes the physical objects as **fireworks**, while also referring to them as explosives for the charged offenses.

Therefore public/research language should preserve both levels:

```text
physical object: fireworks
legal charge/classifier: explosive(s)
```

Avoid:

```text
explosives
-> reader imagines bombs / IEDs / dynamite
```

unless an independent record establishes such devices.

The legal consequence can still be severe; the physical description must remain accurate.

---

## IX. Post-event classifier sequence

Timeline:

```text
2025-07-04
Prairieland violence

2025-07-09 / 07-16
DOJ public complaint/arrest releases describe organized attack and Song
but do not use North Texas Antifa Cell in the headline/public framing inspected here

2025-09-22
Trump order designates Antifa a domestic terrorist organization

2025-09-25
NSPM-7 creates broader domestic-political-violence network strategy and explicitly uses anti-fascism as a classifier/indicator in administration framing

2025-11-14
DOJ indictment announcement publicly calls defendants North Texas Antifa Cell operatives

2026-06-23
DOJ sentencing release explicitly highlights that these were the first Antifa-affiliated sentencings after Trump's September executive order
```

What this establishes:

```text
temporal sequence: DOCUMENTED
later DOJ rhetorical linkage to executive order: DOCUMENTED
```

What this does not establish:

```text
executive order caused charges
executive order caused verdict
executive order caused sentence
North Texas Antifa Cell was invented after the order
```

Those are candidate questions requiring internal prosecution chronology, charging memoranda, jury instructions, and sentencing calculations.

---

## X. First high-centrality lattice pattern

The strongest current connection is not a single allegation.

It is the repeated relation:

```text
PUBLIC AUTHORITY
-> PRIVATE CUSTODY CONTRACT
-> CAPTIVE / LOW-EXIT POPULATION
-> ALLEGED OR DOCUMENTED HARM
-> COMPLAINT ENTERS SYSTEM CONTROLLED OR MEDIATED BY CUSTODY ECOLOGY
-> EVIDENCE RETENTION / CLASSIFICATION / INVESTIGATION
-> PUBLIC FINDING OR ABSENCE OF FINDING
```

Then in 2025:

```text
DETENTION EXPANSION / CAPACITY PRESSURE
-> DOCUMENTED HUMANITARIAN GRIEVANCE
-> PROTEST
-> MIXED / NESTED INTENT QUESTION
-> VIOLENT ESCALATION
-> TERRORISM / ANTIFA CLASSIFIER
-> NETWORK-LEVEL INVESTIGATION AND VERY HIGH SENTENCING EXPOSURE
```

This is not one conspiracy line.

It is a **transformation chain in which control changes seats**.

Every crossing needs its own source and discriminator.

---

## XI. Immediate next work

1. Re-scan the full ICE spreadsheet through narrative text, not only structured facility/actor fields.
2. Resolve the current minimum allegation count and recover any Prairieland rows hidden by metadata errors.
3. Obtain the investigative case files behind indexes `365` and `95`.
4. Obtain full 2018/2021/2023 Prairieland PREA audits and corrective-action records.
5. Reconstruct LaSalle's Prairieland contract, staffing, medical subcontractors, surveillance obligations, penalties, renewals, and revenue.
6. Pull the Mirimanian death-review evidence chain at source-page level.
7. Quantify Prairieland capacity, staffing, medical load, transfers, and detention expansion through July 2025.
8. Recover protest-organizer material showing what specific detention conditions motivated the July 4 action.
9. Build defendant-by-defendant chat / conduct / knowledge / verdict / sentence cards.
10. Retrieve jury instructions, trial transcript, sentencing memoranda, guideline calculations, and appeals.
11. Trace the earliest internal use of `North Texas Antifa Cell` before and after the September 2025 executive policy.
12. Compare classifier/enforcement treatment symmetrically against far-right political-violence networks without collapsing distinct organizations.

---

## Status at re-entry

```yaml
Prairieland_staff_sexual_assault_allegations_exist_in_ICE_records: DOCUMENTED
Prairieland_staff_assaults_substantiated: UNKNOWN
Prairieland_rape_specifically_established: NO
Prairieland_rape_specifically_disproven: NO
FOIA_metadata_integrity_problem: DOCUMENTED
Mirimanian_video_preservation_failure: SUPPORTED_BY_RECORDS_BASED_OVERSIGHT
2025_humanitarian_grievance: SUPPORTED
Song_attempted_murder: ADJUDICATED
common_criminal_counts_for_other_trial_defendants: ADJUDICATED
one_formal_North_Texas_Antifa_organization: DISPUTED / REQUIRES_INDEPENDENT_TRACE
post_event_executive_classifier_sequence: DOCUMENTED
classifier_caused_prosecution_or_sentence: UNKNOWN
nested_intent: LIVE_CANDIDATE
```

No verdict. Continue tracing.
