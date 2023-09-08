# Importaciones Django
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Importaciones locales
from .views import Universidad


router = DefaultRouter()
router.register('universidad', Universidad, basename='universidad')

urlpatterns = [
  path('', include(router.urls)),
]