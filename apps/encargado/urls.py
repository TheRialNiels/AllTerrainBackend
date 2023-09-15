# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Encargado, EncargadoByUser


router = DefaultRouter()
router.register('encargado', Encargado, basename='encargado')

urlpatterns = [
  path('encargado-by-user/', EncargadoByUser.as_view(), name='encargado-by-user'),
  path('', include(router.urls)),
]