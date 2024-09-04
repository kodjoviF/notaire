from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.core.files import File
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .forms import ConnexionForm, DocumentForm, DocumentChargeForm, RegisterForm
from chambre.models import Activite
from .models import Document 
from .serializers import ActiviteSerializer

@login_required
def dashboard(request):
    """
    Affiche le tableau de bord de l'utilisateur connecté, permettant de gérer les documents.
    """
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
    return render(request, 'notaires/dashboard.html', context)

@login_required
def document_list(request):
    """
    Affiche la liste de tous les documents.
    """
    documents = Document.objects.all()
    context = {'documents': documents}
    return render(request, 'notaires/document_list.html', context)

@login_required
def document_create(request):
    """
    Permet de créer un nouveau document.
    """
    if request.method == 'POST':
        form = DocumentChargeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document created successfully.')
            return redirect('document_list')
    else:
        form = DocumentChargeForm()
    return render(request, 'notaires/document_create.html', {'form': form})

@login_required
def charger_document(request):
    """
    Permet de charger un document sur le serveur.
    """
    if request.method == 'POST':
        fichier = request.FILES['fichier']
        nom_fichier = fichier.name
        chemin_fichier = default_storage.save(nom_fichier, File(fichier))
        return HttpResponse(f'Le fichier {nom_fichier} a été chargé avec succès.')
    else:
        return HttpResponse('Erreur : méthode non autorisée.')

@login_required
def document_delete(request, pk):
    """
    Permet de supprimer un document.
    """
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST' and request.POST.get('confirm') == 'true':
        document.delete()
        messages.success(request, 'Document deleted successfully.')
        return redirect('document_list')
    return render(request, 'notaires/document_delete.html', {'document': document})

@login_required
def afficher_document(request, nom_fichier):
    """
    Permet d'afficher un document.
    """
    chemin_fichier = default_storage.path(nom_fichier)
    fichier = File(open(chemin_fichier, 'rb'))
    response = HttpResponse(fichier, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{nom_fichier}"'
    return response

@login_required
def recherche_documents(request):
    """
    Permet de rechercher des documents.
    """
    query = request.GET.get('q')
    documents = Document.objects.all()
    if query:
        documents = documents.filter(
            Q(titre__icontains=query) |
            Q(type_document__icontains=query)
        )
    context = {'documents': documents, 'query': query}
    return render(request, 'notaires/recherche_documents.html', context)

class ActiviteListAPIView(APIView):
    """
    API View pour la gestion des activités.
    """
    def get(self, request):
        """
        Renvoie la liste de toutes les activités.
        """
        activites = Activite.objects.all()
        serializer = ActiviteSerializer(activites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Crée une nouvelle activité.
        """
        serializer = ActiviteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def register_view(request):
    """
    Permettre l'enregistrement d'un nouvel utilisateur.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'notaires/register.html', {'form': form})

def logout_view(request):
    """
    Déconnecte l'utilisateur.
    """
    logout(request)
    return redirect('accueil')

def connexion(request):
    """
    Connecte l'utilisateur.
    """
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
    return render




#### les vues pour initialiser les mots de passe 



from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.urls import reverse_lazy

class PasswordResetView(PasswordResetView):
    """
    Vue pour la réinitialisation du mot de passe.
    """
    template_name = 'notaires/password_reset.html'
    email_template_name = 'notaires/password_reset_email.html'
    subject_template_name = 'notaires/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Réinitialiser le mot de passe"
        return context

class PasswordResetDoneView(PasswordResetDoneView):
    """
    Vue pour afficher le message de réinitialisation du mot de passe.
    """
    template_name = 'notaires/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Réinitialisation du mot de passe"
        return context