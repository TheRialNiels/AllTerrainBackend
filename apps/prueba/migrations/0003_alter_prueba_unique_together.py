# Generated by Django 4.2.4 on 2023-09-16 03:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipo', '0001_initial'),
        ('prueba', '0002_alter_prueba_aceleracionfrenado_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prueba',
            unique_together={('idUsuario', 'idEquipo')},
        ),
    ]
