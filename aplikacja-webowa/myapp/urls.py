from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome_view, name="welcome"),
    path("persons/", views.person_list, name="person_list"),
    path("person/<int:id>/", views.person_detail, name="person_detail"),
    path("teams/", views.team_list, name="team_list"),
    path("team/<int:id>/", views.team_detail, name="team_detail"),
]
