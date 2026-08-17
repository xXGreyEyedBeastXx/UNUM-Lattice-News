# Extensible Evidence Grammar v0.1

Status: ACTIVE METHODOLOGY
Date: 2026-08-17

## Root rule

**Grammar may expand and evolve. Evidentiary collapse is the worse failure.**

The lattice vocabulary is an instrument for preserving distinctions discovered in evidence. It is not a closed ontology and it must not force materially different relations, postures, mechanisms, or authority seats into an existing category merely to maintain schema stability.

```text
SCHEMA_COMPATIBILITY < PRESERVING_MATERIAL_DIFFERENCE
```

when the two genuinely conflict.

Compatibility should be preserved where it does not cost meaning. When it does, add a typed extension and record the reason.

## When grammar should expand

Add or refine a type when an existing type would collapse distinctions that change any of the following:

- identity or kinship;
- evidentiary posture;
- authority or responsibility;
- causal mechanism;
- intent or knowledge;
- temporal sequence;
- territorial effect;
- victim/affected-population seat;
- law versus observed conduct;
- stated justification versus operating procedure;
- local practice versus system-wide pattern;
- direct perpetration versus enabling, encouragement, omission, protection, or impunity;
- movement continuity versus legal-organizational identity;
- formal separation versus functional continuity;
- allegation versus independent finding versus adjudication;
- present effect versus projected trajectory;
- audience-specific framing versus direct contradiction;
- translation dispute versus policy reversal;
- system knowledge versus individual knowledge;
- model failure versus knowing preservation of a false/inadequate model;
- resource allocation versus stated priority;
- formal neutrality versus asymmetric coercive effect;
- internal review versus independent review;
- self-exoneration versus debunking;
- clue convergence versus proven intent.

## Extension pattern

New vocabulary should be typed and reversible rather than silently replacing older records.

```text
existing_type
  -> remains readable
  -> extension adds resolution
  -> old records can be migrated when useful
  -> no evidence is upgraded merely because a new type exists
```

Preferred extension record:

```yaml
grammar_extension:
  term: DELIBERATE_TARGETING_FINDING
  parent_family: EXTERNAL_FINDING
  reason: >-
    distinguish a competent investigative finding of deliberate targeting from
    raw allegation, observed death, ordinary supported inference, or final court judgment
  introduced: 2026-08-17
  migration: optional
```

## Conduct / effect / legal-finding extensions

- `STATED_JUSTIFICATION` — the actor's declared reason or legal/moral frame.
- `STATED_OBJECTIVE` — the actor directly states an intended outcome or policy goal; does not establish implementation.
- `FORMAL_POLICY` — enacted or formally directed policy.
- `LOCAL_ORDER` — documented order at unit, facility, checkpoint, zone, or commander level.
- `OPERATING_PROCEDURE` — repeated practice established as de facto or formal procedure.
- `OBSERVED_CONDUCT` — directly documented action without automatic intent inference.
- `DOCUMENTED_EFFECT` — death, injury, deprivation, displacement, destruction, territorial control, return obstruction, etc.
- `SYSTEMATIC_PATTERN` — repeated conduct established across sufficient incidents/locations/times.
- `LEADERSHIP_ENCOURAGEMENT` — competent evidence that leadership implicitly encouraged conduct.
- `LEADERSHIP_ORDER` — competent evidence of explicit leadership direction.
- `EXTERNAL_FACT_FINDING` — finding by a competent investigatory body, distinct from a court judgment.
- `LEGAL_ADVISORY_FINDING` — authoritative advisory legal determination, distinct from criminal adjudication.
- `DELIBERATE_TARGETING_FINDING` — competent finding that a protected civilian class/persons were deliberately targeted.
- `COLLECTIVE_PUNISHMENT_FINDING` — competent finding that collective punishment occurred.
- `TERRITORIAL_EFFECT` — persistent change in control, access, settlement, displacement, returnability or boundary practice.
- `DENIAL_OR_COUNTERPOSITION` — actor's direct denial or alternative account, preserved without automatic priority.
- `CROSS_THEATER_ANALOGUE` — similar transformation in a distinct legal/geographic theater; never automatic identity or common command.

## Audience / language / narrative-surface extensions

- `AUDIENCE_DIFFERENTIATED_FRAMING` — materially different framing supplied to different linguistic, domestic, diplomatic, electoral, coalition, or media audiences. Requires a recoverable comparison surface; does not itself prove deception.
- `MATERIAL_POLICY_PRESENTATION_DIVERGENCE` — paired or near-paired statements by the same authority on substantially the same policy object materially differ in the policy position presented. Stronger than tonal emphasis; still not automatic proof of deceptive intent.
- `TRANSLATION_DISPUTE` — lexical, semantic, or scope dispute in translation materially affects interpretation.
- `POST_HOC_CLARIFICATION` — later statement narrows, explains, or reframes an earlier statement; does not erase the earlier record.
- `POSITION_REVERSAL` — later stated position materially changes from an earlier one; motive remains separately typed.
- `DOMESTIC_COALITION_SIGNAL` — candidate relation where evidence supports messaging directed toward coalition/domestic political maintenance.
- `INTERNATIONAL_LEGITIMATION_SIGNAL` — candidate relation where evidence supports messaging directed toward international legal/diplomatic legitimacy.
- `DIPLOMATIC_PRESSURE_RESPONSE` — use only where a policy/message change is evidentially linked to diplomatic pressure; do not infer from timing alone.

Locks:

```text
DIFFERENT EMPHASIS != CONTRADICTION
CONTRADICTION != PROVEN DECEPTION
TRANSLATION DISPUTE != POLICY REVERSAL
HEBREW != TRUTH BY DEFAULT
ENGLISH != FALSE BY DEFAULT
LATER CLARIFICATION != ERASURE OF EARLIER SURFACE
SINGLE DOMESTIC STATEMENT != AUDIENCE DIFFERENTIATION without a comparison surface
```

## Identity / institutional-kinship extensions

- `PERSONNEL_PIPELINE` — recurring recruitment, assignment, transfer, or career movement from one institution into another.
- `DUAL_SEAT_SERVICE` — a person occupies materially consequential roles across institutions or periods, including reserve/compulsory service where evidenced.
- `INSTITUTIONAL_KINSHIP` — distinct institutions share evidenced personnel, recruitment, operational, command, funding, oversight, reserve, or joint-action relations.
- `FORMAL_SEPARATION` — legal/organizational distinction preserved as a fact; does not itself prove functional independence.
- `FUNCTIONAL_CONTINUITY` — distinct bodies perform a continuing causal/operational role across a formal organizational boundary.

Locks:

```text
INSTITUTIONALLY DISTINCT != PERSONNEL INDEPENDENT
PERSONNEL KINSHIP != IDENTICAL INSTITUTION
SHARED PERSONNEL != SHARED COMMAND IN EVERY EVENT
RELATION != CONTROL unless control is separately evidenced
```

## Accountability / internal-review extensions

- `INTERNAL_REVIEW` — review performed inside or under the same wider institutional/state system as the investigated actor.
- `INDEPENDENCE_CLAIM` — the reviewing institution's stated claim that it is professionally or structurally independent.
- `INDEPENDENCE_AUDIT` — explicit test of appointment/removal, staffing, budget, evidence access, personnel crossing, sanction capacity, retaliation protection, external review, and reach to senior leadership.
- `SELF_EXONERATION` — an internal review clears the actor, finds no wrongdoing, or materially narrows responsibility.
- `EXTERNAL_CONTRADICTION` — competent outside evidence materially contradicts an internal account or finding.
- `WATCHDOG_REMOVAL` — removal of oversight personnel or offices relevant to independence/correction capacity.
- `WATCHDOG_CAPACITY_LOSS` — material staffing, budget, evidence-access, jurisdictional, or enforcement degradation of an oversight body.
- `POLITICAL_INTERFERENCE_RISK` — supported risk that political/command dependence can affect investigative or enforcement independence; not itself proof of a dishonest result.
- `CORRECTION_FAILURE` — institution fails to reopen, correct, or materially respond after contrary evidence undermines an earlier account/finding.
- `ACCOUNTABILITY_CONSEQUENCE` — sanction, dismissal, prosecution, policy correction, restitution, reopening, or other observable consequence attributable to accountability process.
- `SELF_EXONERATION_CREDIBILITY_DECAY` — repeated weak-accountability self-clearance plus external contradiction/correction failure lowers the future exculpatory weight of similar internal findings without making all internal claims false.

Locks:

```text
SELF INVESTIGATION != INDEPENDENT REVIEW
SELF EXONERATION != DEBUNKING
FORMAL REVIEW MECHANISM != EFFECTIVE ACCOUNTABILITY
INTERNAL INDEPENDENCE CLAIM != EXTERNAL INDEPENDENCE FINDING
LOW TRUST != AUTOMATIC FALSITY
```

## Command / responsibility extensions

- `COMMAND_ALLOWANCE` — harmful conduct is knowingly tolerated, normalized, left uncorrected, or enabled within command authority without proof of a direct written order.
- `FAILURE_TO_PREVENT_OR_REPRESS` — competent evidence supports failure by an authority with relevant duty/capacity to prevent or repress subordinate harm.
- `FAILURE_TO_INVESTIGATE_EFFECTIVELY` — evidence supports materially inadequate investigation/correction despite duty and notice.
- `PROTECTION_OR_IMPUNITY` — evidence supports protective institutional behavior, non-enforcement, or impunity around harmful actors/conduct.
- `COMMAND_RESPONSIBILITY_FINDING` — court or competent legal body attributes superior responsibility at its exact evidentiary/legal standard.

Locks:

```text
NO RECOVERED DIRECT ORDER != NO SUPERIOR RESPONSIBILITY
COMMAND ALLOWANCE != DIRECT COMMAND
CHAIN OF COMMAND EXISTS != EVERY HARM ORDERED FROM THE TOP
LEGAL FINDING AT WARRANT/ADVISORY/COMMISSION STANDARD != FINAL CONVICTION unless it is one
```

## Resource-allocation / asymmetric-enforcement extensions

- `PROTECTION_ALLOCATION_ASYMMETRY` — scarce security/protective capacity is allocated unevenly across populations, events, territories, or political constituencies in a way that changes exposure to harm. Discriminatory intent is a separate question.
- `REVEALED_SECURITY_PRIORITY` — resource movement is evidence of what an institution treated as requiring protection/attention at that time; does not alone prove why.
- `ASYMMETRIC_COERCIVE_ENFORCEMENT` — a security institution formally manages conflict but allocates protection, movement freedom, force, detention, closure, or enforcement in a systematically unequal way that preserves one population's mobility/project while coercively constraining another.
- `PALESTINIAN_CIVIC_SPACE_RESTRICTED_FOR_SETTLER_SECURITY_FIELD` — scoped specimen relation for closures/movement restrictions imposed on Palestinian civic life in order to manage a settler/security field; not a universal relation outside evidenced cases.

Locks:

```text
RESOURCE ALLOCATION = BEHAVIORAL EVIDENCE
RESOURCE ALLOCATION != COMPLETE MOTIVE
ASYMMETRIC EFFECT != IDEOLOGICAL INTENT FOR EVERY OFFICER
REDEPLOYMENT INTO A SECURITY FIELD != PROOF OF EACH UNIT'S EXACT TASK
```

## Operational-narrative / clue extensions

These types preserve cases where a governing model is not merely rhetoric but changes material decisions.

- `REALITY_CONTRADICTED_MODEL` — a governing model materially conflicts with evidence available in the relevant period.
- `NARRATIVE_PERSISTENCE_AGAINST_CONTRARY_EVIDENCE` — the same model survives multiple independent contradictory clues without proportionate updating.
- `MODEL_PROTECTIVE_FILTERING` — contrary evidence is repeatedly downgraded, compartmentalized, normalized, or interpreted in ways that preserve the governing model.
- `NARRATIVE_ENABLED_RISK_NORMALIZATION` — the model makes a serious exposure appear administratively ordinary/manageable and thereby reduces protective action.
- `OPERATIONALIZED_NARRATIVE` — the model has observable downstream effects on troop/police deployment, event approval, protection, warning thresholds, evacuation, access policy, staffing, budget, or accountability.
- `KNOWINGLY_TOLERATED_VULNERABILITY` — candidate hypothesis requiring actor-specific evidence that relevant decision-makers understood a materially elevated risk and consciously maintained the vulnerable posture.
- `CALCULATED_EXPOSURE` — candidate hypothesis requiring evidence of conscious acceptance of a serious exposure while choosing competing priorities or maintaining the vulnerable condition; does not itself require desired deaths.
- `OPERATIONAL_PRETEXT` — use only where evidence supports that a stated model/justification was knowingly used to enable or legitimate conduct while materially contrary facts were understood.
- `SETUP_HYPOTHESIS` — clue-supported hypothesis that a condition may have been deliberately created or preserved to enable a desired downstream event.
- `CALCULATED_SACRIFICE` — strongest candidate in this family; requires evidence that decision-makers anticipated serious civilian death/capture risk and consciously accepted that harm as an instrumentally useful price or deliberately withheld protection for that purpose.

Required setup ladder:

```text
MISTAKE / MISREAD
-> REALITY_CONTRADICTED_MODEL
-> NARRATIVE_PERSISTENCE_AGAINST_CONTRARY_EVIDENCE
-> MODEL_PROTECTIVE_FILTERING
-> NARRATIVE_ENABLED_RISK_NORMALIZATION
-> OPERATIONALIZED_NARRATIVE
-> KNOWING PRESERVATION candidate
-> OPERATIONAL_PRETEXT candidate
-> SETUP_HYPOTHESIS
-> DELIBERATE SETUP finding only if knowledge + capacity + conscious preservation + desired/instrumental outcome are evidenced
```

Locks:

```text
FALSE_OR_INCOMPLETE_NARRATIVE != SETUP
NARRATIVE_PERSISTENCE != PROVEN DECEPTION
MODEL_PROTECTIVE_FILTERING != ABSENCE OF INFORMATION
OPERATIONALIZED_MODEL != MERE RHETORIC
COMMON_CAUSAL_SYSTEM != RANDOMLY INDEPENDENT EVENTS
NON_RANDOM_CAUSAL_RELATION != PROVEN DELIBERATE SETUP
FOREKNOWLEDGE + EXPOSURE != CALCULATED SACRIFICE
```

## Foreknowledge-resolution extensions

Do not use `foreknowledge` as one binary label. Preserve:

- `STRATEGIC_SCENARIO_FOREKNOWLEDGE` — knowledge that an actor had developed a broad attack/incursion concept.
- `OPERATIONAL_PLAN_FOREKNOWLEDGE` — possession of a detailed plan materially resembling the eventual operation.
- `CAPABILITY_SHIFT_WARNING` — evidence that the plan moved from aspiration toward practiced capability.
- `IMMINENT_OR_NEAR_TERM_ATTACK_WARNING` — evidence of near-term offensive risk.
- `EXACT_DATE_TIME_SCALE_FOREKNOWLEDGE` — knowledge of exact date/time/full scale; must never be inferred from the earlier rungs alone.

Locks:

```text
PLAN POSSESSION != CERTAINTY OF EXECUTION
DISCOUNTED WARNING != ABSENT WARNING
SYSTEM FOREKNOWLEDGE != IDENTICAL KNOWLEDGE FOR EVERY OFFICIAL
FOREKNOWLEDGE != EXACT DATE/TIME/SCALE KNOWLEDGE
```

## Relation to existing grammar

The existing `source -> story -> node -> relation -> contribution -> spread -> rendition` architecture remains useful. These extensions increase the resolution *inside* those objects. They do not crown a replacement ontology.

The owning methodology surfaces for later extensions include:

- `docs/STATED_JUSTIFICATION_VS_OBSERVED_CONDUCT_v0_1.md`
- `docs/SELF_INVESTIGATION_INDEPENDENCE_AND_ACCOUNTABILITY_v0_1.md`
- `docs/OPERATIONAL_NARRATIVE_AS_EVIDENCE_v0_1.md`
- `docs/CLUE_RETENTION_AND_NONCOMPRESSION_v0_1.md`

If future evidence requires more resolution, extend again.

## Re-entry rule

When a later analyst encounters a relation that does not fit:

1. do not choose the nearest existing label by habit;
2. state what difference would be lost;
3. search for an existing equivalent or historical term;
4. if none preserves the distinction, add a typed extension;
5. record its parent family, reason, scope and migration implications;
6. leave older evidence intact unless a deliberate migration improves legibility without changing posture;
7. if the new type is introduced in a specialist investigation, propagate it back to this registry or explicitly link the owning grammar surface so it does not become a hidden one-off type.

## Retention lock

A grammar entry may be compact, but the evidence that supports a use of that type must retain or point to:

- date/time;
- actor/seat;
- clue identity;
- source posture;
- claim posture;
- actual relation;
- operational consequence;
- strongest counter-reading;
- missing discriminator;
- owning recovery surface.

```text
THE TYPE MAY BE SHORT.
THE EVIDENCE THAT MAKES THE TYPE TESTABLE MAY NOT BE.
```

**The lattice is allowed to learn new grammar. It is not allowed to gain neatness by losing reality.**
