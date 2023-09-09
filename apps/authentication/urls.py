# Django Imports
from django.urls import path, include
# Import Views
from .views import UserAccountCreateView, UserAccountLoginView, UserAccountLogoutView, UserAccountChangePasswordView, RecoveryUserPassword, CurrentUser


urlpatterns = [
  path('create-user/', UserAccountCreateView.as_view(), name='create-user'),
  path('login/', UserAccountLoginView.as_view(), name='login'),
  path('logout/', UserAccountLogoutView.as_view(), name='logout'),
  path('change-password/', UserAccountChangePasswordView.as_view(),
       name='change-password'),
  path('recovery-password/', RecoveryUserPassword.as_view(),
       name='recovery-password'),
  path('current-user/', CurrentUser.as_view(), name='current-user'),
]
