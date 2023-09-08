# Importaciones Django
from django.contrib import admin
# Importaciones de terceros
from .models import Asesor, Error


admin.site.register(Asesor)
admin.site.register(Error)