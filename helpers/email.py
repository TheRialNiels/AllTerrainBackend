from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from decouple import config


def temporalPassword(data):
  context = {
    'email': data['email'],
    'password': data['password'],
  }
  template = get_template('temporalPassword.html')
  content = template.render(context)
  email = EmailMultiAlternatives(
    'Contraseña temporal',
    '',
    config('EMAIL_HOST_USER'),
    [data['email']],
  )
  email.attach_alternative(content, 'text/html')
  email.send()


def recoveryPassword(data):
  context = {
    'email': data['email'],
    'recuperationCode': data['recuperationCode'],
  }
  template = get_template('recoveryPassword.html')
  content = template.render(context)
  email = EmailMultiAlternatives(
    'Recuperacion de contraseña',
    '',
    config('EMAIL_HOST_USER'),
    [data['email']],
  )
  email.attach_alternative(content, 'text/html')
  email.send()


def sendAuthenticationCode(email, code):
  context = {
    'email': email,
    'code': code,
  }
  template = get_template('authenticationCode.html')
  content = template.render(context)
  email = EmailMultiAlternatives(
    'Codigo de autenticacion',
    '',
    config('EMAIL_HOST_USER'),
    [email],
  )
  email.attach_alternative(content, 'text/html')
  email.send()
