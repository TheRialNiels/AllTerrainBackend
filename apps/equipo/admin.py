# Importaciones Django
from django.contrib import admin
# Importaciones de terceros
from .models import Equipo, Error


admin.site.register(Equipo)
admin.site.register(Error)
