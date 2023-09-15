# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Equipo, EquipoUsuario


router = DefaultRouter()
router.register('equipo', Equipo, basename='equipo')
router.register('equipo-usuario', EquipoUsuario, basename='equipo-usuario')

urlpatterns = [
  path('', include(router.urls)),
]
