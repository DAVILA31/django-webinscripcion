# Generated by Django 3.0.5 on 2020-07-03 22:43

from django.db import migrations
import inscripcion.models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0009_auto_20200702_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsable',
            name='responsable_ocupacion',
            field=inscripcion.models.UpperCaseCharField(choices=[('HOGAR', 'HOGAR'), ('DESEMPLEADO', 'DESEMPLEADO'), ('EMPLEADO', 'EMPLEADO'), ('JUBILADO', 'JUBILADO'), ('ESTUDIANTE', 'ESTUDIANTE'), ('JORNALERO', 'JORNALERO'), ('CUENTA PROPIA', 'CUENTA PROPIA'), ('OTRO', 'OTRO')], max_length=13, null=True, verbose_name='OCUPACION'),
        ),
    ]