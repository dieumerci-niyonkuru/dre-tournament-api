from django.urls import path
from .views import *

urlpatterns = [
    path('tournaments/', TournamentListCreateView.as_view(), name='tournament-list-create'),
    path('teams/', TeamCreateView.as_view(), name='team-create'),
    path('registrations/', RegistrationListView.as_view(), name='registration-list'),
    path('register/', RegisterTeamView.as_view(), name='register-team'),
    path('registrations/<int:pk>/', UpdateRegistrationStatusView.as_view(), name='update-status'),
]
