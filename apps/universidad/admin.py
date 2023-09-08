# Importaciones Django
from django.contrib import admin
# Importaciones de terceros
from .models import Universidad, Error


admin.site.register(Universidad)
admin.site.register(Error)