from django.db import models
from django.contrib.auth.models import User

class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos_identite/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Document(models.Model):
    TYPE_CHOICES = [
        ('identite', 'Identite'),
        ('acte', 'Acte'),
        ('procuration', 'Procuration'),
        ('mandat', 'Mandat'),
    ]
    titre = models.CharField(max_length=200)
    type_document = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)
    fichier = models.FileField(upload_to='documents/')
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name='documents')

    def __str__(self):
        return self.titre


# Classe qui recupère et stock les actualités de la chambre 
class Actualite(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateField()
    auteur = models.CharField(max_length=255)
    image = models.ImageField(upload_to='actualites/')

    def __str__(self):
        return self.titre
    

#Classe qui recupère et stock les actvités faite par la chambre

class Activite(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    auteur = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    date_publication = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


