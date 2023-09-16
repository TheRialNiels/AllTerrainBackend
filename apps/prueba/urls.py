# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import ObtenerPruebaPorUsuarioYEquipo


router = DefaultRouter()
router.register('obtener-prueba', ObtenerPruebaPorUsuarioYEquipo, basename='obtener-prueba')

urlpatterns = [
  path('', include(router.urls)),
]