from django import forms       
        
 # Formulaire qui recupère l'entrée de la recherche faite       
class MembreSearchForm(forms.Form):
    """
    Formulaire pour rechercher un membre.

    Args:
        search_query (CharField): Le champ de saisie pour la recherche.
    """
    search_query = forms.CharField(
        required=False,
        label='Rechercher un membre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez un nom, prénom ou Region'
        })
    )