from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.db.models import Q
from .models import Membre, Document,Actualite,Activite
from .forms import DocumentForm, MembreSearchForm,ConnexionForm

def accueil(request):
    return render(request, 'chambre/accueil.html')

# Récupère les 3 dernières actualités



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
def membres(request):
    form = MembreSearchForm(request.GET)
    membres = Membre.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        if search_query:
            membres = membres.filter(
                Q(nom__icontains=search_query) |
                Q(prenom__icontains=search_query) |
                Q(email__icontains=search_query)
            )

    return render(request, 'chambre/membres.html', {'membres': membres, 'form': form})


def activites(request):
    
    # liste d'activités
    activites = [
        {"titre": "Séminaire sur les nouvelles lois", "date": "2024-09-15"},
        {"titre": "Assemblée générale annuelle", "date": "2024-10-01"},
        {"titre": "Formation continue en droit immobilier", "date": "2024-11-20"}
    ]
    return render(request, 'chambre/activites.html', {'activites': activites})



def actualites(request):
    
    
    # liste d'actualités nécessaire
    actualites = [
        {"titre": "Nouvelle réglementation sur les actes électroniques", "date": "2024-08-01"},
        {"titre": "La Chambre des Notaires accueille 10 nouveaux membres", "date": "2024-07-15"},
        {"titre": "Participation à la conférence internationale des notaires", "date": "2024-06-30"}
    ]
    return render(request, 'chambre/actualites.html', {'actualites': actualites})


#Tableau de baord 
@login_required
def dashboard(request):
    membre = request.user.membre
    documents = membre.documents.all()

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.membre = membre
            document.save()
            return redirect('dashboard')
    else:
        form = DocumentForm()

    context = {
        'membre': membre,
        'documents': documents,
        'form': form
    }
    return render(request, 'chambre/dashboard.html', context)

# Détail de l'afichage des documents
@login_required
def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.user.membre != document.membre:
        return redirect('dashboard')
    return render(request, 'chambre/document_detail.html', {'document': document})


# Affichage de la recherche
def recherche(request):
    query = request.GET.get('q')
    membres = Membre.objects.all()
    documents = Document.objects.all()

    if query:
        membres = membres.filter(
            Q(nom__icontains=query) |
            Q(prenom__icontains=query) |
            Q(email__icontains=query)
        )
        documents = documents.filter(
            Q(titre__icontains=query) |
            Q(type_document__icontains=query)
        )

    context = {
        'membres': membres,
        'documents': documents,
        'query': query
    }
    return render(request, 'chambre/recherche.html', context)

# La page de connexion
def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')
    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', {'form': form})


def dernières_actualités(request):
    activites = Activite.objects.order_by('-date_publication')[:3]
    return render(request, 'dernières_actualités.html', {'activites': activites})