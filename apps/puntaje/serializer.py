# Importaciones rest_framework
from rest_framework import serializers
# Importaciones locales
from .models import Puntaje


class PuntajeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Puntaje
    fields = '__all__'