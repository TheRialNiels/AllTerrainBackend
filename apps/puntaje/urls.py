# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Puntaje


router = DefaultRouter()
router.register('puntaje', Puntaje, basename='puntaje')

urlpatterns = [
  path('', include(router.urls)),
]