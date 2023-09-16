# Importaciones Django
from django.shortcuts import render
# Importaciones rest_framework
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Importaciones locales
from .models import Equipo, Error
from .serializer import EquipoSerializer


class Equipo(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = EquipoSerializer
  queryset = Equipo.objects.all()

  def create(self, request, *args, **kwargs):
    try:
      data = request.data
      serializer = self.get_serializer(data=data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)

      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    except Exception as e:
      Error.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

  def list(self, request, *args, **kwargs):
    try:
      queryset = self.filter_queryset(self.get_queryset())
      serializer = self.get_serializer(queryset, many=True)
      return Response(serializer.data)
    except Exception as e:
      Error.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class EquipoByUser(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, format=None):
    try:
      equipo = Equipo.objects.filter(user=request.user.id).first()
      if equipo:
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)
      else:
        return Response({'error': 'Favor de agregar tu equipo'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      Error.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
