# views.py

from django.shortcuts import render, redirectfrom , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import DocumentForm, ConnexionForm, DocumentChargeForm
from .models import Membre, Document, Activite
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect



# ...

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('accueil')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', {'form': form})


# ...

class LogoutViewCustom(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    




# ....
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
            messages.success(request, 'Document saved successfully.')
            return redirect('dashboard')
    else:
        form = DocumentForm()

    context = {
        'membre': membre,
        'documents': documents,
        'form': form
    }
    return render(request, 'chambre/dashboard.html', context)

# ...

def document_create(request):
    if request.method == 'POST':
        form = DocumentChargeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document created successfully.')
            return redirect('document_list')
    else:
        form = DocumentChargeForm()

    return render(request, 'chambre/document_create.html', {'form': form})



def charger_document(request):
    """
    Charge un document PDF depuis l'ordinateur de l'utilisateur.

    Args:
        request (HttpRequest): La requête HTTP.


    Returns:
        HttpResponse: Une réponse HTTP avec un message de confirmation.

    Raises:
        ValueError: Si la méthode de requête n'est pas POST.
    """
    if request.method == 'POST':
        # Récupère le fichier PDF chargé par l'utilisateur
        fichier = request.FILES['fichier']
        nom_fichier = fichier.name
        # Stocke le fichier dans le système de fichiers de votre serveur
        chemin_fichier = default_storage.save(nom_fichier, File(fichier))
        # Retourne une réponse HTTP avec un message de confirmation
        return HttpResponse(f'Le fichier {nom_fichier} a été chargé avec succès.')
    else:
        # Retourne une réponse HTTP avec un message d'erreur si la méthode de requête n'est pas POST
        return HttpResponse('Erreur : méthode non autorisée.')
    
    

# ...

def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)

    if request.method == 'POST' and request.POST.get('confirm') == 'true':
        document.delete()
        messages.success(request, 'Document deleted successfully.')
        return redirect('document_list')

    return render(request, 'chambre/document_delete.html', {'document': document})


from django.http import HttpResponse

def afficher_document(request, nom_fichier):
    """
    Affiche un document PDF chargé.

    Args:
        request (HttpRequest): La requête HTTP.
        nom_fichier (str): Le nom du fichier PDF à afficher.

    Returns:
        HttpResponse: Une réponse HTTP avec le fichier PDF.

    Raises:
        ValueError: Si le fichier PDF n'existe pas.
    """
    # Récupère le chemin du fichier PDF chargé
    chemin_fichier = default_storage.path(nom_fichier)
    # Crée un objet File qui contient le fichier PDF
    fichier = File(chemin_fichier)
    # Génère une réponse HTTP qui contient le fichier PDF
    response = HttpResponse(fichier, content_type='application/pdf')
    # Ajoute un en-tête de réponse pour spécifier le nom du fichier
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(nom_fichier)
    # Retourne la réponse HTTP
    return response



def document_list(request):
    """
    Renvoie la liste des documents.

    :param request: Objet de requête HTTP
    :return: Réponse HTTP avec la liste des documents
    """
    try:
        documents = Document.objects.all()  # ou toute autre logique pour obtenir les documents
    except Document.DoesNotExist:
        # Gérer la situation où les documents ne sont pas trouvés
        documents = []
    context = {
        'documents': documents,
        # autres éléments du contexte si nécessaire
    }
    return render(request, 'chambre/document_list.html', context)



# la fonction recupère,filtre avec des requetes et affiche le result
def recherche_documents(request):
    query = request.GET.get('q')
    documents = Document.objects.all()

    if query:
        documents = documents.filter(
            Q(titre__icontains=query) |
            Q(type_document__icontains=query)
        )

    context = {
        'documents': documents,
        'query': query
    }
    return render(request, 'chambre/recherche_documents.html', context)



# ...

class ActiviteListAPIView(APIView):
    def get(self, request):
        activites = Activite.objects.all()
        serializer = ActiviteSerializer(activites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ActiviteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ...


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')