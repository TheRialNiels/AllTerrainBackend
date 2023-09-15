# Importaciones Django
from django.db import models
# Importaciones locales
from apps.authentication.models import UserAccount
from apps.equipo.models import Equipo


class Encargado(models.Model):
  telefono = models.CharField(max_length=50)
  idUsuario = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
  idEquipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

  objects = models.Manager()

  def __str__(self):
    return self.idUsuario.get_full_name()


class Error(models.Model):
  error = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.error