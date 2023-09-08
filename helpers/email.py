from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from decouple import config


def recoveryPassword(data):
  context = {
    'email': data['email'],
    'codeVerification': data['codeVerification'],
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
