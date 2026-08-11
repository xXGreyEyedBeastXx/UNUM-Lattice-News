# Controversy Membrane v0.1

This document defines editorial handling rules for topics that require heightened care due to their contested, sensitive, or politically charged nature. Each membrane specifies what the lattice will and will not do when processing content in that domain.

---

## Membrane: Reproductive Autonomy

**Covers:** abortion rights, anti-abortion policy, reproductive coercion, surveillance of pregnant people, minors and reproductive access, contraception access and restriction.

### What This Membrane Governs

Reproductive autonomy content spans a wide spectrum of factual, legal, and deeply contested moral claims. The lattice must handle this domain without amplifying coercive policy framing as neutral fact, without suppressing documented harms, and without treating contested legal interpretations as settled.

### Editorial Rules

#### 1. Factual Claims vs. Policy Advocacy
- **Do:** Surface documented facts — legislative text, court rulings, clinical outcomes, enforcement actions, surveillance incidents.
- **Do not:** Frame policy advocacy (e.g., "abortion is murder" or "abortion is healthcare") as settled factual claims. Both are contested normative positions.
- Headline review must flag any candidate that presents one normative framing as established fact.

#### 2. Anti-Abortion Policy Coverage
- Coverage of anti-abortion legislation, enforcement, and political organizing is in scope and should be surfaced factually.
- The lattice does not editorially endorse or oppose such policies.
- Enforcement actions against individuals must be covered with full context (legal basis, jurisdiction, outcome).
- Characterizations of policy as "pro-life" or "anti-choice" are advocacy language; prefer neutral descriptors: "abortion restriction," "abortion ban," "abortion access law."

#### 3. Extremism
- Documented threats, violence, or targeted harassment directed at abortion providers, clinics, patients, or advocates must be covered as extremism/safety content regardless of the actor's stated ideological motivation.
- The lattice applies the same extremism standard here as in any other domain: documented incitement or violence is not editorially balanced against the actor's cause.
- Do not surface content that functions as operational targeting material (clinic locations framed as threats, provider personal information).

#### 4. Surveillance of Pregnant People and Patients
- Surveillance of individuals based on pregnancy status, menstrual tracking, location near reproductive health facilities, or digital communications about reproductive decisions is a documented harm category.
- Surface surveillance disclosures, data broker exposures, law enforcement requests, and platform policy changes in this area as factual intake candidates.
- Do not suppress or downrank surveillance coverage because the surveillance is legally authorized in a given jurisdiction.

#### 5. Minors
- Content involving minors and reproductive access (parental notification laws, judicial bypass proceedings, cross-state travel by minors) must be handled with heightened privacy protection.
- Do not surface identifying information about minors involved in reproductive health cases, even when that information appears in source material.
- Coverage of the policy and legal landscape is in scope; coverage of specific minors is not.

#### 6. Contraception
- Contraception access, restriction, and coverage disputes are in scope.
- Contested claims about contraceptive mechanism (e.g., whether specific methods constitute "abortifacients") must be labeled as contested and linked to the relevant scientific and legal record.
- Do not present one side's characterization of a contraceptive method as settled medical fact when the characterization is disputed by mainstream clinical bodies.

### Lenses

Content in this membrane should be tagged with one or more of:
- `reproductive_autonomy`
- `law_governance_accountability`
- `health`
- `surveillance_privacy` (where applicable)
- `extremism_safety` (where applicable)

### Review Status

All candidates touching this membrane must enter review with `claim_posture: contested` unless the content is a primary source document (legislative text, court ruling, clinical study) in which case `claim_posture: primary_source` is appropriate.

No candidate in this membrane may be auto-approved. Human review is required.

---

## See Also

- `EDITORIAL_STANDARD.md` — overarching editorial principles
- `RIGHTS.md` — rights framework informing coverage decisions
- `schemas/LATTICE_RECORD_TEMPLATES_v0_1.yaml` — candidate schema including `claim_posture` and `default_lenses`