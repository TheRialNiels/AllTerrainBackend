# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import ActualizarPuntaje


router = DefaultRouter()
router.register('actualizar-puntaje', ActualizarPuntaje, basename='actualizar-puntaje')

urlpatterns = [
  path('', include(router.urls)),
]