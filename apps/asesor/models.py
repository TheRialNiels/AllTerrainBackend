# Importaciones Django
from django.db import models
# Importaciones locales
from apps.equipo.models import Equipo


class Asesor(models.Model):
  tipoAsesorOpcion = (
    ('tecnico', 'Tecnico'),
    ('academico', 'Academico'),
  )

  nombreCompleto = models.CharField(max_length=250)
  tipoAsesor = models.CharField(max_length=50, choices=tipoAsesorOpcion)
  idEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

  def __str__(self):
    return self.nombreCompleto


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error
