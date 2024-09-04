from django.urls import path
from . import views

urlpatterns = [
    # Authentication paths
    path('login/', views.connexion, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Document paths
    path('document/list/', views.document_list, name='document_list'),
    path('document/create/', views.document_create, name='document_create'),
    path('document/delete/<int:pk>/', views.document_delete, name='document_delete'),
    
    # PDF document handling
    path('charger_document/', views.charger_document, name='charger_document'),
    path('afficher_document/<str:nom_fichier>/', views.afficher_document, name='afficher_document'),
]