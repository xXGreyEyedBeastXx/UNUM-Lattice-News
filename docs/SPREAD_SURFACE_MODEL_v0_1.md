# Spread Surface Model v0.1

## Purpose

A **spread** is a reader-facing discovery and review surface assembled from lattice records. It is not an additional truth container and does not replace sources, stories, nodes, relations, contributions, or renditions.

A spread should help a reviewer see how an event travels across lived experience, institutions, material systems, and meaning without implying that proximity in the spread proves causation, intent, agreement, or culpability.

## Position in the lattice

```text
source -> story -> node -> relation -> rendition
                    \-> contribution <-/
                    \----> spread <----/
```

The underlying records remain authoritative for their own claims and provenance. A spread selects and arranges them for a bounded question, time window, or public consequence.

Contribution records are reusable across spreads. A study should reference a stable contribution record rather than duplicate the same factual body each time an action crosses into another investigation.

## Required boundaries

- Every anchor story and source must resolve to an existing record or an explicit review candidate.
- Every referenced contribution must resolve to an existing record or an explicit review candidate.
- Existing nodes, candidate nodes, and promoted nodes must remain visibly distinct.
- Automation may suggest candidate nodes, relations, and contributions, but may not promote them.
- A node is not a verdict; a relation is not proof of motive or blame; a contribution is not automatic culpability.
- Empty lenses are useful findings. A spread is not required to manufacture a node for every lens.
- Consequential public claims require human editorial review under `EDITORIAL_STANDARD.md`.
- Corrections must remain traceable through `CORRECTIONS.md` and the affected records.

## Core lenses

Each spread reviews its anchors through the lenses that are materially relevant:

- health;
- disability and accessibility;
- geopolitics and jurisdiction;
- culture;
- ideology and worldview;
- economy, finance, and ownership;
- labor, care, and dependency;
- law, governance, and accountability;
- technology, data, and infrastructure;
- ecology, climate, and material conditions;
- housing, land, and migration;
- education, science, and knowledge production;
- media, information, and language;
- conflict, security, policing, and carceral systems;
- history and public memory;
- community, resistance, mutual aid, and repair;
- children, aging, future generations, and recoverability.

These are observation lenses, not fixed taxonomies of people. A lens should record what is supported, what is missing, and what remains contested.

## Node exposure

Every reviewed spread records what it made newly visible:

- `existing_nodes`: already accepted nodes that became relevant to the spread;
- `candidate_nodes`: bounded proposals requiring evidence and human review;
- `promoted_nodes`: candidates separately accepted through the repository's review process.

A candidate should state:

1. the proposed node label and type;
2. the evidence that exposed it;
3. why existing nodes are insufficient;
4. affected people, ecologies, institutions, or material systems;
5. uncertainty, counterevidence, and possible conflations;
6. the reviewer and review decision.

## Contribution exposure

A spread may expose contribution records when an actor's specific participation is independently important.

A candidate contribution should state:

1. contributor node;
2. policy/action/mechanism node where available;
3. date or period;
4. bounded causal scope;
5. immediate mechanism;
6. direct and downstream effects being investigated;
7. evidence posture;
8. counterevidence and unknowns;
9. affected participants or ecologies;
10. other spreads or studies likely to reuse the same contribution.

A contribution should be promoted as a reusable record rather than buried permanently inside the first spread that discovered it.

## Review questions

A spread should ask, where relevant:

- Who acted, and through what mechanism or institution?
- Which specific contributions belong to which actors?
- Which contributions predate the event, which occur during it, and which belong to the consequence cone?
- Who or what bears the consequence, including indirect and cumulative effects?
- What law, money, ownership, infrastructure, labor, data, or resource flow matters?
- What lived-experience or accessibility dimension is otherwise easy to erase?
- What cultural or ideological framing shapes what can be seen or said?
- What geography, jurisdiction, history, or power asymmetry changes the interpretation?
- What resistance, adaptation, repair, appeal, refusal, or exit remains possible?
- What is unknown, disputed, absent, or only weakly supported?

## Lifecycle

`draft -> reviewed -> published -> corrected | archived`

Feed automation creates only intake candidates. It does not create a reviewed spread, publish a rendition, promote a contribution, or confer evidentiary status.
