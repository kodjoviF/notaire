from django.urls import path
from . import views
from .views import ActiviteListAPIView

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('services/', views.services, name='services'),
    path('membres/', views.MembreBureau, name='membres_bureau'),
    path('activites/', views.activites, name='activites'),
    path('actualites/', views.actualites, name='actualites'),
    
    # API urls
    path('api/activites/', ActiviteListAPIView.as_view(), name='api-activites'),
]