
from django.contrib import admin
from .models import Membre, Document,Actualite,Activite 

# Model save in admin space
admin.site.register(Membre)
admin.site.register(Document)
admin.site.register(Actualite)
admin.site.register(Activite)
