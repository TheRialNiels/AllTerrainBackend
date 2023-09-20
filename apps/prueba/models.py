# Importaciones Django
from django.db import models
# Importaciones locales
from apps.equipo.models import Equipo
from apps.authentication.models import UserAccount


class Prueba(models.Model):
  idEquipo = models.ForeignKey(
    Equipo, on_delete=models.CASCADE, blank=True, null=True, related_name='pruebas')
  idUsuario = models.ForeignKey(
    UserAccount, on_delete=models.CASCADE, blank=True, null=True)

  escrutinioSeguridad = models.BooleanField(
    default=False, blank=True, null=True)

  rubricaPresentaciones = models.FloatField(blank=True, null=True, default="0.0")
  aceleracionFrenado = models.FloatField(blank=True, null=True, default="0.0")
  rubricaResistencia = models.FloatField(blank=True, null=True, default="0.0")

  circuitoPrimeraVez = models.CharField(max_length=50, blank=True, null=True, default="0.0")
  circuitoSegundaVez = models.CharField(max_length=50, blank=True, null=True, default="0.0")
  aceleracionPrimeraVez = models.CharField(
    max_length=50, blank=True, null=True, default="0.0")
  aceleracionSegundaVez = models.CharField(
    max_length=50, blank=True, null=True, default="0.0")
  hillTractionPrimeraVez = models.CharField(max_length=50, blank=True, null=True, default="0.0")
  hillTractionSegundaVez = models.CharField(max_length=50, blank=True, null=True, default="0.0")
  maniobrabilidadPrimeraVez = models.CharField(max_length=50, blank=True, null=True, default="0.0")
  maniobrabilidadSegundaVez = models.CharField(max_length=50, blank=True, null=True, default="0.0")

  rubricaPresentacionesCalificado = models.BooleanField(blank=True, null=True, default=False)
  aceleracionFrenadoCalificado = models.BooleanField(blank=True, null=True, default=False)
  rubricaManiobrabilidadCalificado = models.BooleanField(blank=True, null=True, default=False)
  hillTractionCalificado = models.BooleanField(blank=True, null=True, default=False)
  rubricaResistenciaCalificado = models.BooleanField(blank=True, null=True, default=False)

  circuitoCalificado = models.BooleanField(blank=True, null=True, default=False)
  aceleracionCalificado = models.BooleanField(blank=True, null=True, default=False)

  def __str__(self):
    return self.idEquipo.nombreEquipo

  class Meta:
    unique_together = ('idUsuario', 'idEquipo')


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error
