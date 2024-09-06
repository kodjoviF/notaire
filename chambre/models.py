
from django.db import models
from django.contrib.auth.models import AbstractUser

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    REGION_CHOICES = [
        ('Savanes', 'Savanes'),
        ('Kara', 'Kara'),
        ('Centrale', 'Centrale'),
        ('Plateau', 'Plateau'),
        ('Maritime', 'Maritime'),
        ('Grand Lomé', 'Grand Lomé'),
    ]
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    photo = models.ImageField(blank=True, null=True, upload_to='photos_identite/')

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    

class Actualite(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateField()
    auteur = models.CharField(max_length=255)
    image = models.ImageField(upload_to='actualites/')

    def __str__(self):
        return self.titre
    
    
class Activite(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    auteur = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    date_publication = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    
class MembreBureau(models.Model):
    titre = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nom} {self.prenom} {self.titre}"
    
    
