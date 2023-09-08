# Importaciones rest_framework
from rest_framework import serializers
# Importaciones locales
from .models import Rubrica


class RubricaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rubrica
    fields = '__all__'