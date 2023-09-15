# Importaciones Django
from django.contrib import admin
# Importaciones de terceros
from .models import Puntaje, Error


admin.site.register(Puntaje)
admin.site.register(Error)