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

  reporteDiseno = models.FloatField(blank=True, null=True)
  rubricaPresentaciones = models.FloatField(blank=True, null=True)
  aceleracionFrenado = models.FloatField(blank=True, null=True)
  rubricaManiobrabilidad = models.FloatField(blank=True, null=True)
  hillTraction = models.FloatField(blank=True, null=True)
  rubricaResistencia = models.FloatField(blank=True, null=True)

  circuitoPrimeraVez = models.CharField(max_length=50, blank=True, null=True)
  circuitoSegundaVez = models.CharField(max_length=50, blank=True, null=True)
  aceleracionPrimeraVez = models.CharField(
    max_length=50, blank=True, null=True)
  aceleracionSegundaVez = models.CharField(
    max_length=50, blank=True, null=True)

  def __str__(self):
    return self.idEquipo.nombreEquipo

  class Meta:
    unique_together = ('idUsuario', 'idEquipo')


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error
