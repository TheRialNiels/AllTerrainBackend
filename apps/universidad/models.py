# Importaciones Django
from django.db import models
# Importaciones locales
from apps.equipo.models import Equipo


class Universidad(models.Model):
  nombre = models.CharField(max_length=50)
  direccion = models.CharField(max_length=50)
  idEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.nombre


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error