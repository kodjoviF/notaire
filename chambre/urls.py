from django.urls import path
from .views import ActiviteListAPIView
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth.decorators import permission_required
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('services/', views.services, name='services'),
    path('membres/', views.membres, name='membres'),
    path('activites/', views.activites, name='activites'),
    path('actualites/', views.actualites, name='actualites'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dernières_activites, name='dernières_activites'),
    
    

    # connexion path
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),


    # Définit l'URL pour charger un document PDF
    path('charger_document/', views.charger_document, name='charger_document'),
    # Définit l'URL pour afficher un document PDF
    path('afficher_document/<str:nom_fichier>/', views.afficher_document, name='afficher_document'),



   # URL pour le dashboard
    path('dashborad', views.dashboard, name='dashboard'),
    # URL pour la liste des documents
    path('document/list/', views.document_list, name='document_list'),
    # URL pour créer un nouveau document
    path('document/create/', views.document_create, name='document_create'),
    # URL pour supprimer un document
    path('document/delete/<int:pk>/', views.document_delete, name='document_delete'),


    path('document/<int:pk>/', views.document_detail, name='document_detail'),


    # URL pour créer un nouveau document
    path('document/create/', views.document_create, name='document_create'),
    # URL pour supprimer un document
    path('document/delete/<int:pk>/', views.document_delete, name='document_delete'),






    
    
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # api urls
    path('api/activites/', ActiviteListAPIView.as_view(), name='api-activites'),
]
