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
      reporteDiseno = 0
      promedioRubricaPresentaciones = 0
      promedioAceleracionFrenado = 0
      rubricaManiobrabilidad = 0
      hillTraction = 0
      rubricaResistencia = 0

      totalPruebas = len(pruebas)

      sumaReporteDiseno = 0
      sumaRubricaPresentaciones = 0
      sumaAceleracionFrenado = 0
      sumaManiobrabilidad = 0
      sumaHillTraction = 0
      sumaResistencia = 0

      menorTiempoCircuito = 0
      menorTiempoAceleracion = 0

      for prueba in pruebas:
        sumaReporteDiseno += prueba.reporteDiseno if prueba.reporteDiseno else 0
        sumaRubricaPresentaciones += prueba.rubricaPresentaciones if prueba.rubricaPresentaciones else 0
        sumaAceleracionFrenado += prueba.aceleracionFrenado if prueba.aceleracionFrenado else 0
        sumaManiobrabilidad += prueba.rubricaManiobrabilidad if prueba.rubricaManiobrabilidad else 0
        sumaHillTraction += prueba.hillTraction if prueba.hillTraction else 0
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

      promedioReporteDiseno = (sumaReporteDiseno / totalPruebas) if sumaReporteDiseno else 0
      promedioRubricaPresentaciones = ((sumaRubricaPresentaciones / totalPruebas) / 3) if sumaRubricaPresentaciones else 0
      promedioAceleracionFrenado = (sumaAceleracionFrenado / totalPruebas) if sumaAceleracionFrenado else 0
      promedioRubricaManiobrabilidad = (sumaManiobrabilidad / totalPruebas) if sumaManiobrabilidad else 0
      promedioHillTraction = (sumaHillTraction / totalPruebas) if sumaHillTraction else 0
      promedioRubricaResistencia = (sumaResistencia / totalPruebas) if sumaResistencia else 0

      totalPuntaje = promedioReporteDiseno + promedioRubricaPresentaciones + promedioAceleracionFrenado + promedioRubricaManiobrabilidad + promedioHillTraction + promedioRubricaResistencia

      # Guardar los promedios en el modelo de Puntaje
      Puntaje.objects.update_or_create(
        idEquipo_id=data['idEquipo'],
        defaults={
          'promedioReporteDiseno': promedioReporteDiseno,
          'promedioRubricaPresentaciones': promedioRubricaPresentaciones,
          'promedioAceleracionFrenado': promedioAceleracionFrenado,
          'promedioRubricaManiobrabilidad': promedioRubricaManiobrabilidad,
          'promedioHillTraction': promedioHillTraction,
          'promedioRubricaResistencia': promedioRubricaResistencia,
          'menorTiempoCircuito': menorTiempoCircuito,
          'menorTiempoAceleracion': menorTiempoAceleracion,
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