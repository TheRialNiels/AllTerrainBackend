# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Asesor


router = DefaultRouter()
router.register('asesor', Asesor, basename='asesor')

urlpatterns = [
  path('', include(router.urls)),
]