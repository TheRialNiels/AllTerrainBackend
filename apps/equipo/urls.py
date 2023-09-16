# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import EquipoViewset, EquipoByUser


router = DefaultRouter()
router.register('equipo', EquipoViewset, basename='equipo')
router.register('equipo-by-user', EquipoByUser, basename='equipo-by-user')

urlpatterns = [
  path('', include(router.urls)),
]
