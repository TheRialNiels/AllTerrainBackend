# Importaciones Django
from django.shortcuts import render
# Importaciones rest_framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Importaciones locales
from apps.prueba.models import Prueba, Error as ErrorPrueba
from apps.prueba.serializer import PruebaSerializer
from .models import Puntaje, Error
from .serializer import PuntajeSerializer
# Importaciones externas
import math


class ActualizarPuntaje(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = PuntajeSerializer
  queryset = Puntaje.objects.all()

  def create(self, request, *args, **kwargs):
    try:
      data = request.data

      defaults = {}

      if data['escrutinioSeguridad']:
        defaults['escrutinioSeguridad'] = data['escrutinioSeguridad']
      if data['reporteDiseno']:
        defaults['reporteDiseno'] = data['reporteDiseno']
      if data['rubricaPresentaciones']:
        defaults['rubricaPresentaciones'] = data['rubricaPresentaciones']
      if data['aceleracionFrenado']:
        defaults['aceleracionFrenado'] = data['aceleracionFrenado']
      if data['rubricaManiobrabilidad']:
        defaults['rubricaManiobrabilidad'] = data['rubricaManiobrabilidad']
      if data['hillTraction']:
        defaults['hillTraction'] = data['hillTraction']
      if data['rubricaResistencia']:
        defaults['rubricaResistencia'] = data['rubricaResistencia']
      if data['circuitoPrimeraVez']:
        defaults['circuitoPrimeraVez'] = data['circuitoPrimeraVez']
      if data['circuitoSegundaVez']:
        defaults['circuitoSegundaVez'] = data['circuitoSegundaVez']
      if data['aceleracionPrimeraVez']:
        defaults['aceleracionPrimeraVez'] = data['aceleracionPrimeraVez']
      if data['aceleracionSegundaVez']:
        defaults['aceleracionSegundaVez'] = data['aceleracionSegundaVez']

      # Guardar los datos de la prueba
      Prueba.objects.update_or_create(
        idEquipo_id=data['idEquipo'],
        idUsuario_id=request.user.id,
        defaults=defaults
      )

      pruebas = Prueba.objects.filter(idEquipo=data['idEquipo'])

      # Calcular los promedios
      # reporteDiseno = 0
      promedioRubricaPresentaciones = 0
      promedioAceleracionFrenado = 0
      # rubricaManiobrabilidad = 0
      # hillTraction = 0
      # rubricaResistencia = 0
      menorTiempoCircuito = 0
      menorTiempoAceleracion = 0

      for prueba in pruebas:
        # reporteDiseno += prueba.reporteDiseno
        promedioRubricaPresentaciones += prueba.rubricaPresentaciones if prueba.rubricaPresentaciones else 0
        promedioAceleracionFrenado += prueba.aceleracionFrenado if prueba.aceleracionFrenado else 0
        # rubricaManiobrabilidad += prueba.rubricaManiobrabilidad
        # hillTraction += prueba.hillTraction
        # rubricaResistencia += prueba.rubricaResistencia

        if prueba.circuitoPrimeraVez and prueba.circuitoSegundaVez:
          if float(prueba.circuitoPrimeraVez) < float(prueba.circuitoSegundaVez):
            menorTiempoCircuito = prueba.circuitoPrimeraVez
          else:
            menorTiempoCircuito = prueba.circuitoSegundaVez

        if prueba.aceleracionPrimeraVez and prueba.aceleracionSegundaVez:
          if float(prueba.aceleracionPrimeraVez) < float(prueba.aceleracionSegundaVez):
            menorTiempoAceleracion = prueba.aceleracionPrimeraVez
          else:
            menorTiempoAceleracion = prueba.aceleracionSegundaVez

      # Guardar los promedios en el modelo de Puntaje
      Puntaje.objects.update_or_create(
        idEquipo_id=data['idEquipo'],
        defaults={
          # 'promedioReporteDiseno': reporteDiseno,
          'promedioRubricaPresentaciones': promedioRubricaPresentaciones,
          'promedioAceleracionFrenado': promedioAceleracionFrenado,
          # 'promedioRubricaManiobrabilidad': rubricaManiobrabilidad,
          # 'promedioHillTraction': hillTraction,
          # 'promedioRubricaResistencia': rubricaResistencia,
          'menorTiempoCircuito': menorTiempoCircuito,
          'menorTiempoAceleracion': menorTiempoAceleracion,
        }
      )

      return Response({'message': 'Puntaje actualizado correctamente'}, status=status.HTTP_201_CREATED)
    except Exception as e:
      Error.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
