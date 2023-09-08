# Importaciones Django
from django.db import models
# Importaciones locales
from apps.rubrica.models import Rubrica


class Prueba(models.Model):
  tipoPruebaOpciones = (
    ('check', 'Check'),
    ('manual', 'Manual'),
  )

  nombre = models.CharField(max_length=250)
  tipoPrueba = models.CharField(max_length=250, choices=tipoPruebaOpciones, default='manual')
  puntaje = models.IntegerField(default=0, blank=True, null=True)
  idRubrica = models.ForeignKey(Rubrica, on_delete=models.CASCADE)

  def __str__(self):
    return self.nombre


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error