# Harm Hierarchy Legibility Adversarial Audit v0.1

Status: active review / architecture refactor  
Updated: 2026-08-21

## Purpose

UNUM-Lattice-News will maintain a harm-first investigative surface that makes concentrated power, civilian harm, and responsibility legible without requiring a net-moral biography of the actor under review.

The audit is intentionally adversarial toward power. Its search posture is:

> Treat every consequential exercise of concentrated public, military, police, corporate, or institutional power as requiring proof, trace the harmed population first, and aggressively test the strongest negative account supported by the record.

This is not a presumption that every investigated person or institution is legally guilty of a crime. `criminal`, `crime`, `war crime`, `corruption`, and similar terms remain legal/evidentiary conclusions that require their own elements and proof.

The investigation may be adversarial without making the conclusion predetermined.

## Core direction

```text
HARMED PERSON / POPULATION / ECOLOGY
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

Follow the chain as far backward and outward as evidence permits.

Do not stop at the last actor who physically implemented the harm when upstream authority, funding, procurement, policy, lobbying, command, legal protection, institutional obstruction, political normalization, intentional term-setting, or cost externalization is independently evidenced.

## Negative-only audit rule

A harm audit is not a net-goodness score.

A beneficial act does not subtract from a documented harm.

```text
humanitarian action != offset for unrelated killing
beneficial program != erasure of rights deprivation
good policy elsewhere != discount on detention death
charity != credit against coercion
```

Counterevidence remains mandatory only when it materially bears on the claim being tested: attribution, scope, causation, chronology, magnitude, mechanism, identity, motive, knowledge, or evidentiary reliability.

Do not pad a harm record with unrelated accomplishments for balance.

## Four investigation states

Every consequential claim or contribution under adversarial review must carry one of four investigation states.

### PENDING

The claim remains unresolved.

Use when:
- investigation is incomplete;
- evidence conflicts materially;
- required records are unavailable, sealed, delayed, or missing;
- causation or attribution is not sufficiently established;
- the current evidence does not justify confirmation or debunking.

`PENDING` is the default unresolved state.

### PATH_FORWARD

A concrete evidentiary route exists but has not yet been completed.

A path-forward record should identify the next recoverable objects, for example:

```text
named statute or executive order
contract / procurement award
appropriation or transfer record
court file
casualty or medical record
inspection report
campaign-finance record
lobbying disclosure
command chronology
agency memo
named witness or testimony
corporate filing
internal or public notice chronology
historical comparison set
```

`PATH_FORWARD` means the investigation knows what to look for. It does not mean the allegation is probably true.

### CONFIRMED

The scoped claim is sufficiently established for the repository's evidentiary standard.

Confirmation must preserve exactly what is confirmed:
- actor;
- conduct;
- mechanism;
- date or period;
- affected population or system;
- direct effect or supported downstream consequence;
- attribution grade;
- source lineage and limitations.

A broad accusation may contain narrower confirmed components without the entire accusation being confirmed.

### DEBUNKED

`DEBUNKED` is a high-burden finding, not a synonym for `not proven`.

Before marking a claim debunked, the record must contain a debunking explanation with at least:

1. the claim as fairly reconstructed;
2. the strongest available version of the supporting case;
3. the evidence that should exist if the claim were true, where applicable;
4. the relevant evidence actually recovered;
5. the decisive contradiction, impossibility, identity error, chronology failure, falsified source, or other failure;
6. why that failure defeats the scoped claim;
7. any narrower residual claim that remains pending or confirmed.

```text
SEARCHED_NOT_FOUND != DEBUNKED
NOT_SEARCHED != DEBUNKED
authority denial != DEBUNKED
lack of prosecution != DEBUNKED
court dismissal on procedure != factual DEBUNKING
one false detail != automatic debunking of every related claim
```

## Claim posture and investigation state are separate

The existing evidentiary posture remains useful:

```text
observed
stated
adjudicated
supported_inference
alleged
disputed
ambiguous
unknown
```

Do not collapse it into the four investigation states.

Example:

```yaml
investigation_state: CONFIRMED
claim_posture: stated
claim: "The president publicly ordered the agency to pursue X."
```

The statement is confirmed as a statement; the truth of the statement's content may remain pending.

## Harm rating architecture

The harm hierarchy exists for legibility, not to hide complexity inside one number.

Every scored contribution therefore carries a **harm vector**, sortable harm scores, and—where independently established—a separate harmful-intent / trajectory axis.

### Harm vector

Score each dimension from `0` to `5`, with written justification and source anchors.

```text
lethal_physical_harm          death, injury, torture, medical neglect, bodily danger
confinement_coercion          detention, forced displacement, coercive institutionalization, labor under custody
material_deprivation          food, healthcare, housing, income, benefits, property, essential services
rights_agency_harm            bodily autonomy, speech, due process, voting, labor, family, identity, refusal, exit
land_sovereignty_displacement land seizure, Indigenous sovereignty, sacred sites, forced migration, occupation
ecological_future_harm        pollution, habitat loss, climate/material degradation, future-generation burden
democratic_epistemic_harm     oversight destruction, retaliation, evidence control, politicized justice, censorship/propaganda mechanisms
power_concentration           increased coercive, surveillance, military, police, executive, carceral, monopoly, or essential-system chokepoint capacity
catastrophic_risk_imposition  nuclear, mass-casualty, systemic-war, ecological-collapse, or other extreme-tail risk imposed on civilians
```

A zero means no currently supported harm in that dimension for the scoped contribution; it does not mean the actor is harmless generally.

### Propagation dimensions

Also score:

```text
reach            number / breadth of people or ecologies exposed
duration         persistence over time
irreversibility  difficulty of restoring the prior state
vulnerability    reduced exit, bargaining power, legal protection, physical safety, or political voice of those harmed
```

### Attribution grade

Use the repository responsibility scale:

```text
R0 adjacency
R1 rhetorical support / normalization
R2 vote / endorsement / formal support
R3 sponsorship / funding / material facilitation
R4 leadership / decisive enabling / command responsibility
R5 direct operational control
```

R0 contributes no actor harm score by itself. Adjacency is a lead, not harm attribution.

### Four public axes, not one hidden scalar

Each confirmed contribution may expose:

1. **Realized Harm Score (RHS)** — confirmed realized human/material/rights/land/ecological/democratic harm attributable to the actor.
2. **Structural Harm Score (SHS)** — confirmed expansion of concentrated coercive or unaccountable power, even where the full downstream injury has not yet occurred.
3. **Catastrophic Risk Score (CRS)** — supported extreme-tail risk imposed by the action; kept separate so forecast risk is not numerically confused with realized deaths.
4. **Harmful Intent / Trajectory Score (HIS)** — confirmed evidenced harmful objective, attempted harmful action, preparation, persistence, or operational trajectory as defined in `docs/HARMFUL_INTENT_AND_TRAJECTORY_MODEL_v0_1.md`.

The public harm rating is the tuple:

```text
HR = [RHS, SHS, CRS, HIS]
```

`HIS` does not convert rhetoric into realized harm. It preserves direction and attempted harmful action so a blocked attempt does not disappear from the actor's trajectory.

Intentional action or term-setting that is not itself evidence of a harmful endpoint may still be recorded in the contribution's accountability state without automatically increasing `HIS`. Intent to capture value, reduce cost, or preserve capacity and intent to cause a downstream deprivation are separate claims.

### Power-conditioned knowledge and persistence

Where responsibility depends on what an actor knew or reasonably could know, preserve:

```text
knowledge state
capacity to know
foreseeability
credible notice
capacity to correct
response after notice
gain or insulation retained after notice
repair or mitigation
```

Greater power does not prove knowledge or guilt. It may increase the actor's practical capacity to investigate, model, receive warning, correct, and repair.

```text
capacity to know != actual knowledge
foreseeability != desire
absence of harmful-endpoint intent != absence of accountability
credible notice + capacity to correct + persistence = accountability evidence, not automatic proof of secret motive
```

See `docs/HARMFUL_INTENT_AND_TRAJECTORY_MODEL_v0_1.md` and `nodes/harm-domination-protection-weighting.yaml`.

### Contribution scoring

For hierarchy purposes, only `CONFIRMED` contribution records may add to the confirmed harm totals or confirmed intent/trajectory axis.

`PENDING` and `PATH_FORWARD` may appear in an exposed-risk or accountability appendix but do not count as confirmed realized harm or confirmed intent.

`DEBUNKED` claims contribute zero and retain their explanatory record.

Actor attribution must be weighted by the responsibility grade so the same downstream event is not counted identically against a direct operator and a merely adjacent actor.

Recommended attribution multipliers for sortable internal scoring:

```text
R0 = 0.00
R1 = 0.15
R2 = 0.35
R3 = 0.60
R4 = 0.85
R5 = 1.00
```

These multipliers are audit conveniences, not claims of legal liability.

### No double counting

The same harm may have multiple contributors.

Do not duplicate the victim count into every actor's score as though each independently caused a separate death or deprivation.

Instead preserve:

```text
shared_harm_id
underlying_harm_magnitude
contributor-specific responsibility grade
contributor-specific mechanism
```

A hierarchy may show that several actors materially contributed to the same harm without multiplying the underlying casualty or deprivation count.

## Three separate hierarchies

Maintain separate ranking surfaces for:

### Institution hierarchy
Governments, departments, agencies, militaries, police systems, corporations, parties, advocacy institutions, courts, and other organized power-bearing bodies.

### Leader hierarchy
Heads of government, presidents, prime ministers, cabinet officials, governors, military commanders, corporate executives, movement leaders, and other named authority-bearing persons.

### Non-leader actor hierarchy
Contractors, donors, lobbyists, intermediaries, operational actors, organizations, networks, and other entities that materially contribute without occupying the leader seat used above.

Do not force unlike categories into one leaderboard when category differences destroy legibility.

## Time windows and historical depth

Every hierarchy must declare its time window.

Examples:

```text
current administration term
calendar year
war period
full public career
institutional history since founding
specific historical era
```

Current harm and historical harm may be displayed together, but they must remain separable.

Historical priors inform investigation and risk. They do not automatically add old harms to a current-term score unless the chosen time window includes them.

## Power-first rule

The audit treats concentration of coercive power as a harm dimension in its own right.

Examples include:
- expansion of military or police authority;
- reduced judicial or inspector oversight;
- detention capacity expansion;
- surveillance expansion;
- executive control over formerly independent processes;
- erosion of collective bargaining or organized counterpower;
- concentration of private chokepoint power over essential systems.

A claimed security or efficiency benefit does not erase the power-concentration score.

## Civilian-first rule

When a policy creates both institutional capability and civilian consequence, the audit begins with the person or population bearing the downside.

Questions:

1. Who died, was injured, detained, dispossessed, impoverished, displaced, silenced, surveilled, excluded, or stripped of protection?
2. What exactly was lost?
3. What mechanism produced the loss?
4. Who implemented it?
5. Who authorized it or intentionally set the consequential terms?
6. Who funded or materially enabled it?
7. What did the relevant actors know, reasonably have capacity to know, or receive credible notice of?
8. Who could correct or repair the mechanism, and what happened after notice?
9. Who protected the mechanism from accountability?
10. Who profited, avoided cost, or gained authority?
11. What evidence establishes each edge?
12. What claim remains pending, has a path forward, is confirmed, or is actually debunked?

## Symmetry rule

The audit does not become less adversarial because the actor belongs to a preferred party, movement, government, ideology, ethnicity, religion, or alliance.

```text
Republican != exemption
Democrat != exemption
ally != exemption
opponent != automatic guilt
victimhood in one relation != immunity in another
```

The stable object of concern is the harmed person, population, ecology, or democratic capacity.

## Publication lock

A high harm rating means:

> Within the declared time window and evidence set, the actor has a larger amount of confirmed attributable harm, structural/catastrophic risk, and/or evidenced harmful intent/trajectory according to the published rubric.

It does **not** mean:
- the actor is legally a criminal absent the required legal showing;
- every allegation about the actor is true;
- every person associated with the actor shares responsibility;
- violence or punishment against the actor is justified;
- lower-ranked actors are harmless.

The audit is an accountability and legibility instrument, not a punishment engine.
