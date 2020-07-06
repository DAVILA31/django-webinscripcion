# Generated by Django 3.0.5 on 2020-07-02 05:00

from django.db import migrations, models
import django.db.models.deletion
import inscripcion.models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0006_auto_20200701_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('pk_responsable_curp', inscripcion.models.UpperCaseCharField(max_length=18, primary_key=True, serialize=False, verbose_name='CURP DEL RESPONSABLE')),
                ('responsable_parentesco', inscripcion.models.UpperCaseCharField(max_length=6, verbose_name='PARENTESCO')),
                ('responsable_ap_paterno', inscripcion.models.UpperCaseCharField(max_length=45, verbose_name='APELLIDO PATERNO')),
                ('responsable_ap_materno', inscripcion.models.UpperCaseCharField(max_length=45, verbose_name='APELLIDO MATERNO')),
                ('responsable_nombre', inscripcion.models.UpperCaseCharField(max_length=45, verbose_name='NOMBRE')),
                ('responsable_fecha_nacimiento', models.DateField(verbose_name='FECHA DE NACIMIENTO')),
                ('responsable_correo', models.EmailField(max_length=254, verbose_name='CORREO ELECTRONICO')),
                ('responsable_telefono', inscripcion.models.UpperCaseCharField(max_length=10, verbose_name='TELEFONO')),
                ('responsable_nivel_estudio', inscripcion.models.UpperCaseCharField(choices=[('NINGUNA', 'NINGUNA'), ('PRIMARIA', 'PRIMARIA'), ('SECUNDARIA', 'SECUNDARIA'), ('BACHILLERATO', 'BACHILLERATO'), ('TECNICO', 'TECNICO'), ('PROFESIONAL', 'PROFESIONAL'), ('POSGRADO', 'POSGRADO')], max_length=12, verbose_name='NIVEL DE ESTUDIOS')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='FECHA DE CREACION')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='FECHA DE EDICION')),
                ('pk_curp', models.ForeignKey(max_length=18, on_delete=django.db.models.deletion.ProtectedError, to='inscripcion.Curp', verbose_name='CURP DEL ALUMNO')),
            ],
            options={
                'verbose_name': 'Responsable',
                'verbose_name_plural': 'Responsables',
                'db_table': 'responsable',
                'ordering': ['pk_curp', 'pk_responsable_curp'],
            },
        ),
    ]