from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Prueba, Error
from .serializer import PruebaSerializer


class ObtenerPruebaPorUsuarioYEquipo(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = PruebaSerializer
  queryset = Prueba.objects.all()

  def list(self, request, *args, **kwargs):
    try:
      idEquipo = request.query_params.get('idEquipo')
      idUsuario = request.user.id

      if idEquipo and idUsuario:
        queryset = Prueba.objects.filter(idEquipo=idEquipo, idUsuario=idUsuario)
        serializer = PruebaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      Error.objects.create(error=e)
      return Response({'error': 'Ha ocurrido un error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)