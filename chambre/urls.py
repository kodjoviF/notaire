from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('services/', views.services, name='services'),
    path('membres/', views.membres, name='membres'),
    path('activites/', views.activites, name='activites'),
    path('actualites/', views.actualites, name='actualites'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dernières_actualités, name='dernières_actualités'),
]