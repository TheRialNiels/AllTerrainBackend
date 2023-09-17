# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import ActualizarPuntaje, ObtenerPuntajes


router = DefaultRouter()
router.register('actualizar-puntaje', ActualizarPuntaje, basename='actualizar-puntaje')
router.register('obtener-puntajes', ObtenerPuntajes, basename='obtener-puntajes')

urlpatterns = [
  path('', include(router.urls)),
]