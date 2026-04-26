from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Tournament, Team, Registration
from rest_framework.test import APIClient

class TournamentRegistrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tournament = Tournament.objects.create(
            name="Test Tournament",
            max_teams=2,
            deadline=timezone.now() + timedelta(days=1)
        )
        self.team1 = Team.objects.create(name="Team Alpha", members_count=3)
        self.team2 = Team.objects.create(name="Team Beta", members_count=2)

    def test_create_tournament(self):
        response = self.client.post('/api/tournaments/', {
            'name': 'New Tourney',
            'max_teams': 5,
            'deadline': '2026-12-31T23:59:59Z'
        })
        self.assertEqual(response.status_code, 201)

    def test_register_team_success(self):
        response = self.client.post('/api/register/', {
            'tournament_id': self.tournament.id,
            'team_id': self.team1.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Registration.objects.count(), 1)

    def test_register_after_deadline_fails(self):
        self.tournament.deadline = timezone.now() - timedelta(days=1)
        self.tournament.save()
        response = self.client.post('/api/register/', {
            'tournament_id': self.tournament.id,
            'team_id': self.team1.id
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("deadline passed", str(response.data))
