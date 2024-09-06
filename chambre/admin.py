
from django.contrib import admin
from .models import Actualite,Activite,MembreBureau,Membre

# Model save in admin space

admin.site.register(Actualite)
admin.site.register(Activite)
admin.site.register(MembreBureau)
admin.site.register(Membre)
