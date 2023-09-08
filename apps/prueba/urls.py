# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Prueba


router = DefaultRouter()
router.register('prueba', Prueba, basename='prueba')

urlpatterns = [
  path('', include(router.urls)),
]