# Layered Node Surface Model v0.2

Updated: 2026-08-21

## Purpose

A Lattice News node is not only a name and summary. It is a bounded subject surface that can expose the people, institutions, industries, money flows, technologies, policies, resources, constraints, accountability states, and public narratives directly connected to that subject.

The purpose is to let one node remain independently readable while still carrying enough structure to reveal how power, responsibility, consequence, gain, and correction are distributed.

New node identity uses the canonical `family` / `subtype` registry in `schemas/NODE_TYPE_REGISTRY_v0_1.yaml`. The descriptive classes below are reader-facing surface patterns, not a competing node-type registry. Existing legacy `node_type` or `entity_type` records remain migration-compatible.

## Reader-facing node patterns

### Institution nodes

Examples:

- governments and agencies;
- corporations;
- universities;
- foundations;
- militaries and intelligence bodies;
- political parties and movements;
- media organizations;
- regulatory bodies;
- financial institutions;
- religious or civil-society organizations.

Institution nodes may include:

```text
public leadership
formal governance
secondary operators
subsidiaries and divisions
contractors and partners
funding and ownership
policies and declared missions
technologies and capabilities
material term-setting where relevant
knowledge / notice / correction state where relevant
affected populations and ecologies
active disputes and investigations
```

### High-visibility person nodes

Examples:

- heads of state;
- ministers and senior officials;
- founders, chief executives, major owners, and board chairs;
- prominent investors;
- public movement leaders;
- senior military or intelligence officials;
- high-reach media figures.

A high-visibility person node should distinguish:

```text
public office or role
formal authority
ownership and financial interests
public statements
known institutional relationships
direct decisions or actions
advisers and delegated operators
claimed mission
observed consequences
knowledge / notice / persistence where evidenced
```

Visibility does not automatically establish control over every action taken by associated institutions.

### Secondary or lower-visibility person nodes

Examples:

- deputies and advisers;
- policy architects;
- board members;
- senior engineers or researchers;
- lobbyists;
- donors;
- contractors;
- legal representatives;
- program directors;
- procurement officials;
- intermediaries and operational managers.

These nodes are appropriate when the person has a documented public or institutional role relevant to the subject. They should not be created merely because a private individual appears adjacent to a controversy.

### Industry and market surfaces

Industries and markets are usually better represented through the canonical network, system, resource-flow, institution, or analysis-framework families rather than treated as an untyped catch-all node class.

Examples of useful market or domain surfaces include:

```text
artificial intelligence
facial-recognition services
cloud infrastructure
military targeting systems
neurotechnology
private intelligence
political consulting
data brokerage
energy infrastructure
mineral extraction
private equity
food retail
housing
healthcare
water access
```

Such surfaces describe shared markets, capabilities, supply chains, regulatory environments, resource flows, and recurring relationships without implying that every participant coordinates with every other participant.

### Other canonical families

Technology, policy, movement, population, ecology, place/jurisdiction, resource-flow, consequence, response/repair, claim/proposition, and analysis-framework nodes remain first-class when they match the canonical registry. Their internal lanes should be adapted to the actual subject rather than mechanically copied from actor nodes.

## Internal node lanes

A node may contain the following sections.

### Identity and current role

What is this node, what canonical family/subtype does it use, what does it do, and what scope does this record cover?

Entity identity, relation role, authority seat, hierarchy class, and evidentiary posture remain distinct.

### Public face

The people or offices most visibly associated with the node.

This is a visibility lane, not proof of full operational control.

### Governance and authority

Who holds formal decision rights, appointment power, voting power, command authority, ownership control, regulatory jurisdiction, or practical power to set consequential terms?

### Secondary operators

Which less-visible public actors materially shape policy, implementation, procurement, research, communication, pricing, compensation, access, or enforcement?

### Divisions, subsidiaries, and programs

What named internal organs or controlled entities carry out relevant functions?

### Industries, markets, and material systems

Which industries, markets, professional domains, resource systems, necessities, or supply chains does the node participate in?

### Money and material-flow network

Documented relationships such as:

```text
ownership
equity stakes
major investments
donations
campaign finance
contracts
procurement
subsidies
grants
loans
revenue dependence
foundation funding
lobbying expenditure
wages
rents
prices and fees
public benefits
public revenue
avoided cost
asset appreciation
resource access
```

Every material-flow claim should preserve amount, date or range, direction, source, transformation, and known limitations when available.

Money flow does not automatically establish control, agreement, corruption, extraction, or causation. But decomposition must not become fragmentation: where value changes accounting or legal seats, continue to the terminal or reseated beneficiary when evidence permits.

### Technology and infrastructure

Relevant systems, platforms, datasets, facilities, patents, supply chains, or technical dependencies.

### Policy and declared mission

Official goals, policies, strategies, public commitments, and stated justifications.

### Actions, term-setting, and observed consequences

Documented decisions, deployments, enforcement, transactions, wage/price/rent/fee/access conditions, or other consequential actions, plus affected populations or ecologies.

Keep intentional action or term-setting distinct from intent to cause every downstream harm.

### Accountability state

Where material to the node, preserve:

```text
intentional action / term-setting
intended gain / cost reduction / capacity increase
harmful-endpoint intent
knowledge state
capacity to know
foreseeability
credible notice
capacity to correct
response after notice
gain or insulation retained after notice
repair or mitigation
```

Do not infer actual knowledge from capacity to know. Do not infer deliberate avoidance from mere failure to investigate. Do not let uncertainty about motive or knowledge erase independently supported mechanism, outcome, loss, gain, or beneficiary edges.

### Narrative and public framing

How the node describes its own role and how credible external sources characterize it. These should remain separately attributed.

### Direct relations

Typed, evidenced edges to other nodes, resources, consequences, propositions, or contributions. Use the active relation vocabulary where a registered relation fits.

### Hashtag neighborhoods

High-recall routes into related subject areas. Hashtags may identify domains, mechanisms, flows, constraints, accountability questions, rights, harms, governance concerns, or evidence posture.

Hashtag co-occurrence is not an evidenced edge.

### Disputes, evidence effects, and unknowns

Material disagreement, incomplete evidence, unanswered questions, typed evidence effects, missingness, and evidence that would change the current rendition.

Legacy `counterevidence` may remain in historical records, but new work should route evidence to the exact claim or edge it updates rather than treating favorable facts as a general counterweight.

### Sources and corrections

Recoverable sources, dates, rights posture, source lineage, and correction trail.

## Visibility and responsibility

Keep these separate:

```text
high visibility != sole control
formal title != operational involvement
funding != command
association != agreement
employment != responsibility for every institutional act
public criticism != proven wrongdoing
capacity_to_know != actual_knowledge
intentional_term_setting != harmful_endpoint_intent
```

At the same time:

```text
low visibility != low influence
indirect control != no control
delegation != no responsibility
complexity != absence of accountability
harmful-endpoint intent unknown != intentional mechanism absent
legal recipient != terminal economic beneficiary
```

## Money-network discipline

Financial and material networks are especially vulnerable to both overstatement and false disconnection.

Each consequential flow should identify where possible:

- payer, source, or loss-bearer;
- recipient or destination;
- relation type;
- amount or scale;
- date or reporting period;
- stated purpose;
- source quality;
- whether the relation is direct or mediated;
- costs and productive contribution where extraction is alleged;
- counterfactual where incidence depends on one;
- terminal or reseated beneficiary;
- whether influence, control, gain, extraction, or causation is established, alleged, disputed, or unknown.

The lattice may expose a pattern of dependence, concentration, extraction, or recirculation when the individual edges support it. It must not convert every payment, investment, benefit, or shared funder into conspiracy.

## Node depth

A node may remain small when evidence is sparse or the subject is narrow.

A larger node may become a local index that points to subnodes or reusable records such as:

```text
institution
├── leadership
├── board and governance
├── subsidiaries
├── major programs
├── money / material-flow network
├── technology stack
├── policy history
├── accountability / notice chronology
└── affected populations
```

Do not force all material into one page. When a lane becomes independently important, create a subnode, contribution, claim, relation, spread, or other reusable record and retain the parent relation.

## Core locks

```text
Public face != total system.
Money relation != corruption.
Profit != extraction by itself.
Low visibility != irrelevance.
Association != culpability.
Complexity != immunity from accountability.
Capacity to know != actual knowledge.
Intentional term-setting != harmful-endpoint intent.
Uncertainty about motive != permission to erase the mechanism.
Node depth should follow evidence and use, not appetite for totality.
```