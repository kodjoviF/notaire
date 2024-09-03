from django import forms
from .models import Document, Membre
from django.contrib.auth.models import User

# Formulaire qui recupère les documents
class DocumentForm(forms.ModelForm):
    """
    Formulaire pour créer ou modifier un document.

    Args:
        titre (CharField): Le titre du document.
        type_document (CharField): Le type de document.
        fichier (FileField): Le fichier associé au document.
    """
    class Meta:
        model = Document
        fields = ['titre', 'type_document', 'fichier']



# Formulaire de connexion qui recupère les identifiants de la connexion
class ConnexionForm(forms.Form):
    """
    Formulaire pour se connecter.

    Args:
        username (CharField): Le nom d'utilisateur.
        password (CharField): Le mot de passe.
    """
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def clean(self):
        """
        Méthode pour valider les données du formulaire.

        Raises:
            ValidationError: Si les données sont invalides.
        """
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                self.add_error('password', 'Mot de passe incorrect')
        except User.DoesNotExist:
            self.add_error('username', 'Nom d\'utilisateur inconnu')

# Formulaire pour charger un document PDF
class DocumentChargeForm(forms.Form):
    """
    Formulaire pour charger un document PDF.

    Args:
        fichier (FileField): Le champ de saisie pour le fichier PDF.
    """
    fichier = forms.FileField(label='Fichier PDF')

# Formulaire pour s'inscrire
class RegisterForm(forms.ModelForm):
    """
    Formulaire pour s'inscrire.

    Args:
        nom (CharField): Le nom du membre.
        prenom (CharField): Le prénom du membre.
        adresse (CharField): L'adresse du membre.
        telephone (CharField): Le téléphone du membre.
        email (EmailField): L'email du membre.
        photo (ImageField): La photo du membre.
        username (CharField): Le nom d'utilisateur.
        password (CharField): Le mot de passe.
        region (CharField): La région du membre.
    """
    class Meta:
        model = Membre
        fields = ('nom', 'prenom', 'adresse', 'telephone', 'email', 'photo', 'username', 'password', 'region')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget = forms.Select(choices=Membre.REGION_CHOICES)