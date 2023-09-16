# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Equipo, EquipoByUser


router = DefaultRouter()
router.register('equipo', Equipo, basename='equipo')

urlpatterns = [
  path('equipo-by-user/', EquipoByUser.as_view(), name='equipo-by-user'),
  path('', include(router.urls)),
]
