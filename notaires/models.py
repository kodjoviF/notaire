from django.db import models
from django.contrib.auth.models import AbstractUser



class Membre(AbstractUser):
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
    

class Document(models.Model):
    TYPE_CHOICES = [
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



