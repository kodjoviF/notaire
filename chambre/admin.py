
from django.contrib import admin
from .models import Actualite,Activite 

# Model save in admin space

admin.site.register(Actualite)
admin.site.register(Activite)
