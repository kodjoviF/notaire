from django import forms
from .models import Document
from django.contrib.auth.models import User


# Formulaire qui recupère les documents
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['titre', 'type_document', 'fichier']
        
        
 # Formulaire qui recupère l'entrée de la recherche faite       
class MembreSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        label='Rechercher un membre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez un nom, prénom ou email'
        })
    )
    

# Formulaire de connexion qui recupère les identifiants de la connexion
class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
# Gestion des exceptions

        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                self.add_error('password', 'Mot de passe incorrect')
        except User.DoesNotExist:
            self.add_error('username', 'Nom d\'utilisateur inconnu')