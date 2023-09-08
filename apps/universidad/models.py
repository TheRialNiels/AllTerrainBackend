# Importaciones Django
from django.db import models


class Universidad(models.Model):
  nombre = models.CharField(max_length=50)
  direccion = models.CharField(max_length=50)

  def __str__(self):
    return self.nombre


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error