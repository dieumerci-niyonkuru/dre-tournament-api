from rest_framework import serializers
from .models import Tournament, Team, Registration
from django.utils import timezone

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    tournament_name = serializers.ReadOnlyField(source='tournament.name')
    team_name = serializers.ReadOnlyField(source='team.name')

    class Meta:
        model = Registration
        fields = ['id', 'tournament', 'team', 'status', 'registered_at', 'tournament_name', 'team_name']

class RegisterTeamSerializer(serializers.Serializer):
    tournament_id = serializers.IntegerField()
    team_id = serializers.IntegerField()

    def validate(self, data):
        from .models import Tournament, Team, Registration
        tournament = Tournament.objects.get(id=data["tournament_id"])
        team = Team.objects.get(id=data["team_id"])

        if tournament.registration_deadline_utc < timezone.now():
            raise serializers.ValidationError(
                {"registration_deadline_utc": "Registration closed: deadline passed"}
            )

        current_registrations = Registration.objects.filter(tournament=tournament).count()
        if current_registrations >= tournament.max_teams:
            raise serializers.ValidationError("Tournament is full")

        if Registration.objects.filter(tournament=tournament, team=team).exists():
            raise serializers.ValidationError("Team already registered")

        return data
