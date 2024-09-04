from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from .models import Actualite,Activite
from .forms import  MembreSearchForm
from django.contrib import messages

# Import api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



def accueil(request):
    return render(request, 'chambre/accueil.html')





def services(request):
    """liste de services si nécessaire"""
    
    services = [
        "Rédaction d'actes notariés",
        "Conseils juridiques",
        "Authentification de documents",
        "Gestion de succession"
    ]
    return render(request, 'chambre/services.html', {'services': services})




# Recuperation de la liste des membres a afficher 
def membresBureau(request):
    membres = Membre.objects.all()
    return render(request, 'membres_bureau.html', {'membres': membres})


# liste d'activités
def activites(request):
    activites = [
        {"titre": "Séminaire sur les nouvelles lois", "date": "2024-09-15"},
        {"titre": "Assemblée générale annuelle", "date": "2024-10-01"},
        {"titre": "Formation continue en droit immobilier", "date": "2024-11-20"}
    ]
    return render(request, 'chambre/activites.html', {'activites': activites})



# Cette fonction recupère les 3 dernières activités
def dernières_activites(request):
    activites = Activite.objects.order_by('-date_publication')[:3]
    return render(request, 'dernières_activites.html', {'activites': activites})



# liste d'actualités nécessaire
def actualites(request):
    actualites = [
        {"titre": "Nouvelle réglementation sur les actes électroniques", "date": "2024-08-01"},
        {"titre": "La Chambre des Notaires accueille 10 nouveaux membres", "date": "2024-07-15"},
        {"titre": "Participation à la conférence internationale des notaires", "date": "2024-06-30"}
    ]
    return render(request, 'chambre/actualites.html', {'actualites': actualites})



def recherche_membres(request):
    query = request.GET.get('q')
    membres = Membre.objects.all()

    if query:
        membres = membres.filter(
            Q(nom__icontains=query) |
            Q(prenom__icontains=query) |
            Q(email__icontains=query)
        )

    context = {
        'membres': membres,
        'query': query
    }
    return render(request, 'chambre/recherche_membres.html', context)




# cette vue est une api qui recupère la liste des cativités
class ActiviteListAPIView(APIView):
    def get(self, request):
        activites = Activite.objects.all()
        serializer = ActiviteSerializer(activites, many=True)
        return Response(serializer.data)