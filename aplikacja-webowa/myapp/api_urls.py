from django.urls import path
from . import api_views

urlpatterns = [
    # Endpointy dla Osoba
    path('osoby/', api_views.person_list, name='osoby-list'),  # Lista i dodawanie osób
    path('osoby/<int:pk>/', api_views.person_detail, name='osoby-detail'),  # Szczegóły osoby

    # Endpointy dla Stanowisko
    path('stanowiska/', api_views.stanowisko_list, name='stanowisko-list'),  # Lista i dodawanie stanowisk
    path('stanowiska/<int:pk>/', api_views.stanowisko_detail, name='stanowisko-detail'),  # Szczegóły stanowiska
]
