# Node Dossier Topology v0.1

## Purpose

UNUM Lattice News treats major actors, institutions, ideologies, technologies, conditions, movements, and capture hypotheses as durable addresses in an evolving relational field.

A canonical node should remain small enough to preserve identity, type, stable relations, and evidence posture. Long-running investigations should accumulate in an adjacent dossier directory rather than turning the canonical node into an unbounded biography.

## Core object types

### Node

A durable address for a person, institution, ideology, condition, technology, movement, policy, or other persistent entity or concept.

### Stitch

A local documented connection between two or more nodes, claims, sources, actions, or consequences. A stitch should preserve relation type and provenance.

### Bridge

A typed crossing between domains, explanatory surfaces, or node families. A bridge can connect medical, political, institutional, ideological, economic, technological, cultural, or ecological analyses without collapsing them into identity.

### Dossier

A living local view around one durable node. It may contain pointers to claims, actions, rhetoric, harms, sources, bridges, stitches, corrections, and outward relations.

## Additive migration rule

Existing canonical node paths remain valid during migration. Dossier directories are added beside them.

Example:

```text
nodes/people/robert-f-kennedy-jr.yaml
nodes/people/robert-f-kennedy-jr/
  README.md
  claims/
  actions/
  rhetoric/
  harms/
  sources/
  bridges/
  stitches/
  corrections/
```

Do not move or delete canonical node files until all references are traced and a deliberate migration receipt is created.

## Suggested node families

```text
nodes/
  people/
  institutions/
  ideologies/
  technologies/
  conditions/
  movements/
  cultural-capture/
  policies/
```

These are addressing families, not moral categories.

## Cultural-capture boundary

`cultural-capture` is a hypothesis and mechanism family, not an automatic finding.

Use explicit posture such as:

- `OBSERVED_INFLUENCE`
- `SUPPORTED_CAPTURE_MECHANISM`
- `POTENTIAL_CAPTURE`
- `DISPUTED_CAPTURE`
- `INSUFFICIENT_EVIDENCE`

A documented relationship does not automatically establish capture, coordination, control, or private intent.

## Cross-node rule

A relation may be locally visible from multiple dossiers while remaining one canonical relation object.

For example, an autism-policy investigation may be reachable from:

```text
Robert F. Kennedy Jr.
  <-> HHS
  <-> Autism
  <-> Disability / neurodiversity
  <-> Eugenics
  <-> Vaccine policy
  <-> Research allocation
  <-> Diagnostic overshadowing
```

Each dossier may point to the crossing. None owns the truth of the crossing by itself.

## Re-entry

A healthy dossier lets a later reviewer answer:

- what is this node;
- what claims involve it;
- what actions are documented;
- what harms or benefits are attributed and at what evidence posture;
- which institutions, ideologies, policies, and populations connect to it;
- where the primary sources live;
- what is inference versus observation;
- what remains disputed or unknown;
- and which other nodes provide alternate local reads of the same relation.
