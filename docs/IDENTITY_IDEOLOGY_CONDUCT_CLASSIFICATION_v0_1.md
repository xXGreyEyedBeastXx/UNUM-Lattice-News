# Identity, Ideology, Organization, Conduct, and Sponsorship Classification v0.1

Status: active review
Analyst seat: Vella Cora — News Analyst
Purpose: prevent identity categories from collapsing into ideology, conduct, threat, or guilt.

## Core rule

```text
IDENTITY != IDEOLOGY != ORGANIZATION != ROLE != TACTIC != SPONSORSHIP != EVIDENTIARY STATUS
```

This primitive applies across religions, political movements, states, insurgencies, militias, parties, governments, and other organized actors.

It is designed to prevent category errors such as:

```text
Muslim -> Islamist -> jihadist -> insurgent -> terrorist
Christian -> Christian nationalist -> extremist -> violent actor
Jewish -> Zionist -> Israeli state actor
state military -> lawful conduct
insurgent -> terrorist
protester -> extremist
```

None of these arrows may be assumed.

## 1. Identity layer

Identity describes what a person or group identifies as or belongs to.

Examples:

```text
Muslim
Christian
Jewish
Hindu
Buddhist
atheist
national identity
ethnic identity
political party membership
```

Identity alone does not establish ideology, political program, conduct, threat, or responsibility.

## 2. Ideology / political orientation layer

Record the specific worldview or political program when evidence supports it.

Examples:

```text
Islamist
Christian nationalist
Jewish nationalist
Hindu nationalist
secular nationalist
jihadist
white nationalist
authoritarian
revolutionary
separatist
socialist
liberal
conservative
```

Ideology should be defined operationally and sourced where possible.

Holding an ideology does not by itself establish participation in violence or crime.

## 3. Organization layer

Classify the actual organizational form separately.

Examples:

```text
religious institution
political party
advocacy group
movement
militia
armed group
insurgent organization
terrorist-designated organization
state military
police service
intelligence service
proxy force
civilian organization
corporation
```

Designation by a government is evidence of a legal or political classification, not metaphysical proof of conduct. Preserve who designated the organization, under what authority, when, and whether the designation is disputed.

## 4. Role layer

Role is contextual and may change by event.

Examples:

```text
civilian
combatant
commander
political leader
religious leader
protester
journalist
medic
humanitarian worker
hostage
prisoner
detainee
insurgent
state official
contractor
```

Role does not totalize identity.

## 5. Tactic / conduct layer

Classify observed or alleged conduct separately from identity and organization.

Examples:

```text
peaceful protest
civil disobedience
propaganda
political intimidation
guerrilla warfare
conventional warfare
terrorism
hostage-taking
indiscriminate attack
targeted killing
torture
collective punishment
forced displacement
ethnic cleansing
genocide
mass detention
assassination
sabotage
cyberattack
```

Where legal definitions differ, preserve the definition, jurisdiction, and evidentiary posture rather than forcing one label.

## 6. Sponsorship / authority layer

Record how the actor is empowered.

```text
independent_non_state
community_supported
private_funded
foreign_funded
state_tolerated
state_supported
state_sponsored_proxy
state_directed
state_actor
unknown
```

State sponsorship must not be inferred merely from ideological alignment or geographic proximity.

State actors do not receive a presumption of innocence for conduct merely because violence was legally authorized domestically.

## 7. Terrorism and insurgency distinction

Insurgency is an organizational/conflict role: an organized challenge to an established government, occupying authority, or political order, often using armed force.

Terrorism is a tactic or strategy classification centered on violence or threats intended to intimidate or coerce a broader audience for political or ideological ends, commonly involving civilians or other protected persons depending on the governing definition.

Therefore:

```text
INSURGENCY != TERRORISM
ARMED_RESISTANCE != TERRORISM
STATE_FORCE != LAWFUL_CONDUCT
TERRORIST_DESIGNATION != PROOF_OF_EVERY_ALLEGED_ACT
```

An insurgent organization may employ terrorist tactics, may avoid them, or may contain factions with different conduct.

## 8. State-sponsored terrorism and state terror

Keep at least two separate categories:

### State-sponsored terrorism

A state materially supports, directs, funds, arms, trains, shelters, or otherwise enables a non-state actor that employs terrorist tactics.

### State terror / government terror

A state or state organ itself uses terrorizing violence or coercion against civilian or political populations as an instrument of rule, occupation, punishment, intimidation, or policy.

Possible conduct includes torture, enforced disappearance, collective punishment, indiscriminate attack, terror campaigns, political assassination, mass intimidation, or comparable acts when evidence supports the classification.

Do not use statehood to sanitize conduct. Do not use the terrorism label to erase the legal distinctions between war crimes, crimes against humanity, genocide, repression, insurgency, and other categories.

## 9. Religious-nationalist application

For Christianity-related political analysis, keep these separate:

```text
Christian identity
Christian theological tradition
Christian political advocacy
Christian nationalism
Christian nationalist organization
Christian nationalist rhetoric
support for coercive policy
support for political violence
participation in violence
```

Do not infer the later categories from the earlier ones.

The same structure applies to Islam, Judaism, Hinduism, Buddhism, atheism, secular nationalism, and other identities or ideologies.

## 10. Evidentiary status

Every consequential classification carries its own posture:

```text
observed
stated
self_identified
supported_inference
alleged
disputed
adjudicated
unknown
missing_or_withheld
```

Classification may change as evidence changes. Preserve correction and re-entry.

## 11. Threat interaction

Threat assessment occurs after classification, not before.

Threat should evaluate capability, expressed direction, trajectory, constraint erosion, reach, vulnerability of targets, irreversibility, opacity, repetition, escalation potential, repair capacity, and immediacy.

Do not translate religious, ethnic, national, or ideological identity directly into threat score.

## 12. Query sequence

When encountering a potentially extremist, insurgent, terrorist, militant, or state-violence claim, ask in order:

1. Who or what is the actor?
2. What identity labels are relevant, and which are merely projected by others?
3. What ideology or political program is evidenced?
4. What organizational form exists?
5. What role did the actor occupy in the event?
6. What specific conduct is alleged or documented?
7. Who funded, armed, directed, protected, tolerated, or constrained the actor?
8. What legal or political designations exist, and who issued them?
9. What evidence supports and contradicts each classification?
10. What remains unknown?
11. What threat follows from the evidenced conduct and capability rather than from identity?

## 13. Parent ideology, subtype, and outlier scope

Classification must preserve the relationship between a parent ideology and its internal currents without allowing either collapse or false separation.

```text
SELF_IDENTIFIES_AS(X) != REPRESENTATIVE_INSTANTIATION_OF(X)
SUBTYPE_OF(X) != ABSENCE_OF_PARENT_IDEOLOGY(X)
OUTLIER_WITHIN(X) != COUNTEREVIDENCE_TO_PARENT_INVARIANT(X)
EXISTS_WITHIN_MOVEMENT != REPRESENTS_MOVEMENT
```

A branch or subtype can represent a genuine difference in tactics, institutions, theology, economics, borders, or desired outcomes. Those differences should be recorded. They must not be used automatically to erase parent commitments that remain evidenced.

Likewise, a reformer, dissident, humane participant, or internal opposition figure may demonstrate that contestation exists without demonstrating that the movement as a whole shares that person's program.

When an example substantially departs from the dominant or institutional program, record whether the person or faction is mainstream, minority, dissident, opposition, outlier, or unresolved in the relevant period. State explicitly whether the example is being used to demonstrate internal contestation or representativeness.

Do not use representative-exception substitution:

```text
one reformist/outlier actor retains movement label
-> actor rejects or softens a parent commitment
-> INVALID: parent movement therefore lacks that commitment
```

A self-applied ideological label is evidence of claimed identity. The actor's actual program determines what they instantiate.

For the current Zionism specimen and Martin Buber scope correction, see:

- `docs/IDEOLOGY_PARENT_INVARIANT_AND_OUTLIER_SCOPE_v0_1.md`
- `sources/source-zionism-parent-ideology-and-buber-scope-2026-08-17.yaml`
- `nodes/zionism.yaml`

## Core locks

```text
Identity is not tactic.
Ideology is not conduct.
Insurgency is not terrorism.
Statehood is not innocence.
Designation is not proof.
Religious identity is not collective culpability.
Threat is assessed from capability, conduct, trajectory, and constraint interaction.
No body is exempt from the evidence standard.
A dissident does not become representative merely by retaining the parent label.
An outlier does not falsify a parent ideological invariant without evidence of representativeness.
```
