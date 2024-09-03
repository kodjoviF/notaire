
from django.db import models

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