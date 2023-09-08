# Importaciones rest_framework
from rest_framework import serializers
# Importaciones locales
from .models import Asesor


class AsesorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Asesor
    fields = '__all__'