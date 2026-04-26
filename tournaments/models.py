from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    max_teams = models.IntegerField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    members_count = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Registration(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['tournament', 'team']

    def __str__(self):
        return f"{self.team.name} -> {self.tournament.name}"
