from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tournament, Team, Registration
from .serializers import TournamentSerializer, TeamSerializer, RegistrationSerializer, RegisterTeamSerializer

class TournamentListCreateView(generics.ListCreateAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class RegistrationListView(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class RegisterTeamView(APIView):
    def post(self, request):
        serializer = RegisterTeamSerializer(data=request.data)
        if serializer.is_valid():
            tournament = Tournament.objects.get(id=serializer.validated_data['tournament_id'])
            team = Team.objects.get(id=serializer.validated_data['team_id'])
            registration = Registration.objects.create(tournament=tournament, team=team)
            return Response(RegistrationSerializer(registration).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateRegistrationStatusView(generics.UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    partial = True
