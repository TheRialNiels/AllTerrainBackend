# Generated by Django 4.2.4 on 2023-09-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0004_alter_prueba_aceleracionfrenado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='aceleracionFrenado',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='hillTraction',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='reporteDiseno',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='rubricaManiobrabilidad',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='rubricaPresentaciones',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='rubricaResistencia',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
