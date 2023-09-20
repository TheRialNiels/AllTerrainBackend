# Generated by Django 4.2.4 on 2023-09-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puntaje', '0003_puntaje_totalpuntaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puntaje',
            name='promedioHillTraction',
        ),
        migrations.RemoveField(
            model_name='puntaje',
            name='promedioRubricaManiobrabilidad',
        ),
        migrations.AddField(
            model_name='puntaje',
            name='menorTiempoHillTraction',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='puntaje',
            name='menorTiempoManiobrabilidad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]