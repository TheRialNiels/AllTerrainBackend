# Importaciones Django
from django.contrib import admin
# Importaciones de terceros
from .models import Encargado, Error


admin.site.register(Encargado)
admin.site.register(Error)