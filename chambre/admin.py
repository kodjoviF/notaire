
from django.contrib import admin
from .models import Membre, Document,Actualite  # Importez vos modèles

admin.site.register(Membre)
admin.site.register(Document)
admin.site.register(Actualite)
# Register your models here.
