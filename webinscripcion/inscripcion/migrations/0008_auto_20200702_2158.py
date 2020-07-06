# Generated by Django 3.0.5 on 2020-07-03 02:58

from django.db import migrations
import inscripcion.models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0007_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_intelectual',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE DISCAPACIDAD INTELECTUAL?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_mental',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE DISCAPACIDAD MENTAL?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_motriz',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE DISCAPACIDAD MOTRIZ?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_multiple',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE DISCAPACIDAD MULTIPLE?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_autismo',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE AUTISMO?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_baja_audicion',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE BAJA AUDICIÓN?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_baja_vision',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE BAJA VISIÓN?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_ceguera',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE CEGUERA?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_problema_comunicacion_lenguaje',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE PROBLEMAS DE COMUNICACION O LENGUAJE?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_problema_conducta',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE PROBLEMAS DE CONDUCTA?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_sordera',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE SORDERA?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_sordoceguera',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE SORDOCEGUERA?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_transtorno_deficit_atencion_hiperactividad',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE TRANSTORNO DE DEFICIT DE ATENCION O HIPERACTIVIDAD?'),
        ),
        migrations.AlterField(
            model_name='discapacidad',
            name='discapacidad_tiene_transtorno_del_desarrollo',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿TIENE TRANSTORNO DEL DESARROLLO?'),
        ),
        migrations.AlterField(
            model_name='ficha_medica',
            name='fmedica_servicio_medico',
            field=inscripcion.models.UpperCaseCharField(blank=True, choices=[('IMSS', 'IMSS'), ('ISSTE', 'ISSTE'), ('ISSFAM', 'ISSFAM'), ('SERVCIO MEDICO DE PEMEX', 'SERVICIO MEDICO DE PEMEX'), ('SEGURO POPULAR', 'SEGURO POPULAR'), ('SIN SEGURO', 'SIN SEGURO'), ('OTRO', 'OTRO')], max_length=25, null=True, verbose_name='SERVICIO MEDICO'),
        ),
    ]