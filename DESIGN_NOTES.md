# Design Notes

## Architecture choice
Django + DRF for rapid development

## Data model
Tournament, Team, Registration with unique_together

## Edge cases handled
Deadline, max_teams, duplicate registration

## Risks
Concurrency not fully handled - acceptable for junior demo
