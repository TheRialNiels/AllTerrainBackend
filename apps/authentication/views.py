# Django Imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
# Rest Framework Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# Other Imports
import secrets
# Local Imports
from helpers.email import recoveryPassword
from .serializer import UserAccountSerializer
from .models import Errors

User = get_user_model()


class UserAccountCreateView(APIView):
  permission_classes = (IsAuthenticated,)

  def post(self, request):
    try:
      email = request.data.get('email')
      password = secrets.token_hex(10)
      username = request.data.get('username')
      user = User.objects.filter(email=email).first()
      if user:
        return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
      else:
        user = User.objects.create_user(
          email=email, password=password, username=username)
        data = {
          'email': email,
          'password': password,
        }
        # validateUser(data)
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserAccountLoginView(APIView):
  def post(self, request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    user = authenticate(email=email, password=password)
    if user and user.is_active:
      login(request, user)
      Token.objects.filter(user=user).delete()
      token, _ = Token.objects.get_or_create(user=user)
      return Response({'token': token.key}, status=status.HTTP_200_OK)
    elif user and not user.is_active:
      return Response({'error': 'La cuenta está desactivada'}, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response({'error': 'Correo o contraseña inválidos'}, status=status.HTTP_400_BAD_REQUEST)


class UserAccountLogoutView(APIView):
  permission_classes = (IsAuthenticated,)

  def post(self, request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


class RecoveryUserPassword(APIView):
  def post(self, request):
    try:
      email = request.data.get('email')
      user = User.objects.filter(email=email).first()
      if user and user.is_active:
        user.codeVerification = secrets.token_hex(2)
        user.codeVerification = user.codeVerification.upper()
        user.save()
        data = {
          'email': email,
          'codeVerification': user.codeVerification,
        }
        recoveryPassword(data)
        return Response(status=status.HTTP_200_OK)
      else:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserAccountChangePasswordView(APIView):
  def post(self, request):
    user = User.objects.filter(email=request.data.get('email')).first()
    code = request.data.get('code')
    password = request.data.get('password')
    newPassword = request.data.get('confirmPassword')

    if user.codeVerification != code:
      return Response({'error': 'Código de verificación inválido'}, status=status.HTTP_400_BAD_REQUEST)

    if password != newPassword:
      return Response({'error': 'Las contraseñas no coinciden'}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(password)
    user.codeVerification = None
    user.save()
    return Response(status=status.HTTP_200_OK)


class CurrentUser(APIView):
  permission_classes = (IsAuthenticated,)

  def get(self, request):
    try:
      serializer = UserAccountSerializer(request.user)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      Errors.objects.create(error=str(e))
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
