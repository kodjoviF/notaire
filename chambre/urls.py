from django.urls import path
from .views import ActiviteListAPIView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('services/', views.services, name='services'),
    path('membres/', views.membres, name='membres'),
    path('activites/', views.activites, name='activites'),
    path('actualites/', views.actualites, name='actualites'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dernières_activites, name='dernières_activites'),
    
    
    # connexion path
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),

    
    
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # api urls
    path('api/activites/', ActiviteListAPIView.as_view(), name='api-activites'),
]
