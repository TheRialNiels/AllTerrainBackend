# Importaciones Django
from django.shortcuts import render
# Importaciones rest_framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Importaciones locales
from .models import Puntaje, Error
from apps.prueba.models import Prueba
from .serializer import PuntajeSerializer


class Puntaje(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = PuntajeSerializer
  queryset = Puntaje.objects.all()

  # Obten todas las pruebas de un equipo para posteriormente sacar el promedio de sus puntajes y guardarlos en la tabla puntaje
  def create(self, request, *args, **kwargs):
    try:
      data = request.data
      serializer = self.get_serializer(data=data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)

      # Obtenemos el id del equipo
      idEquipo = data['idEquipo']

      # Obtenemos todas las pruebas del equipo
      pruebas = Prueba.objects.filter(idEquipo=idEquipo)

      promedioReporteDiseno = 0
      promedioRubricaPresentaciones = 0
      promedioAceleracionFrenado = 0
      promedioRubricaManiobrabilidad = 0
      promedioHillTraction = 0
      promedioRubricaResistencia = 0

      mayorTiempoCircuito = 0
      mayorTiempoAceleracion = 0

      # Obtener el total de pruebas de cada tipo para sacar el promedio
      totalReporteDiseno = 0
      totalRubricaPresentaciones = 0
      totalAceleracionFrenado = 0
      totalRubricaManiobrabilidad = 0
      totalHillTraction = 0
      totalRubricaResistencia = 0

      # Obtener el mayor tiempo de cada tipo de prueba
      mayorTiempoCircuito = 0
      mayorTiempoAceleracion = 0

      # Sacar el promedio de cada tipo de prueba
      for prueba in pruebas:
        # Sacar el promedio de cada tipo de prueba
        promedioReporteDiseno += prueba.reporteDiseno
        promedioRubricaPresentaciones += prueba.rubricaPresentaciones
        promedioAceleracionFrenado += prueba.aceleracionFrenado
        promedioRubricaManiobrabilidad += prueba.rubricaManiobrabilidad
        promedioHillTraction += prueba.hillTraction
        promedioRubricaResistencia += prueba.rubricaResistencia

        # Sacar el mayor tiempo de cada tipo de prueba
        if prueba.circuitoPrimeraVez > mayorTiempoCircuito:
          mayorTiempoCircuito = prueba.circuitoPrimeraVez
        if prueba.circuitoSegundaVez > mayorTiempoCircuito:
          mayorTiempoCircuito = prueba.circuitoSegundaVez
        if prueba.aceleracionPrimeraVez > mayorTiempoAceleracion:
          mayorTiempoAceleracion = prueba.aceleracionPrimeraVez
        if prueba.aceleracionSegundaVez > mayorTiempoAceleracion:
          mayorTiempoAceleracion = prueba.aceleracionSegundaVez

        # Obtener el total de pruebas de cada tipo para sacar el promedio
        totalReporteDiseno += 1
        totalRubricaPresentaciones += 1
        totalAceleracionFrenado += 1
        totalRubricaManiobrabilidad += 1
        totalHillTraction += 1
        totalRubricaResistencia += 1

      # Sacar el promedio de cada tipo de prueba
      promedioReporteDiseno = promedioReporteDiseno / totalReporteDiseno
      promedioRubricaPresentaciones = promedioRubricaPresentaciones / totalRubricaPresentaciones
      promedioAceleracionFrenado = promedioAceleracionFrenado / totalAceleracionFrenado
      promedioRubricaManiobrabilidad = promedioRubricaManiobrabilidad / totalRubricaManiobrabilidad
      promedioHillTraction = promedioHillTraction / totalHillTraction
      promedioRubricaResistencia = promedioRubricaResistencia / totalRubricaResistencia

      # Guardar los promedios en la tabla puntaje
      puntaje = Puntaje.objects.get(idEquipo=idEquipo)
      puntaje.promedioReporteDiseno = promedioReporteDiseno
      puntaje.promedioRubricaPresentaciones = promedioRubricaPresentaciones
      puntaje.promedioAceleracionFrenado = promedioAceleracionFrenado
      puntaje.promedioRubricaManiobrabilidad = promedioRubricaManiobrabilidad
      puntaje.promedioHillTraction = promedioHillTraction
      puntaje.promedioRubricaResistencia = promedioRubricaResistencia
      puntaje.mayorTiempoCircuito = mayorTiempoCircuito
      puntaje.mayorTiempoAceleracion = mayorTiempoAceleracion
      puntaje.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    except Exception as e:
      Error.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
# Importaciones rest_framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Importaciones locales
from .models import Puntaje, Error
from apps.prueba.models import Prueba
from .serializer import PuntajeSerializer


class Puntaje(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = PuntajeSerializer
  queryset = Puntaje.objects.all()

  # Obten todas las pruebas de un equipo para posteriormente sacar el promedio de sus puntajes y guardarlos en la tabla puntaje
  def create(self, request, *args, **kwargs):
    try:
      data = request.data
      serializer = self.get_serializer(data=data)
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)

      # Obtenemos el id del equipo
      idEquipo = data['idEquipo']

      # Obtenemos todas las pruebas del equipo
      pruebas = Prueba.objects.filter(idEquipo=idEquipo)

      promedioReporteDiseno = 0
      promedioRubricaPresentaciones = 0
      promedioAceleracionFrenado = 0
      promedioRubricaManiobrabilidad = 0
      promedioHillTraction = 0
      promedioRubricaResistencia = 0

      mayorTiempoCircuito = 0
      mayorTiempoAceleracion = 0

      # Obtener el total de pruebas de cada tipo para sacar el promedio
      totalReporteDiseno = 0
      totalRubricaPresentaciones = 0
      totalAceleracionFrenado = 0
      totalRubricaManiobrabilidad = 0
      totalHillTraction = 0
      totalRubricaResistencia = 0

      # Obtener el mayor tiempo de cada tipo de prueba
      mayorTiempoCircuito = 0
      mayorTiempoAceleracion = 0

      # Sacar el promedio de cada tipo de prueba
      for prueba in pruebas:
        # Sacar el promedio de cada tipo de prueba
        promedioReporteDiseno += prueba.reporteDiseno
        promedioRubricaPresentaciones += prueba.rubricaPresentaciones
        promedioAceleracionFrenado += prueba.aceleracionFrenado
        promedioRubricaManiobrabilidad += prueba.rubricaManiobrabilidad
        promedioHillTraction += prueba.hillTraction
        promedioRubricaResistencia += prueba.rubricaResistencia

        # Sacar el mayor tiempo de cada tipo de prueba
        if prueba.circuitoPrimeraVez > mayorTiempoCircuito:
          mayorTiempoCircuito = prueba.circuitoPrimeraVez
        if prueba.circuitoSegundaVez > mayorTiempoCircuito:
          mayorTiempoCircuito = prueba.circuitoSegundaVez
        if prueba.aceleracionPrimeraVez > mayorTiempoAceleracion:
          mayorTiempoAceleracion = prueba.aceleracionPrimeraVez
        if prueba.aceleracionSegundaVez > mayorTiempoAceleracion:
          mayorTiempoAceleracion = prueba.aceleracionSegundaVez

        # Obtener el total de pruebas de cada tipo para sacar el promedio
        totalReporteDiseno += 1
        totalRubricaPresentaciones += 1
        totalAceleracionFrenado += 1
        totalRubricaManiobrabilidad += 1
        totalHillTraction += 1
        totalRubricaResistencia += 1

      # Sacar el promedio de cada tipo de prueba
      promedioReporteDiseno = promedioReporteDiseno / totalReporteDiseno
      promedioRubricaPresentaciones = promedioRubricaPresentaciones / totalRubricaPresentaciones
      promedioAceleracionFrenado = promedioAceleracionFrenado / totalAceleracionFrenado
      promedioRubricaManiobrabilidad = promedioRubricaManiobrabilidad / totalRubricaManiobrabilidad
      promedioHillTraction = promedioHillTraction / totalHillTraction
      promedioRubricaResistencia = promedioRubricaResistencia / totalRubricaResistencia

      # Guardar los promedios en la tabla puntaje
      puntaje = Puntaje.objects.get(idEquipo=idEquipo)
      puntaje.promedioReporteDiseno = promedioReporteDiseno
      puntaje.promedioRubricaPresentaciones = promedioRubricaPresentaciones
      puntaje.promedioAceleracionFrenado = promedioAceleracionFrenado
      puntaje.promedioRubricaManiobrabilidad = promedioRubricaManiobrabilidad
      puntaje.promedioHillTraction = promedioHillTraction
      puntaje.promedioRubricaResistencia = promedioRubricaResistencia
      puntaje.mayorTiempoCircuito = mayorTiempoCircuito
      puntaje.mayorTiempoAceleracion = mayorTiempoAceleracion
      puntaje.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    except Exception as e:
      Error.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# # Importaciones Django
# from django.shortcuts import render
# # Importaciones rest_framework
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# # Importaciones locales
# from .models import Puntaje, Error
# from apps.prueba.models import Prueba
# from .serializer import PuntajeSerializer


# class Puntaje(viewsets.ModelViewSet):
#   permission_classes = [IsAuthenticated]
#   serializer_class = PuntajeSerializer
#   queryset = Puntaje.objects.all()

#   # Obten todas las pruebas de un equipo para posteriormente sacar el promedio de sus puntajes y guardarlos en la tabla puntaje
#   def create(self, request, *args, **kwargs):
#     try:
#       data = request.data
#       serializer = self.get_serializer(data=data)
#       serializer.is_valid(raise_exception=True)
#       self.perform_create(serializer)
#       headers = self.get_success_headers(serializer.data)

#       # Obtenemos el id del equipo
#       idEquipo = data['idEquipo']

#       # Obtenemos todas las pruebas del equipo
#       pruebas = Prueba.objects.filter(idEquipo=idEquipo)

#       promedioReporteDiseno = 0
#       promedioRubricaPresentaciones = 0
#       promedioAceleracionFrenado = 0
#       promedioRubricaManiobrabilidad = 0
#       promedioHillTraction = 0
#       promedioRubricaResistencia = 0

#       mayorTiempoCircuito = 0
#       mayorTiempoAceleracion = 0

#       # Obtener el total de pruebas de cada tipo para sacar el promedio
#       totalReporteDiseno = 0
#       totalRubricaPresentaciones = 0
#       totalAceleracionFrenado = 0
#       totalRubricaManiobrabilidad = 0
#       totalHillTraction = 0
#       totalRubricaResistencia = 0

#       # Obtener el mayor tiempo de cada tipo de prueba
#       mayorTiempoCircuito = 0
#       mayorTiempoAceleracion = 0

#       # Sacar el promedio de cada tipo de prueba
#       for prueba in pruebas:
#         # Sacar el promedio de cada tipo de prueba
#         promedioReporteDiseno += prueba.reporteDiseno
#         promedioRubricaPresentaciones += prueba.rubricaPresentaciones
#         promedioAceleracionFrenado += prueba.aceleracionFrenado
#         promedioRubricaManiobrabilidad += prueba.rubricaManiobrabilidad
#         promedioHillTraction += prueba.hillTraction
#         promedioRubricaResistencia += prueba.rubricaResistencia

#         # Sacar el mayor tiempo de cada tipo de prueba
#         if prueba.circuitoPrimeraVez > mayorTiempoCircuito:
#           mayorTiempoCircuito = prueba.circuitoPrimeraVez
#         if prueba.circuitoSegundaVez > mayorTiempoCircuito:
#           mayorTiempoCircuito = prueba.circuitoSegundaVez
#         if prueba.aceleracionPrimeraVez > mayorTiempoAceleracion:
#           mayorTiempoAceleracion = prueba.aceleracionPrimeraVez
#         if prueba.aceleracionSegundaVez > mayorTiempoAceleracion:
#           mayorTiempoAceleracion = prueba.aceleracionSegundaVez

#         # Obtener el total de pruebas de cada tipo para sacar el promedio
#         totalReporteDiseno += 1
#         totalRubricaPresentaciones += 1
#         totalAceleracionFrenado += 1
#         totalRubricaManiobrabilidad += 1
#         totalHillTraction += 1
#         totalRubricaResistencia += 1

#       # Sacar el promedio de cada tipo de prueba
#       promedioReporteDiseno = promedioReporteDiseno / totalReporteDiseno
#       promedioRubricaPresentaciones = promedioRubricaPresentaciones / \
#         totalRubricaPresentaciones
#       promedioAceleracionFrenado = promedioAceleracionFrenado / totalAceleracionFrenado
#       promedioRubricaManiobrabilidad = promedioRubricaManiobrabilidad / \
#         totalRubricaManiobrabilidad
#       promedioHillTraction = promedioHillTraction / totalHillTraction
#       promedioRubricaResistencia = promedioRubricaResistencia / totalRubricaResistencia

#       # Guardar los promedios en la tabla puntaje
#       puntaje = Puntaje.objects.get(idEquipo=idEquipo)
#       puntaje.promedioReporteDiseno = promedioReporteDiseno
#       puntaje.promedioRubricaPresentaciones = promedioRubricaPresentaciones
#       puntaje.promedioAceleracionFrenado = promedioAceleracionFrenado
#       puntaje.promedioRubricaManiobrabilidad = promedioRubricaManiobrabilidad
#       puntaje.promedioHillTraction = promedioHillTraction
#       puntaje.promedioRubricaResistencia = promedioRubricaResistencia
#       puntaje.mayorTiempoCircuito = mayorTiempoCircuito
#       puntaje.mayorTiempoAceleracion = mayorTiempoAceleracion
#       puntaje.save()

#       return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#     except Exception as e:
#       Error.objects.create(error=str(e))
#       return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
