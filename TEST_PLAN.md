# Test Plan

1. Create tournament - basic POST works
2. Successful registration - happy path
3. Registration after deadline fails - tests business rule
4. Tournament full fails - second business rule
5. Duplicate registration fails - unique_together test

## Additional test details
- Test 1 (create tournament): validates POST endpoint returns 201 and stores data.
- Test 2 (successful registration): ensures happy path works.
- Test 3 (deadline fail): verifies business rule prevents late registration.
- Test 4 (tournament full): checks max_teams limit is enforced.
