# Importaciones rest_framework
from rest_framework import serializers
# Importaciones locales
from .models import Equipo


class EquipoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Equipo
    fields = '__all__'