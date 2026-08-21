# Typed Hashtag Registry v0.2

Updated: 2026-08-21

Hashtags are discovery neighborhoods, not verdicts or evidence of coordination.

## Namespaces

```text
#person/<Name>
#institution/<Name>
#technology/<Name>
#policy/<Name>
#movement/<Name>
#place/<Name>
#population/<Name>
#ecology/<Name>

#domain/<Topic>
#mechanism/<Mechanism>
#flow/<FlowOrDirection>
#constraint/<ConstraintOrDependency>
#accountability/<AccountabilityStateOrQuestion>
#right/<ProtectedCapacity>
#harm/<Consequence>
#governance/<Concern>
#status/<EvidencePosture>
#source/<SourceClass>
```

Entity-style hashtag namespaces remain human-facing discovery handles. Canonical node identity for new records is defined by `schemas/NODE_TYPE_REGISTRY_v0_1.yaml`; hashtag namespace and node family are not required to be identical.

## Initial high-contest neighborhoods

### Technology and power

```text
#domain/ArtificialIntelligence
#domain/Neurotechnology
#domain/MilitaryTechnology
#domain/DreamResearch
#technology/FacialRecognition
#technology/AutonomousWeapons
#technology/AIDecisionSupport
#technology/TargetedDreamIncubation
```

### Mechanisms

```text
#mechanism/Surveillance
#mechanism/Classification
#mechanism/TargetSelection
#mechanism/NeuralRecording
#mechanism/NeuralStimulation
#mechanism/DreamGuidance
#mechanism/AutomationBias
#mechanism/ClosedLoopOptimization
```

### Material extraction, necessity gating, and recirculation

```text
#domain/Labor
#domain/PublicFinance
#domain/Taxation
#domain/Housing
#domain/FoodSystems
#domain/Healthcare
#domain/Water
#domain/Land
#domain/CorporateGovernance

#mechanism/WageSuppression
#mechanism/PublicAssistanceLaborCostSupplementation
#mechanism/PricePower
#mechanism/RentCapture
#mechanism/ResourceGating
#mechanism/SurvivalEnclosure
#mechanism/PublicCostExternalization
#mechanism/DownwardScapegoating
#mechanism/CausalPartitionLaundering
#mechanism/TerminalBeneficiaryReseating

#flow/UpwardRecirculation
#flow/PublicToPrivate
#flow/WorkerToOwner
#flow/TenantToOwner
#flow/ConsumerToOwner
#flow/TaxpayerToPrivateRevenue
#flow/ExternalizedCost

#constraint/Dependency
#constraint/CaptiveDemand
#constraint/LackOfMeaningfulExit
#constraint/MarketConcentration
#constraint/EmployerLinkedNecessity
#constraint/BenefitConditionality
```

These tags identify a route for investigation. They do not establish that a particular wage, price, rent, benefit, profit, tax treatment, or ownership relation is extractive in a specific case.

### Accountability and knowledge

```text
#accountability/IntentionalTermSetting
#accountability/IntentionalGainSeeking
#accountability/CapacityToKnow
#accountability/ShouldHaveKnown
#accountability/CredibleNotice
#accountability/ActualKnowledge
#accountability/ContinuedAfterNotice
#accountability/EscalatedAfterNotice
#accountability/MitigatedAfterNotice
#accountability/Repair
#accountability/RefusalToRepair
#accountability/DeliberateAvoidance
```

Accountability tags are especially high-risk for semantic leakage. Use them only to route to an explicit evidence-bounded accountability record or clearly provisional investigation state.

```text
#accountability/CapacityToKnow != proof of actual knowledge
#accountability/ShouldHaveKnown != legal negligence finding by itself
#accountability/DeliberateAvoidance != inference from mere failure to investigate
#accountability/IntentionalTermSetting != intent to cause every downstream harm
```

### Protected capacities

```text
#right/HumanDignity
#right/SelfSovereignty
#right/MentalPrivacy
#right/CognitiveLiberty
#right/MeaningfulHumanControl
#right/Consent
#right/Refusal
#right/MeaningfulExit
#right/Appeal
```

### Governance and harms

```text
#governance/DemocraticAccountability
#governance/InstitutionalOversight
#governance/CorporatePower
#governance/CorporateAccountability
#governance/MilitaryAuthority
#governance/MarketConcentration
#governance/PublicCostShifting
#governance/TaxIncidence

#harm/CivilLibertiesRisk
#harm/CivilianHarm
#harm/PrivacyLoss
#harm/BehavioralManipulation
#harm/IrreversibleForce
#harm/MaterialDeprivation
#harm/FoodInsecurity
#harm/HousingInsecurity
#harm/HealthcareInsecurity
#harm/WageLoss
#harm/Dependency
#harm/ResourceEnclosure
#harm/PowerConcentration
```

### Evidence posture

```text
#status/Observed
#status/Stated
#status/SupportedInference
#status/Potential
#status/Possible
#status/Probable
#status/Likely
#status/Alleged
#status/Disputed
#status/Unknown
```

## Use rule

Use the broadest useful human-readable neighborhood while preserving a typed namespace underneath.

Do not infer an edge because two nodes share a hashtag.

```text
shared hashtag -> investigate possible relation
shared hashtag != established relation
accountability hashtag != accountability finding
harm hashtag != proof of causation
flow hashtag != proof of terminal beneficiary
```

Where a hashtag begins carrying case-specific evidentiary meaning rather than discovery value, promote the underlying relation, claim, contribution, or accountability state into a typed record instead of making the tag do evidentiary work.
