# Importaciones Django
from django.db import models


class Equipo(models.Model):
  nombreEquipo = models.CharField(max_length=250)
  puntaje = models.IntegerField(default=0, blank=True, null=True)
  status = models.BooleanField(default=True)

  def __str__(self):
    return self.nombreEquipo


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error
