# Importaciones rest_framework
from rest_framework import serializers
# Importaciones locales
from .models import Encargado


class EncargadoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Encargado
    fields = '__all__'