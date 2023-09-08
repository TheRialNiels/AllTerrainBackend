# Importaciones rest_framework
from rest_framework import serializers
# Importaciones locales
from .models import Universidad


class UniversidadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Universidad
    fields = '__all__'