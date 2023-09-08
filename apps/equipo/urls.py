# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Equipo


router = DefaultRouter()
router.register('equipo', Equipo, basename='equipo')

urlpatterns = [
  path('', include(router.urls)),
]
