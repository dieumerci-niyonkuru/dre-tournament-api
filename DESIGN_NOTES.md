# Design Notes

## Architecture choice
Django + DRF for rapid development

## Data model
Tournament, Team, Registration with unique_together

## Edge cases handled
Deadline, max_teams, duplicate registration

## Risks
Concurrency not fully handled - acceptable for junior demo

## Spec update (hour 24)
Added registration_deadline_utc field to Tournament. Validation now uses this field and returns a structured JSON error. Added boundary test for deadline edge case.
