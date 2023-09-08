# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Rubrica


router = DefaultRouter()
router.register('rubrica', Rubrica, basename='rubrica')

urlpatterns = [
  path('', include(router.urls)),
]