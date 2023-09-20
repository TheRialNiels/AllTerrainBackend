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
      if data['rubricaPresentaciones']:
        defaults['rubricaPresentaciones'] = data['rubricaPresentaciones']
      if data['aceleracionFrenado']:
        defaults['aceleracionFrenado'] = data['aceleracionFrenado']
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
      if data['hillTractionPrimeraVez']:
        defaults['hillTractionPrimeraVez'] = data['hillTractionPrimeraVez']
      if data['hillTractionSegundaVez']:
        defaults['hillTractionSegundaVez'] = data['hillTractionSegundaVez']
      if data['maniobrabilidadPrimeraVez']:
        defaults['maniobrabilidadPrimeraVez'] = data['maniobrabilidadPrimeraVez']
      if data['maniobrabilidadSegundaVez']:
        defaults['maniobrabilidadSegundaVez'] = data['maniobrabilidadSegundaVez']

      if data['reporteDisenoCalificado']:
        defaults['reporteDisenoCalificado'] = data['reporteDisenoCalificado']
      if data['rubricaPresentacionesCalificado']:
        defaults['rubricaPresentacionesCalificado'] = data['rubricaPresentacionesCalificado']
      if data['aceleracionFrenadoCalificado']:
        defaults['aceleracionFrenadoCalificado'] = data['aceleracionFrenadoCalificado']
      if data['rubricaManiobrabilidadCalificado']:
        defaults['rubricaManiobrabilidadCalificado'] = data['rubricaManiobrabilidadCalificado']
      if data['hillTractionCalificado']:
        defaults['hillTractionCalificado'] = data['hillTractionCalificado']
      if data['rubricaResistenciaCalificado']:
        defaults['rubricaResistenciaCalificado'] = data['rubricaResistenciaCalificado']
      if data['circuitoCalificado']:
        defaults['circuitoCalificado'] = data['circuitoCalificado']
      if data['aceleracionCalificado']:
        defaults['aceleracionCalificado'] = data['aceleracionCalificado']

      # Guardar los datos de la prueba
      Prueba.objects.update_or_create(
        idEquipo_id=data['idEquipo'],
        idUsuario_id=request.user.id,
        defaults=defaults
      )

      pruebas = Prueba.objects.filter(idEquipo=data['idEquipo'])

      # Calcular los promedios
      promedioRubricaPresentaciones = 0
      promedioAceleracionFrenado = 0
      promedioRubricaResistencia = 0

      totalPruebas = len(pruebas)

      sumaRubricaPresentaciones = 0
      sumaAceleracionFrenado = 0
      sumaResistencia = 0

      menorTiempoCircuito = 0
      menorTiempoAceleracion = 0
      menorTiempoHillTraction = 0
      menorTiempoManiobrabilidad = 0

      for prueba in pruebas:
        sumaRubricaPresentaciones += prueba.rubricaPresentaciones if prueba.rubricaPresentaciones else 0
        sumaAceleracionFrenado += prueba.aceleracionFrenado if prueba.aceleracionFrenado else 0
        sumaResistencia += prueba.rubricaResistencia if prueba.rubricaResistencia else 0

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

        if prueba.hillTractionPrimeraVez and prueba.hillTractionSegundaVez:
          if float(prueba.hillTractionPrimeraVez) < float(prueba.hillTractionSegundaVez):
            menorTiempoHillTraction = prueba.hillTractionPrimeraVez
          else:
            menorTiempoHillTraction = prueba.hillTractionSegundaVez

        if prueba.maniobrabilidadPrimeraVez and prueba.maniobrabilidadSegundaVez:
          if float(prueba.maniobrabilidadPrimeraVez) < float(prueba.maniobrabilidadSegundaVez):
            menorTiempoManiobrabilidad = prueba.maniobrabilidadPrimeraVez
          else:
            menorTiempoManiobrabilidad = prueba.maniobrabilidadSegundaVez

      promedioRubricaPresentaciones = ((sumaRubricaPresentaciones / totalPruebas) / 3) if sumaRubricaPresentaciones else 0
      promedioAceleracionFrenado = (sumaAceleracionFrenado / totalPruebas) if sumaAceleracionFrenado else 0
      promedioRubricaResistencia = (sumaResistencia / totalPruebas) if sumaResistencia else 0
      promedioRubricaResistencia = (sumaResistencia / totalPruebas) if sumaResistencia else 0

      totalPuntaje = promedioRubricaPresentaciones + promedioAceleracionFrenado + promedioRubricaResistencia

      # Guardar los promedios en el modelo de Puntaje
      Puntaje.objects.update_or_create(
        idEquipo_id=data['idEquipo'],
        defaults={
          'promedioRubricaPresentaciones': promedioRubricaPresentaciones,
          'promedioAceleracionFrenado': promedioAceleracionFrenado,
          'promedioRubricaResistencia': promedioRubricaResistencia,
          'menorTiempoCircuito': menorTiempoCircuito,
          'menorTiempoAceleracion': menorTiempoAceleracion,
          'menorTiempoHillTraction': menorTiempoHillTraction,
          'menorTiempoManiobrabilidad': menorTiempoManiobrabilidad,
          'totalPuntaje': totalPuntaje
        }
      )

      return Response({'message': 'Puntaje actualizado correctamente'}, status=status.HTTP_201_CREATED)
    except Exception as e:
      Error.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ObtenerPuntajes(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = PuntajeSerializer
  queryset = Puntaje.objects.all()

  def list(self, request, *args, **kwargs):
    try:
      puntajes = Puntaje.objects.all()
      serializer = PuntajeSerializer(puntajes, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      Error.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)