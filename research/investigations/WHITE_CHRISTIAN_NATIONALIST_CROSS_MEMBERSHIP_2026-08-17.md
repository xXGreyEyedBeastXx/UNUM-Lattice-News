# White-Nationalist / Christian-Nationalist Cross-Membership and Convergence — 2026-08-17

Status: ACTIVE INVESTIGATION / CROSS-MEMBERSHIP AND DUAL-CLASSIFICATION SUPPORTED / FULL NETWORK MAP UNRESOLVED

## Research question

Are white-nationalist / white-supremacist and Christian-nationalist movements merely rhetorically similar, or is there recoverable evidence of dual-classified movements, cross-membership, personnel migration, organizational succession, coalition events, and ideological transmission between them?

## Current answer

**Yes. The overlap is materially stronger than shared rhetoric alone.**

The evidence supports at least four distinct relation classes:

1. **DUAL-CLASSIFIED MOVEMENT** — a movement simultaneously advances white-nationalist / white-supremacist and Christian-nationalist aims.
2. **PERSONNEL CROSSING / CROSS-MEMBERSHIP** — individuals or memberships move between multiple extremist organizations.
3. **ORGANIZATIONAL SUCCESSION / REBRANDING** — personnel and functions persist while the organizational shell changes.
4. **COALITION / EVENT OVERLAP** — distinct organizations share demonstrations, conferences, or mobilization spaces without necessarily sharing membership or command.

These relation classes must not be collapsed into one generic `CONNECTED_TO` edge.

## Specimen 1 — America First / Groypers: dual ideological classification

ADL characterizes Nick Fuentes and the America First / Groyper movement as white-supremacist while documenting Fuentes's explicit promotion of Christian nationalism and a desired white Christian nation. The movement therefore provides a contemporary specimen where white nationalism and Christian nationalism are co-instantiated in the same movement rather than merely adjacent.

This matters because an actor can use a Christian-nationalist frame as an exoteric or mainstreaming surface for white-nationalist demographic and racial hierarchy claims without ceasing to be white nationalist.

Correct typing:

`AMERICA_FIRST_GROYPER -> WHITE_NATIONALIST` — supported

`AMERICA_FIRST_GROYPER -> CHRISTIAN_NATIONALIST` — supported

`WHITE_NATIONALISM == CHRISTIAN_NATIONALISM` — false collapse

## Specimen 2 — Legion of Saint Ambrose: Tennessee organizational succession

ADL documents Knoxville-based Legion of Saint Ambrose as a white-supremacist organization seeking a white Christian nation and Christian state religion. It was founded by former members of the neo-Nazi Traditionalist Worker Party. In 2020, most of its membership reportedly left to join NSC-Dixie, a southern chapter of Nationalist Social Club.

This provides a direct Tennessee-relevant example of:

`TWP personnel -> Legion of Saint Ambrose -> NSC-Dixie`

The names and organizational forms changed while personnel and white-power organizing continued.

This is precisely why group-name discontinuity must not automatically be treated as movement discontinuity.

## Specimen 3 — Billy Roper / Shield Wall Network: personnel migration across white-power organizations

ADL identifies Shield Wall Network founder Billy Roper as a Christian Identity adherent with prior involvement in National Alliance, White Revolution, Knights Party, and an Aryan Nations faction. SWN also participated in events with National Socialist Movement, League of the South, and Knights Party actors.

This is not merely ideological similarity. It is a recoverable personnel and coalition path across multiple organizations.

## Specimen 4 — Aryan Nations: common membership across white-power organizations

Aryan Nations / Church of Jesus Christ Christian combined Christian Identity, white supremacy, and neo-Nazism. ADL reports historical members in common with National Alliance, Ku Klux Klan organizations, and The Silent Brotherhood / The Order.

This establishes that cross-membership has historically been an ordinary feature of portions of the organized white-power movement rather than an exceptional anomaly.

## Christian Identity is a bridge, not a synonym

Christian Identity is an explicitly racist and antisemitic theology and is **not identical to contemporary Christian nationalism**.

However, SPLC reports both:

- Christian Identity's historical centrality in the organized white-power movement; and
- continuing seepage of Christian Identity rhetoric and themes into more mainstream Christian-nationalist, Dominionist, and neo-Confederate currents.

The correct relation is therefore transmission / influence where evidenced, not identity collapse.

`CHRISTIAN_IDENTITY != CHRISTIAN_NATIONALISM`

but

`CHRISTIAN_IDENTITY --INFLUENCES/TRANSMITS_THEMES_TO--> some CHRISTIAN_NATIONALIST currents` — supported at movement level by SPLC reporting.

## Population-level convergence

Organizational records are complemented by population-level research.

A 2025 Social Forces study finds that among white Americans, Christian nationalism is among the leading predictors of white racial solidarity: stronger white identity salience, group pride, perceived shared racial interests, and support for collective political action on behalf of white interests.

PRRI likewise finds sharp racial differences within Christian-nationalist adherents/sympathizers. White adherents/sympathizers are substantially more likely than Black counterparts to endorse racial-replacement and white-discrimination frames.

This supports a `WHITE_CHRISTIAN_NATIONALIST_CONVERGENCE` analytic category, but not the claim that every Christian nationalist is white nationalist. Nonwhite Christian nationalists exist and show materially different racial attitudes.

## Coalition spaces are weaker than cross-membership but still consequential

Unite the Right brought together neo-Nazis, Klan organizations, Christian Identity adherents, neo-Confederates, racist skinheads, Odinists, and militia-linked actors. This is a coalition/event edge.

The event does not prove that every attendee was a member of multiple groups or that all participating groups shared one command structure. It does demonstrate a real cross-movement encounter ecology in which people, propaganda, tactics, and relationships could pass between otherwise distinct bodies.

## Implication for Christian-nationalism reproductive-autonomy investigation

The reproductive-autonomy investigation should therefore not assume that white-nationalist, white-supremacist, and Christian-nationalist networks are separate explanatory silos.

When tracing pronatalism, replacement rhetoric, gender hierarchy, abortion policy, child-marriage defenses, anti-LGBTQ politics, or demographic-threat narratives, test for:

- dual ideological identification;
- shared personnel or membership;
- leadership migration;
- common events and conferences;
- shared donors / foundations;
- shared legal or advocacy infrastructure;
- media-platform and influencer conductance;
- rebranding / organizational succession;
- church / ministry / political-group bridges;
- explicit white-demographic or replacement rhetoric inside Christian-nationalist policy advocacy;
- Christian-nationalist framing used to mainstream otherwise explicit white-nationalist claims.

## Oath Keepers / militia caution

Do not solve this by relabeling every Patriot or militia organization as white nationalist.

ADL documents overlap between Oath Keepers and other militia / Three Percenter formations and historical overlap between the broader militia/Patriot movement and white supremacy, especially through Christian Identity. It also documents militia-linked presence at white-supremacist events.

That supports tracing `PERSONNEL_OVERLAP`, `COALITION_EVENT`, and `IDEOLOGICAL_CROSSING` where evidence exists. It does not, by itself, support classifying the entire Oath Keepers organization as a white-nationalist organization.

## Current lattice rule

```text
SHARED RHETORIC alone -> investigate
DUAL IDEOLOGICAL PROGRAM -> dual classification
PERSON IN MULTIPLE GROUPS -> cross-membership edge
MEMBERS MOVE FROM GROUP A TO GROUP B -> personnel succession edge
GROUP A DISSOLVES AND MEMBERS REFORM AS B -> organizational-succession candidate
SHARED EVENT -> coalition/event relation
SHARED FUNDING / COMMAND / PLANNING -> stronger coordination edge, if evidenced
```

The absence of one relation type cannot erase the others.

## Pattern conclusion

The current evidence supports an ecology in which white-nationalist / white-supremacist and Christian-nationalist currents can overlap through **the same movements, the same people, successor organizations, shared coalition spaces, inherited rhetoric, and shared demographic / national-order goals**.

Therefore, treating these movements as presumptively independent until a formal institutional affiliation is found would create systematic false separation.

At the same time, the lattice should not universalize the overlap:

- Christianity is not Christian nationalism;
- Christian nationalism is not automatically white nationalism;
- every militia actor is not a white nationalist;
- attendance is not membership;
- shared membership is not organizational identity;
- common ideology is not proof of central command.

## Next tracing targets

1. Current personnel who appear in both explicit white-nationalist and Christian-nationalist organizations.
2. Current Tennessee-specific cross-membership, especially successors to Legion of Saint Ambrose / NSC-Dixie and WLM-linked local actors.
3. Groypers / America First crossings into churches, Christian-nationalist conferences, political organizations, and policy networks.
4. Donor, foundation, legal, and media infrastructure shared between Christian-nationalist and white-nationalist campaigns.
5. Cross-membership and succession involving Proud Boys, Active Clubs, WLM, Klan formations, Patriot organizations, and explicitly Christian-nationalist groups, with each edge independently sourced.

## Sources

See `sources/source-white-christian-nationalist-cross-membership-2026-08-17.yaml`.
