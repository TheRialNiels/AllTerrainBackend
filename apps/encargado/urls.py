# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import EncargadoViewset, EncargadoByUser


router = DefaultRouter()
router.register('encargado', EncargadoViewset, basename='encargado')
router.register('encargado-by-user', EncargadoByUser, basename='encargado-by-user')

urlpatterns = [
  path('', include(router.urls)),
]