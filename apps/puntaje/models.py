# Importaciones Django
from django.db import models
# Importaciones locales
from apps.equipo.models import Equipo


class Puntaje(models.Model):
  idEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True, related_name='puntajes')

  promedioReporteDiseno = models.FloatField(blank=True, null=True)
  promedioRubricaPresentaciones = models.FloatField(blank=True, null=True)
  promedioAceleracionFrenado = models.FloatField(blank=True, null=True)
  promedioRubricaResistencia = models.FloatField(blank=True, null=True)

  menorTiempoCircuito = models.CharField(max_length=50, blank=True, null=True)
  menorTiempoAceleracion = models.CharField(max_length=50, blank=True, null=True)
  menorTiempoHillTraction = models.CharField(max_length=50, blank=True, null=True)
  menorTiempoManiobrabilidad = models.CharField(max_length=50, blank=True, null=True)

  totalPuntaje = models.FloatField(blank=True, null=True)

  def __str__(self):
    return self.idEquipo.nombreEquipo


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error