# Actor and Authority Node Model v0.1

## Purpose

UNUM-Lattice-News needs to distinguish what an entity **is** from what role or authority it occupies in a particular event.

A flat node list such as `person | institution | movement | place` is insufficient for power analysis because a survivor, governor, corporation, court, state government, sovereign state, international organization, and federal agency can all appear as ordinary nodes while carrying radically different capacities, vulnerabilities, duties, and jurisdiction.

This model adds typed actor families and authority seats without turning role labels into moral verdicts.

## Core rule

```text
entity identity != role in event != authority level != evidentiary status
```

The same person or institution may occupy more than one role across different stories.

Example:

```text
person: governor
entity_type: person
actor_roles: [public_official, authority]
authority_seat: subnational_executive
jurisdiction: Tennessee, United States
```

A survivor is not defined only by victimization; `victim` or `survivor` is a role in relation to a documented or alleged harm event, not a total identity.

## Actor families

### Victim / survivor nodes

Use when a person or population is reported, alleged, adjudicated, or otherwise documented as bearing harm.

Preserve:

- self-description: victim, survivor, complainant, witness, plaintiff, affected population, other;
- harm relation and alleged/observed/adjudicated status;
- who caused or is accused of causing harm;
- reporting chronology;
- treatment after disclosure;
- threats, retaliation, exposure, litigation pressure, institutional response, and evidence attrition;
- agency, resistance, advocacy, and later roles.

Do not require adjudication before a victim-role relation may exist. Instead type the relation:

```text
ALLEGES_HARM_BY
DOCUMENTED_HARM_BY
ADJUDICATED_HARM_BY
REPORTS_HARM_BY
SURVIVED_HARM_BY
```

### Authority nodes

Authority is a **capacity relation**, not a truth privilege.

Authority-bearing persons may include:

- presidents and heads of government;
- governors and premiers;
- legislators;
- judges;
- prosecutors;
- police or military commanders;
- agency heads;
- regulators;
- corporate executives;
- religious authorities;
- party leaders;
- international officials.

Record:

- authority source;
- office or title;
- jurisdiction;
- term dates;
- formal powers;
- practical powers;
- appointment/election path;
- oversight and appeal mechanisms;
- conflicts of interest;
- funding or patronage relations.

An authority statement is evidence with provenance. It is not automatically a higher-truth observation.

### Institution nodes

Institutions may include:

- government agencies;
- corporations;
- political parties;
- churches or religious institutions;
- schools and universities;
- media organizations;
- NGOs;
- advocacy organizations;
- think tanks;
- unions;
- foundations;
- military or intelligence organizations;
- courts.

Record whether the institution is public, private, hybrid, supranational, religious, commercial, charitable, or other.

### Government nodes

Government needs multiple levels rather than one `state` label.

#### Local / municipal government

Cities, counties, municipalities, local authorities, school districts, local courts, police departments.

#### Subnational government

U.S. states such as Tennessee are **subnational federated governments**, not sovereign states in the international-law sense.

Record:

```text
government_level: subnational
constitutional_system: federal
jurisdiction: Tennessee
parent_sovereign: United States
```

Other countries may use provinces, cantons, Länder, regions, territories, or constituent nations.

#### Federal / national government

For a federal system such as the United States:

```text
government_level: federal
sovereign_status: sovereign_state_government
```

For a unitary country use `national` rather than forcing `federal`.

#### Sovereign state

A sovereign state is the international-law political entity, such as the United States, Israel, Germany, Mexico, or South Africa.

This is distinct from a U.S. state despite the shared English word `state`.

Suggested fields:

```text
entity_type: sovereign_state
sovereign_status: recognized | partially_recognized | disputed
recognition_notes: []
```

Recognition and sovereignty disputes must remain explicit rather than silently resolved by the schema.

#### International / supranational governance

Examples:

- United Nations;
- European Union;
- NATO;
- African Union;
- international treaty bodies;
- international financial institutions.

These are not simply `international governments`. Their authority differs by treaty, membership, mandate, and jurisdiction.

Use:

```text
entity_type: international_organization
authority_scope: treaty | supranational | intergovernmental | judicial | financial | security | other
```

### Court nodes

Courts require their own authority seat because they produce adjudicated findings but are not infallible truth engines.

Court levels may include:

- local;
- state/subnational;
- federal/national;
- constitutional/supreme;
- international;
- regional supranational;
- arbitral or special tribunal.

Record:

- jurisdiction;
- legal system;
- appellate relation;
- standard of proof;
- procedural posture;
- whether the finding is final, appealed, stayed, vacated, reversed, settled, or otherwise limited.

International courts should remain distinct:

```text
International Court of Justice (ICJ)
International Criminal Court (ICC)
European Court of Human Rights (ECtHR)
```

They differ in parties, jurisdiction, subject matter, and enforcement.

## Additional actor families

The lattice should also preserve:

- accused / defendant;
- witness;
- whistleblower;
- journalist / media actor;
- donor / funder;
- lobbyist;
- contractor;
- intermediary;
- advocate;
- regulator;
- police / military / intelligence actor;
- corporation / owner;
- political party / movement;
- religious organization / authority;
- population / constituency;
- nonhuman ecology / affected environment.

These are roles or functional families, not moral labels.

## Recommended node extension

Add the following optional fields to node records:

```yaml
entity_type: ""
actor_roles: []
authority:
  has_authority: false
  seat: ""
  source: ""
  jurisdiction: ""
  level: "" # local | subnational | federal | national | sovereign | supranational | international | private | other
  term_start: null
  term_end: null
  oversight: []
  appeal_or_review: []

vulnerability:
  roles: [] # victim | survivor | complainant | witness | whistleblower | affected_population | other
  protection_needs: []

funding:
  gives_to: []
  receives_from: []

constituencies: []
```

## Relation families

### Harm and victimization

```text
ALLEGES_HARM_BY
REPORTS_HARM_BY
DOCUMENTED_HARM_BY
ADJUDICATED_HARM_BY
THREATENED_BY
HARASSED_BY
EXPOSED_BY
RETALIATED_AGAINST_BY
PROTECTED_BY
FAILED_BY
```

### Authority and governance

```text
GOVERNS
REGULATES
PROSECUTES
INVESTIGATES
ADJUDICATES
APPEALS_TO
OVERRULES
APPOINTS
REMOVES
SANCTIONS
DESIGNATES
DETAINS
DEPORTS
FUNDS
CONTRACTS_WITH
```

### Money and influence

```text
DONATES_TO
FUNDS
LOBBIES
EMPLOYS
CONTRACTS_WITH
OWNS
INVESTS_IN
BENEFITS_FROM
ADVOCATES_FOR
ENDORSES
```

`BENEFITS_FROM` must never imply `CAUSED` without additional evidence.

### Information and evidence control

```text
REPORTS_TO
TESTIFIES_BEFORE
DISCLOSES
WITHHOLDS
SEALS
REDACTS
LEAKS
PUBLISHES
AMPLIFIES
DISPUTES
CORROBORATES
CONTRADICTS
```

### Constituency and representation

```text
REPRESENTS
CLAIMS_TO_REPRESENT
SERVES
IMPACTS
ABANDONS_COMMITMENT_TO
REVERSES_POSITION_ON
ACTS_AGAINST_STATED_INTEREST_OF
```

The last three require explicit temporal evidence and should normally begin as `supported_inference` rather than `observed` unless the contradiction is direct and documentary.

## Evidence-state interaction

Every consequential relation carries its own posture:

```text
observed
stated
adjudicated
alleged
supported_inference
disputed
ambiguous
unknown
missing_or_withheld
```

Unknown and ambiguous relations remain in the graph.

```text
unknown != absent
alleged != false
adjudicated != metaphysical certainty
authority != truth privilege
victim != identity totalization
```

## Power-aware query order

When reviewing a story, query in this order:

1. Who reports or bears harm?
2. Who has authority over them or the event?
3. Which institutions mediate the relation?
4. Which governments and jurisdictions have power to act?
5. Which courts or oversight bodies can review the action?
6. Who funds whom?
7. Who benefits and who bears cost?
8. What evidence is available, missing, sealed, delayed, contradicted, or degraded?
9. What retaliation, protection, refusal, appeal, or exit path exists?
10. What remains unknown?

This ordering is intended to prevent authority from becoming the default narrative seat.

## Tiny lock

> Start with the harmed signal, then map the powers around it. Authority changes capacity and provenance, not truth value. Preserve every jurisdiction, funding path, appeal route, ambiguity, and unknown needed to reconstruct how the outcome was produced.
