# Nova Organizer Affiliations and Boundary Analysis — 2026-08-17

Status: ACTIVE INVESTIGATION / ORGANIZATIONAL KINSHIP PARTIALLY RESOLVED / IDEOLOGY QUESTION OPEN

## Question

The Nova festival publicly framed itself around peace, love, freedom, internationalism and acceptance. What do the organizers' actual affiliations show, and could the social world being described as inclusive have been inclusive across friendly national/cultural boundaries while remaining structurally or politically separate from Palestinians in Gaza and the occupied West Bank?

## Immediate correction

Do not infer organizer ideology from festival branding.

```text
FESTIVAL_ETHOS != ORGANIZER_IDEOLOGY
INTERNATIONALISM != ANTI_NATIONALISM
COSMOPOLITAN_SOCIALITY != SOLIDARITY_WITH_OCCUPIED_POPULATION
```

A person can be socially liberal, internationally networked, culturally permissive and sincerely committed to peace/love while remaining Zionist, nationalist, security-aligned, indifferent to occupation, supportive of military policy, or simply politically unexamined. Each edge must be traced.

## Identity resolution: there is not one organizer list

### October 2023 production-company surface

Hebrew reporting after the massacre identifies **Nimrod Arnin, Omri Sassi and Omri Kochavi** as organizers from **Kzat LaNeshama Ltd.** and founders of Nova.

### Corporate surface

Kzat LaNeshama Ltd. is an Israeli private company incorporated in 2018. A current 2026 business-registry snapshot identifies **Ofir Amir** as shareholder/director, while litigation records connect **Omri Sassi** and **Yagil Rimoni** to the company. This may reflect role/ownership changes over time and requires historical Companies Authority filings for a publication-grade ownership chronology.

### Post-attack exhibition/foundation surface

Current Nova Exhibition material lists **Omri Sassi, Yoni Feingold, Ofir Amir and Yagil Rimoni** as Nova founders. Tribe of Nova has a broader survivor-support, memorial, fundraising and public-advocacy structure.

Correct model:

```text
KZAT_LANESHAMA_COMPANY
  != OCT_7_EVENT_PRODUCTION_TEAM necessarily in every period
  != TRIBE_OF_NOVA_ASSOCIATION
  != NOVA_EXHIBITION_TEAM
```

but these bodies have substantial personnel kinship and succession/continuity relations.

## Organizer affiliation findings

### Nimrod Arnin

**Established:**
- Nova/Kzat LaNeshama organizer/founder surface.
- Post-Oct. 7 co-originator of a high-tech emergency command-center effort with Guy Katsovich.
- Primary/near-primary accounts state that Arnin and Katsovich used Nova ticketing/communications data to build missing-person databases used by command centers and Israeli security bodies.
- CTech reports the broader High-Tech Command Center distributed equipment to more than 200 IDF units.
- Arnin publicly expressed continuing love of Israel after the massacre.

**Strong lead requiring primary recovery:**
- The Grayzone reports that Arnin's then-LinkedIn profile described co-founding **Cobalt Complex**, an OSINT/WEBINT center supporting Israeli intelligence, later integrated into Aman/IDF Intelligence. The indexed current LinkedIn profile no longer exposes this historical description. Until the original historical profile, archive, or official military record is recovered, type the Aman-integration claim as `SUPPORTED_LEAD`, not confirmed fact.

**Interpretation:**
Arnin's post-attack trajectory demonstrates a real crossing from civilian festival production into security/intelligence-support activity. It does **not** by itself prove he held a pre-Oct. 7 intelligence role or that the festival had an intelligence purpose.

### Omri Sassi

**Established:**
- Principal Nova/Kzat LaNeshama organizer/founder surface.
- Publicly expressed love for Israel after the massacre.
- Central participant in Nova memorial/exhibition advocacy internationally.
- Performed as DJ at an AFMDA gala whose hosts explicitly framed the gathering around Jewish/Zionist pride.

**Not established:**
- Likud affiliation.
- settler-movement affiliation.
- Religious-Zionist affiliation.
- pre-Oct. 7 military/intelligence organizational role beyond ordinary Israeli service possibilities.
- stated position on Palestinian rights, occupation or settlement policy.

The AFMDA appearance is an `EVENT_PARTICIPATION` relation, not automatic ideological endorsement.

### Omri Kochavi

**Established:**
- Original organizer/founder surface in Hebrew reporting.
- Current Tribe of Nova project-management role.

**Not yet established:**
- party affiliation;
- settlement affiliation;
- explicit nationalist ideology;
- security/intelligence organizational role.

### Ofir Amir

**Established:**
- Current Kzat LaNeshama corporate ownership/director relation in 2026 registry snapshot.
- Current Nova/Tribe organizer and external-relations role.
- Strong post-attack relationships with UJA and other Jewish philanthropic networks through survivor care and the exhibition.
- Public biography reports German birth, childhood move to Israel, Berlin business interests and a pre-Oct. 7 plan to relocate to Berlin with his family.

**Interpretation:**
His biography does not fit a simple closed ethnonationalist stereotype. At the same time, international mobility/cosmopolitanism does not answer his position on Palestinian political equality or occupation.

### Yagil Rimoni / Yoni Feingold

Current exhibition materials include them in the Nova-founder/producer surface; corporate/legal records tie Rimoni to Kzat LaNeshama. Their exact pre-Oct. 7 production, ownership and ideological roles need further resolution. Do not infer that every person later called a 'Nova founder' occupied the same legal or operational seat on Oct. 7.

## The user's boundary hypothesis

Candidate hypothesis:

> Nova's 'internationalist' culture may describe horizontal friendship among Israelis and foreign participants while leaving the vertical political relation to Palestinians in occupied/blockaded territories outside the community's practical moral boundary.

Current status: **PLAUSIBLE AND TESTABLE, NOT YET ESTABLISHED AS ORGANIZER INTENT.**

Why the distinction matters:

The official Nova community says attendees came from **36 countries**. But immediately before Oct. 7, UN OCHA reported that **most Palestinians in Gaza were not even eligible to apply for an Israeli exit permit**; eligible categories were mainly laborers, traders, patients/companions and aid workers. Therefore:

```text
36_COUNTRIES_PRESENT
!= BORDERLESS_ACCESS
!= GAZAN_PALESTINIAN_ACCESS
```

A festival five kilometers from Gaza could be genuinely international in one social dimension while residents on the other side of the perimeter were structurally unable to participate in that same internationalism.

That exclusion was primarily produced by the Israeli/Egyptian movement-control regime, not yet shown to be a Nova admissions policy. The important analytic point is that **cosmopolitan self-description can exist inside a bounded political geography whose excluded population is barely visible inside the cosmopolitan frame.**

## What would establish the stronger hypothesis

Search organizer and company records **before Oct. 7** for:

1. statements about Gaza, Palestinians, Arabs, occupation, settlements and Palestinian statehood;
2. participation in coexistence work involving Palestinians from the West Bank/Gaza versus only Jewish/Israeli/international communities;
3. participation in Zionist, nationalist, military-support, settlement, anti-occupation or peace organizations;
4. military/reserve histories where publicly self-disclosed and relevant;
5. event partnerships with state/security bodies beyond ordinary licensing and paid police security;
6. whether Arab citizens of Israel or Palestinian residents were present in meaningful numbers and how organizers described them;
7. whether 'acceptance of the other' was ever operationalized toward Palestinians specifically;
8. organizer reactions to major pre-Oct. 7 episodes of Gaza bombing, West Bank settler violence, judicial-overhaul protests and occupation policy;
9. business partners, donors and affiliated event-production firms with political/security ties;
10. historical corporate filings showing who owned/controlled Kzat LaNeshama at each relevant date.

## Current conclusion

The earlier description of Nova as simply a nonnationalist peace-and-love counterculture was **too compressed**.

Better current model:

```text
PSYTRANCE / COUNTERCULTURAL ETHOS
+ INTERNATIONAL SOCIAL NETWORK
+ ISRAELI PATRIOTIC ATTACHMENT among at least some principal organizers
+ POST_OCT7 SECURITY/INTELLIGENCE SUPPORT CROSSING for Arnin
+ POST_OCT7 ZIONIST/JEWISH PHILANTHROPIC AND ADVOCACY NETWORKS around the successor association/exhibition
+ UNKNOWN / UNDERTRACED PRE_OCT7 POSITION ON PALESTINIANS AND OCCUPATION
```

This is enough to reject the inference:

`PEACE_LOVE_INTERNATIONALISM -> POLITICAL UNIVERSALISM`

It is **not** yet enough to claim:

`NOVA_ORGANIZERS -> ANTI_PALESTINIAN NATIONALIST PROJECT`

The missing discriminator is the organizers' pre-Oct. 7 relationship to Palestinians and occupation, not whether they liked foreigners or trance culture.

## Source bundle

`sources/source-nova-organizer-affiliations-and-boundary-analysis-2018-2026.yaml`

## Locks

- Victim status does not immunize organizers from ordinary political/network investigation.
- Investigation of affiliations does not diminish the civilian status of festival victims.
- Post-attack trauma can materially change political conduct; do not silently back-project later conduct.
- Security collaboration after an attack != advance knowledge of the attack.
- Public peace rhetoric can be sincere and politically bounded at the same time.
- Palestinians != Hamas.
- Structural exclusion != organizer-specific discriminatory intent without evidence.
- Different organizer lists require identity/role reconciliation, not averaging.
