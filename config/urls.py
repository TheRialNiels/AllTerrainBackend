from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),

  path('api/auth/', include('apps.authentication.urls')),
  path('api/', include('apps.equipo.urls')),
  path('api/', include('apps.prueba.urls')),
  path('api/', include('apps.universidad.urls')),
  path('api/', include('apps.asesor.urls')),
  path('api/', include('apps.encargado.urls')),
  path('api/', include('apps.puntaje.urls')),

  path('api/docs/', include_docs_urls(title='API')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)