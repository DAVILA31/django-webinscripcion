from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Alumno, Curp, Alumnogg, Ficha_medica, Ficha_medica_visual, Ficha_medica_dental, Ficha_medica_auditiva, Alumno_bajo_tratamiento, Acta_nacimiento,Alumno_convivencia,Datos_familiares, Discapacidad, Aptitud_sobresaliente, Responsable, Archivo

# Register your models here.
@admin.register(Curp)
class CurpAdmin(ImportExportModelAdmin):
    list_display=('user','curp_ap_paterno','curp_ap_materno')
    pass

@admin.register(Alumno)
class AlumnoAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','alumno_municipio','alumno_colonia')
    pass

@admin.register(Alumnogg)
class AlumnoggAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','alumnogg_turno','alumnogg_grupo')
    pass

@admin.register(Ficha_medica)
class Ficha_medicaAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','fmedica_servicio_medico','fmedica_es_alergico_medicamento')
    pass

@admin.register(Ficha_medica_visual)
class Ficha_medica_visualAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','fvisual_usa_lentes')
    pass

@admin.register(Ficha_medica_dental)
class Ficha_medica_dentalAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','fdental_tiene_caries')
    pass

@admin.register(Ficha_medica_auditiva)
class Ficha_medica_auditivaAdmin(ImportExportModelAdmin):
    list_display=('pk_curp', 'fauditiva_agudeza_oido_izquierdo')
    pass

@admin.register(Alumno_bajo_tratamiento)
class Alumno_bajo_tratamientoAdmin(ImportExportModelAdmin):
    list_display=('pk_curp', 'atratamiento_tiene_obesidad')
    pass

@admin.register(Acta_nacimiento)
class Acta_nacimientoAdmin(ImportExportModelAdmin):
    list_display=('pk_curp', 'acta_nacimiento_año_registro')
    pass

@admin.register(Datos_familiares)
class Datos_familiaresAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','pcasa_padres')
    pass

@admin.register(Alumno_convivencia)
class Alumno_convivenciaAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','pconvive_padres')
    pass

@admin.register(Discapacidad)
class DiscapacidadAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','discapacidad_tiene_problema_comunicacion_lenguaje')
    pass

@admin.register(Aptitud_sobresaliente)
class Aptitud_sobresalienteAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','aptitud_creativa')
    pass

@admin.register(Responsable)
class ResponsableAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','pk_responsable_curp')
    pass

@admin.register(Archivo)
class ArchivoAdmin(ImportExportModelAdmin):
    list_display=('pk_curp','created')
    pass

