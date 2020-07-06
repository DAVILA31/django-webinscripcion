# Generated by Django 3.0.5 on 2020-07-04 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0010_responsable_responsable_ocupacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo_curp', models.FileField(upload_to='curp/%Y/%m/%D', verbose_name='Archivo CURP')),
                ('archivo_acta_nacimiento', models.FileField(upload_to='actan/%Y/%m/%D', verbose_name='Archivo Acta de Nacimiento')),
                ('archivo_certificado_primaria', models.FileField(upload_to='certificado/%Y/%m/%D', verbose_name='Archivo Certificado Primaria')),
                ('archivo_boleta_sexto', models.FileField(upload_to='Boleta/%Y/%m/%D', verbose_name='Archivo Boleta')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='FECHA DE CREACION')),
                ('pk_curp', models.OneToOneField(max_length=18, on_delete=django.db.models.deletion.CASCADE, to='inscripcion.Curp')),
            ],
            options={
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
                'db_table': 'Archivo',
                'ordering': ['pk_curp', 'created'],
            },
        ),
    ]