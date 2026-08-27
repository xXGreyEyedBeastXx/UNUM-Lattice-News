# Antifascism / Antifa Classifier Audit — 2026-08-27

**Status:** COMPLETED FIRST-PASS ORG-WIDE AUDIT / ACTIVE LEGACY INTERPRETATION OVERLAY  
**Scope:** searchable `Antifa` / `anti-fascism` references across the current GitHub organization, with emphasis on UNUM-Lattice-News and UNUM-Extremism-Watch  
**Trigger:** concern that a state or repository classifier could silently become the project's own conclusion that Antifa/antifascism is terrorism or extremism.

## Audit conclusion

No reviewed file was found in which the project itself simply adopts the proposition:

```text
Antifa = terrorism
antifascism = extremism
antifascist identity = initiating aggression
```

The reviewed occurrences fall mainly into four categories:

1. source-attributed Trump / White House / DOJ terrorism or `Antifa cell` classifiers;
2. research into whether those classifiers expanded security/prosecutorial power;
3. Prairieland case records separating specific violence and convictions from broader ideological/organizational attribution;
4. anti-laundering / causal-role rules explicitly warning against inheriting the classifier.

The primary weakness was **classifier inheritance by proximity** rather than an explicit project conclusion: a future agent could see an antifascist case inside `UNUM-Extremism-Watch`, or see `Antifa` adjacent to `terrorism`, and infer a classification that the underlying file did not authorize.

That route is now explicitly blocked.

## Controlling correction

New global lock:

```text
docs/ANTIFASCISM_CLASSIFIER_AND_DEMOCRATIC_ALIGNMENT_LOCK_v0_1.md
```

Core rule:

```text
antifascist identity
!= terrorism
!= extremism
!= criminality
!= formal organizational membership
!= initiating aggression

repository placement
!= extremism classification

official designation
!= independent truth of classifier
```

Antifascism at the principle seat is opposition to fascist domination and is compatible with defense of democratic conditions such as plural political life, equal political standing, free association, accountable government, and peaceful removability of rulers. Individual actors and acts still require act-specific classification.

## Files reviewed — safe source attribution / existing separation

### `sources/source-antifa-classifier-policy-2025-2026.yaml`

Status: **SAFE / SOURCE-ATTRIBUTED**

The file records Trump's executive designation, NSPM-7, and DOJ classifier use as government actions. Existing locks already say:

```text
Executive designation != criminal conviction
Anti-fascist belief != membership in a formal organization
Political ideology != material support or conspiracy
Temporal sequence != causation
```

### `research/notes/FAR_LEFT_TERRORISM_FRAMING_EVIDENCE_AUDIT_2026-08-26.md`

Status: **SAFE / STRONG CORRECTION SURFACE**

Explicitly states:

```text
government designation != neutral threat baseline
government press-release label != incident-level proof
```

and refuses to generalize state designations to anti-fascism, Palestine advocacy, protest, or left-wing politics as classes.

### `nodes/ideological-threat-labeling-and-redress-delegitimization.yaml`

Status: **SAFE**

Existing invariant:

```text
opposition_to_fascism_social_inequality_or_corporate_power_is_not_by_itself_evidence_of_terrorism
```

### `docs/HARM_MESH_COMPLAINT_CENSUS_2026-08-16.md`

Status: **SAFE / SOURCE-ATTRIBUTED**

Records White House threat framing and immediately requires violent crime, ideology, association, lawful protest, civil-liberties claims, funding relations, and nonviolent collective redress to remain separate.

### `sources/source-left-complaints-corporate-support-and-threat-labeling-2026-08-16.yaml`

Status: **SAFE / SOURCE-ATTRIBUTED**

White House `Antifa` and domestic-terrorism language appears only as primary-government framing. The source bundle states that neither side's causal interpretation is adopted merely because it is stated.

### `research/investigations/PRAIRIELAND_EVIDENCE_EXTRACTION_AND_LATTICE_PASS_2026-08-14.md`

Status: **SAFE / IMPORTANT LEGACY LOCK**

Explicitly prohibits:

```text
anti-fascist -> Antifa -> formal organization -> criminal conspiracy
```

and separates the post-event executive classifier sequence from specific convictions and conduct.

### `lattice/PRAIRIELAND_ICE_DETENTION_EVIDENCE_LATTICE_2026-08-14.yaml`

Status: **SAFE BUT LEGACY PROXIMITY RISK**

The file contains phrases such as `terrorism / Antifa classifier`, but within a transformation chain describing the movement from protest/violence to government/prosecutorial classification. The same lattice identifies `North Texas Antifa Cell` as a `prosecutorial_classifier` and says to treat it as DOJ/prosecution ontology unless independent organizational evidence is established.

Interpret all such legacy phrasing through the new global lock. Do not rewrite the historical evidence ledger merely to remove an attributed classifier.

### `research/harm-audit/CONSTITUTIONAL_SAFEGUARD_AND_REGIME_TRAJECTORY_LEDGER_2026-08-13.md`

Status: **SAFE / SOURCE-ATTRIBUTED**

Records the September 2025 White House designation as directional state action and explicitly requires lawful antifascist advocacy to remain distinct from violent conduct.

### `research/harm-audit/TRUMP_HUMANITARIAN_HARM_AND_EXTREMIST_ENABLEMENT_LEDGER_2026-08-13.md`

Status: **SAFE**

The Antifa mention occurs in reconstruction of Trump's 2020 debate rhetoric; it is not an independent extremism classification.

## Files changed in this audit

### Main Lattice

`docs/ANTIFASCISM_CLASSIFIER_AND_DEMOCRATIC_ALIGNMENT_LOCK_v0_1.md`

Added global cross-surface classifier, causal-role, organization, and repository-seating rules.

`nodes/anti-fascism-threat-labeling-and-security-capacity-expansion.yaml`

Updated to v0.2 with:

- principle-level democratic alignment;
- `anti_fascism_is_not_a_terrorism_or_extremism_predicate`;
- government designation != independent truth;
- antifascist identity != initiating aggression;
- repository/node location != classification;
- later responder wrongdoing cannot rehabilitate prior fascist/authoritarian coercion.

`tests/fixtures/ANTI_LAUNDERING_REASONING_REGRESSION_CASES_v0_1.yaml`

Updated to v0.2 with `antifascism_repository_classifier_inheritance` regression case.

### Extremism Watch

`README.md`

Added front-door rule:

```text
appears_in_UNUM_Extremism_Watch != classified_as_extremist
```

and explicit antifascism/official-classifier handling.

`cases/prairieland-ice-protest-prosecution-2025/PROFILE.yaml`

Updated to v0.2. `North Texas Antifa cell` is now explicitly recorded as the prosecution's ontology, not the repository's independent organizational or terrorism classification.

`crossings/FASCISM_FIELD_AND_REGIME_CONTEXT_BRIDGE_v0_1.md`

Updated to v0.2 with repository-seat and antifascism classifier locks.

## Legacy interpretation rule

Do not delete or sanitize historically accurate evidence that a government called Antifa or an antifascist actor `terrorist` or `extremist`. That state action itself may be highly consequential evidence.

Instead preserve:

```text
who applied classifier
when
under what authority
what conduct/predicate was asserted
what operational consequence followed
what independent evidence supports or contradicts the classifier
```

The historical statement:

> `Government X designated Antifa as terrorist`

must never be normalized into:

> `Antifa is terrorist`

without a separate independent classification record satisfying the required conduct, organization, intent, legal/analytical predicate, and evidentiary posture.

## Historical inversion guard

Misconduct by an antifascist or resistance actor does not retroactively transform fascism into democratic defense or legitimate prior fascist aggression/coercion.

```text
opponent wrongdoing != fascist exculpation
resistance wrongdoing != transfer of initiating aggression
state classifier != moral reversal
```

Historical fascist systems, including Nazi Germany, are assessed from their own documented ideology, institutions, aggression, repression, exclusion, mass violence, and exterminatory machinery. Opposition misconduct cannot invert that record.

## Regression discriminator

A future runtime fails this audit if it does any of the following:

```text
Antifa appears in Extremism Watch -> therefore Antifa is extremist
White House calls Antifa terrorist -> therefore terrorism is established
antifascist protest includes one violent actor -> antifascism becomes terrorism
resistance commits later wrongdoing -> prior fascist/state aggression becomes defense
shared antifascist identity -> one formal organization / command structure
```

## Tiny lock

> Preserve the government's classifier as evidence of government action. Never inherit it as reality merely because it is repeated, prosecuted, stored in an extremism repository, or attached to a resisting population.
