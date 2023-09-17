# Importaciones rest_framework
from rest_framework import serializers
# Importaciones locales
from .models import Universidad


class UniversidadSerializer(serializers.ModelSerializer):
  nombre_equipo = serializers.SerializerMethodField()
  class Meta:
    model = Universidad
    fields = '__all__'

  def get_nombre_equipo(self, obj):
    if obj.idEquipo:
      return obj.idEquipo.nombreEquipo
    return None