# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Encargado


router = DefaultRouter()
router.register('encargado', Encargado, basename='encargado')

urlpatterns = [
  path('', include(router.urls)),
]