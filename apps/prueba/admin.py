# Importaciones Django
from django.contrib import admin
# Importaciones de terceros
from .models import Prueba, Error


admin.site.register(Prueba)
admin.site.register(Error)