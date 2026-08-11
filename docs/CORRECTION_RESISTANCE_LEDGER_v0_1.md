ledger_entry:
  id: string                        # ledger-{sha256[:16]}
  schema: unum-lattice-news/correction-resistance-ledger/v0.1
  actor_ref: string                 # reference to actor node ID
  actor_name: string
  actor_role: string
  actor_institution: string
  lineage:
    known_since: date               # earliest documented record of actor in this domain
    prior_roles: list[string]
    funding_sources: list[string]   # disclosed or documented
    institutional_affiliations: list[string]
  behavioral_patterns:
    - pattern_id: string
      description: string
      first_documented: date
      recurrence_count: integer
      source_urls: list[string]
  correction_attempts:
    - attempt_id: string
      date: date
      correcting_party: string
      correction_summary: string
      actor_response: enum[acknowledged_and_updated, acknowledged_no_update, denied, ignored, retaliated]
      source_urls: list[string]
  retaliation_events:
    - event_id: string
      date: date
      target: string
      description: string
      source_urls: list[string]
  review_status: enum[candidate_unreviewed, under_review, published, disputed, retracted]
  last_updated: datetime
  editorial_notes: string