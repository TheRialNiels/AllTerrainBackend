# Django Imports
from django.urls import path, include
# Importaciones rest_framework
from rest_framework.routers import DefaultRouter
# Import Views
from .views import UserAccountCreateView, UserAccountLoginView, UserAccountLogoutView, UserAccountChangePasswordView, RecoveryUserPassword, CurrentUser, GetUsers, UserAccountDeleteView, UserAccountUpdateView, UserAccountCreateEncargadoView

router = DefaultRouter()
router.register('create-encargado', UserAccountCreateEncargadoView, basename='create-encargado')

urlpatterns = [
  path('create-user/', UserAccountCreateView.as_view(), name='create-user'),
  path('login/', UserAccountLoginView.as_view(), name='login'),
  path('logout/', UserAccountLogoutView.as_view(), name='logout'),
  path('change-password/', UserAccountChangePasswordView.as_view(),
       name='change-password'),
  path('recovery-password/', RecoveryUserPassword.as_view(),
       name='recovery-password'),
  path('current-user/', CurrentUser.as_view(), name='current-user'),
  path('get-users/', GetUsers.as_view(), name='get-users'),
  path('update-user/', UserAccountUpdateView.as_view(), name='update-user'),
  path('delete-user/<int:id>/', UserAccountDeleteView.as_view(), name='delete-user'),
  path('', include(router.urls)),
]
