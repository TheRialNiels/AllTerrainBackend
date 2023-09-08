# Importaciones rest_framework
from rest_framework import serializers
# Importaciones locales
from .models import Prueba


class PruebaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Prueba
    fields = '__all__'