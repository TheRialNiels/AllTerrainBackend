# Importaciones Django
from django.contrib import admin
# Importaciones de terceros
from .models import Rubrica, Error


admin.site.register(Rubrica)
admin.site.register(Error)