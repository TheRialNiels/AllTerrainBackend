# Importaciones Django
from django.db import models


class Rubrica(models.Model):
  descripcion = models.TextField()
  puntaje = models.IntegerField(default=0, blank=True, null=True)

  def __str__(self):
    return self.descripcion


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error