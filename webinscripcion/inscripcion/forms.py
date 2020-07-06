from django import forms
from .models import Alumno, Alumnogg, Alumno_bajo_tratamiento,Ficha_medica, Ficha_medica_dental, Ficha_medica_visual, Ficha_medica_auditiva, Alumno_convivencia , Aptitud_sobresaliente, Discapacidad, Datos_familiares, Acta_nacimiento, Responsable, Archivo

class AlumnoForm(forms.ModelForm): 

    class Meta: 
        model= Alumno
        fields=[ 'pk_curp','alumno_nom_esc',
                'alumno_fecha_nacimiento','alumno_sexo','alumno_calle',
                'alumno_num_int','alumno_num_ext','alumno_colonia',
                'alumno_cp','alumno_telefono','alumno_nacionalidad',
                'alumno_entidad','alumno_municipio','alumno_localidad' 
        ]
        
        widgets = {
                'alumno_fecha_nacimiento' : forms.DateInput(attrs={'class':'form-input'}), 
                'alumno_sexo' :forms.TextInput(attrs={'class':'form-input', 'placeholder' :'SEXO'}),
                'alumno_calle' : forms.TextInput(attrs={'class':'form-input', 'placeholder' :'NOMBRE DE LA CALLE','style':'text-transform:uppercase;'}),
                'alumno_num_int': forms.TextInput(attrs={'class':'form2-input', 'placeholder' :'NUM. INTERIOR','style':'text-transform:uppercase;'}),
                'alumno_num_ext' : forms.TextInput(attrs={'class':'form2-input', 'placeholder' :'NUM. EXTERIOR','style':'text-transform:uppercase;'}),
                'alumno_colonia' : forms.TextInput(attrs={'class':'form-input', 'placeholder' :'NOMBRE DE LA COLONIA','style':'text-transform:uppercase;'}),
                'alumno_cp' : forms.TextInput(attrs={'class':'form2-input', 'placeholder' :'CP'}),
                'alumno_telefono' : forms.TextInput(attrs={'class':'form-input', 'placeholder':'TELEFONO','pattern':"[0-9]{10}"}),
                'alumno_nacionalidad' :forms.TextInput(attrs={'class':'form-input', 'placeholder':'NACIONALIDAD','style':'text-transform:uppercase;'}),
                'alumno_entidad' :forms.TextInput(attrs={'class':'form-input', 'placeholder':'NOMBRE DE LA ENTIDAD','style':'text-transform:uppercase;'}),
                'alumno_municipio' :forms.TextInput(attrs={'class':'form-input', 'placeholder':'NOMBRE DEL MUNICIPIO','style':'text-transform:uppercase;'}),
                'alumno_localidad' :forms.TextInput(attrs={'class':'form-input', 'placeholder':'NOMBRE DE LA LOCALIDAD','style':'text-transform:uppercase;'}),
            }    

class AlumnoggForm(forms.ModelForm): 

    class Meta: 
        model= Alumnogg
        fields=[ 'pk_curp', 'alumnogg_grupo','alumnogg_turno','alumnogg_grado',
                'alumnogg_ciclo_escolar','alumnogg_promedio'
        ]
        widgets={
            'alumnogg_grupo': forms.TextInput(attrs={'class':'form-input', 'placeholder':'GRUPO'}),
            'alumnogg_turno': forms.TextInput(attrs={'class':'form-input', 'placeholder':'TURNO'}),
            'alumnogg_grado': forms.TextInput(attrs={'class':'form-input', 'placeholder':'GRADO'}),
            'alumnogg_ciclo_escolar': forms.TextInput(attrs={'class':'form-input', 'placeholder':'CICLO ESCOLAR'}),
            'alumnogg_promedio': forms.TextInput(attrs={'class':'form-input', 'placeholder':'PROMEDIO'}),
        }

class FichamedicaForm(forms.ModelForm): 

    class Meta: 
        model= Ficha_medica
        fields=[ 'pk_curp', 'fmedica_talla','fmedica_peso','fmedica_medida_cintura','fmedica_medida_cadera',
                'fmedica_tipo_sangre','fmedica_servicio_medico','fmedica_educacion_especial','fmedica_es_alergico_medicamento',
                'fmedica_cual_medicamento','fmedica_es_alergico_alimento','fmedica_cual_alimento', 'fmedica_problema_postural','fmedica_usa_aparato_ortopedico'
        ]
        widgets={            
            'fmedica_talla': forms.TextInput(attrs={'class':'form-input', 'placeholder':'ALTURA'}),
            'fmedica_peso': forms.TextInput(attrs={'class':'form-input', 'placeholder':'PESO'}),
            'fmedica_medida_cintura': forms.TextInput(attrs={'class':'form-input', 'placeholder':'MEDIDA DE LA CINTURA'}),
            'fmedica_medida_cadera': forms.TextInput(attrs={'class':'form-input', 'placeholder':'MEDIDA DE LA CADERA'}),
            'fmedica_tipo_sangre': forms.TextInput(attrs={'class':'form-input', 'placeholder':'TIPO DE SANGRE'}),
            'fmedica_servicio_medico': forms.TextInput(attrs={'class':'form-input', 'placeholder':'SERVICIO MEDICO'}),
            'fmedica_educacion_especial': forms.TextInput(attrs={'class':'form-input', 'placeholder':'EDUCACION ESPECIAL'}),
            'fmedica_es_alergico_medicamento': forms.TextInput(attrs={'class':'form-input', 'placeholder':'¿ES ALERGICO A MEDICAMENTOS?'}),
            'fmedica_cual_medicamento': forms.TextInput(attrs={'class':'form-input', 'placeholder':'¿CUÁL MEDICAMENTO?'}),
            'fmedica_es_alergico_alimento': forms.TextInput(attrs={'class':'form-input', 'placeholder':'¿ES ALERGICO A ALGÚN ALIMENTO?'}),
            'fmedica_cual_alimento': forms.TextInput(attrs={'class':'form-input', 'placeholder':'¿QUÉ ALIMENTO(S)?'}),
            'fmedica_problema_postural':forms.TextInput(attrs={'class':'form-input'}),
            'fmedica_usa_aparato_ortopedico':forms.TextInput(attrs={'class':'form-input'})
        }

class FichamedicavisualForm(forms.ModelForm): 

    class Meta: 
        model= Ficha_medica_visual
        fields=[ 'pk_curp', 'fvisual_ojo_izquierdo_num_linea','fvisual_ojo_derecho_num_linea',
                'fvisual_usa_lentes'
        ]
        widgets={
                'pk_curp':forms.TextInput(attrs={'class':'form-input', 'placeholder':'CURP'}),
                'fvisual_ojo_izquierdo_num_linea': forms.TextInput(attrs={'class':'form-input'}),
                'fvisual_ojo_derecho_num_linea':forms.TextInput(attrs={'class':'form-input'}),
                'fvisual_usa_lentes':forms.TextInput(attrs={'class':'form-input'}),
        }


class FichamedicadentalForm(forms.ModelForm): 

    class Meta: 
        model= Ficha_medica_dental
        fields=[ 'pk_curp','fdental_tiene_caries','fdental_numero_caries',
                'fdental_tiene_inflamacion_o_sangrado_al_cepillarse','fdental_tiene_dientes_chuecos_malaposicion'
        ]
        widgets={
                'pk_curp':forms.TextInput(attrs={'class':'form-input'}),
                'fdental_tiene_caries':forms.TextInput(attrs={'class':'form-input'}),
                'fdental_numero_caries':forms.TextInput(attrs={'class':'form-input'}),
                'fdental_tiene_inflamacion_o_sangrado_al_cepillarse':forms.TextInput(attrs={'class':'form-input'}),
                'fdental_tiene_dientes_chuecos_malaposicion':forms.TextInput(attrs={'class':'form-input'})
        }

class FichamedicaauditivaForm(forms.ModelForm):
    class Meta: 
        model=Ficha_medica_auditiva
        fields=['pk_curp','fauditiva_agudeza_oido_izquierdo','fauditiva_agudeza_oido_derecho',
                'fauditiva_usa_aparato_oido_izquierdo' ,'fauditiva_usa_aparato_oido_derecho'
        ]
        widgets={
                'fauditiva_agudeza_oido_izquierdo':forms.TextInput(attrs={'class':'form-input'}),
                'fauditiva_agudeza_oido_derecho':forms.TextInput(attrs={'class':'form-input'}),
                'fauditiva_usa_aparato_oido_izquierdo':forms.TextInput(attrs={'class':'form-input'}),
                'fauditiva_usa_aparato_oido_derecho':forms.TextInput(attrs={'class':'form-input'})
        }

class AlumnobajotratamientoForm(forms.ModelForm):
    class Meta:
        model=Alumno_bajo_tratamiento
        fields=['pk_curp','atratamiento_tiene_cardiopatias', 'atratamiento_tiene_hipertension', 'atratamiento_tiene_cancer', 'atratamiento_tiene_diabetes',
        'atratamiento_tiene_obesidad', 'atratamiento_tiene_desnutricion','atratamiento_tiene_VIH_sida','atratamiento_tiene_asma',
        'atratamiento_tiene_depresion', 'atratamiento_tiene_lupus', 'atratamiento_tiene_insuficiencia_renal', 'atratamiento_tiene_artritis', 'atratamiento_tiene_epilepsia_o_convulsiones',
        'atratamiento_tiene_tuberculosis', 'atratamiento_tiene_otras_enfermedades_cronicas'

        ]

        widgets={
            'atratamiento_tiene_cardiopatias':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_hipertension':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_cancer':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_diabetes':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_obesidad':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_desnutricion':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_VIH_sida':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_asma':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_depresion':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_lupus':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_insuficiencia_renal':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_artritis':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_epilepsia_o_convulsiones':forms.TextInput(attrs={'class':'form-input'}),
            'atratamiento_tiene_tuberculosis':forms.TextInput(attrs={'class':'form-input'}), 
            'atratamiento_tiene_otras_enfermedades_cronicas':forms.TextInput(attrs={'class':'form-input'})
        }

class ActanForm(forms.ModelForm):
    class Meta:
        model=Acta_nacimiento
        fields=[ 'pk_curp','acta_nacimiento_numero_control_o_folio', 'acta_nacimiento_numero_libro',
        'acta_nacimiento_año_registro','acta_nacimiento_numero_acta','acta_nacimiento_folio_curp'
        ]
        widgets={
                'pk_curp':forms.TextInput(attrs={'class':'form-input'}),
                'acta_nacimiento_numero_control_o_folio':forms.TextInput(attrs={'class':'form-input'}),
                'acta_nacimiento_numero_libro':forms.TextInput(attrs={'class':'form-input'}),
                'acta_nacimiento_año_registro':forms.TextInput(attrs={'class':'form-input'}),
                'acta_nacimiento_numero_acta':forms.TextInput(attrs={'class':'form-input'}),
                'acta_nacimiento_folio_curp':forms.TextInput(attrs={'class':'form-input'})
        }


class DatosfamiliaresForm(forms.ModelForm):
    class Meta: 
        model=Datos_familiares
        fields=['pk_curp','pcasa_padres', 'pcasa_madre','pcasa_padre', 'pcasa_hermanos',
                'pcasa_abuelos', 'pcasa_tios', 'pcasa_otro','pcasa_solo'
        ]
        widgets={
                'pk_curp':forms.TextInput(attrs={'class':'form-input'}),
                'pcasa_padres':forms.TextInput(attrs={'class':'form-input'}),
                'pcasa_madre':forms.TextInput(attrs={'class':'form-input'}),
                'pcasa_padre':forms.TextInput(attrs={'class':'form-input'}),
                'pcasa_hermanos':forms.TextInput(attrs={'class':'form-input'}),
                'pcasa_abuelos':forms.TextInput(attrs={'class':'form-input'}),
                'pcasa_tios':forms.TextInput(attrs={'class':'form-input'}),
                'pcasa_otros':forms.TextInput(attrs={'class':'form-input'}),
                'pcasa_solo':forms.TextInput(attrs={'class':'form-input'})
                

        }

class AlumnoconvivenciaForm(forms.ModelForm):
    class Meta: 
        model=Alumno_convivencia
        fields=['pk_curp','pconvive_padres','pconvive_madre', 'pconvive_padre','pconvive_hermanos',
                'pconvive_abuelos','pconvive_tios','pconvive_otro','pconvive_solo','pconvive_numero_hermanos',
                'pconvive_lugar_entre_hermanos','pconvive_actividad_dedica_mas_tiempo'
        ]

class DiscapacidadForm(forms.ModelForm):
    class Meta: 
        model= Discapacidad
        fields=[ 'pk_curp', 'discapacidad_tiene_autismo','discapacidad_tiene_baja_vision', 'discapacidad_tiene_ceguera',
                'discapacidad_intelectual', 'discapacidad_motriz', 'discapacidad_multiple', 'discapacidad_tiene_baja_audicion',
                'discapacidad_mental', 'discapacidad_tiene_problema_comunicacion_lenguaje', 'discapacidad_tiene_problema_conducta',
                'discapacidad_tiene_sordera', 'discapacidad_tiene_sordoceguera', 'discapacidad_tiene_transtorno_del_desarrollo',
                'discapacidad_tiene_transtorno_deficit_atencion_hiperactividad'
        ]

class AptitudsobresalienteForm(forms.ModelForm):
    class Meta:
        model=Aptitud_sobresaliente
        fields=['pk_curp', 'aptitud_intelectual','aptitud_psicomotriz',
                'aptitud_socioafectiva', 'aptitud_creativa'
        ]

class ResponsableForm(forms.ModelForm):
    class Meta:
        model= Responsable 
        fields=[ 'pk_curp','pk_responsable_curp', 'responsable_parentesco',
                'responsable_ap_paterno','responsable_ap_materno','responsable_nombre',
                'responsable_fecha_nacimiento','responsable_correo','responsable_telefono',
                'responsable_ocupacion','responsable_nivel_estudio'
        ]
        widgets = {
            'pk_responsable_curp': forms.TextInput(attrs={'class':'form-input','pattern':"[A-Z]{4}[0-9]{6}[A-Z]{6}[0-9]{2}"}),
            'responsable_parentesco': forms.TextInput(attrs={'class':'form-input', 'placeholder' :'PARENTESCO'}),
            'responsable_ap_paterno' : forms.TextInput(attrs={'class':'form-input', 'placeholder' :'APELLIDO PATERNO','style':'text-transform:uppercase;'}),
            'responsable_ap_materno'  : forms.TextInput(attrs={'class':'form-input', 'placeholder' :'APELLIDO MATERNO','style':'text-transform:uppercase;'}),
            'responsable_nombre'  : forms.TextInput(attrs={'class':'form-input', 'placeholder' :'NOMBRE','style':'text-transform:uppercase;'}),
            'responsable_fecha_nacimiento' : forms.DateInput(attrs={'class':'form-input'}),
            'responsable_telefono' : forms.TextInput(attrs={'class':'form-input','pattern':"[0-9]{10}"}),
            'responsable_correo': forms.EmailInput(attrs={'class':'form-input','style':'text-transform:uppercase;','list':"defaultEmails"}), 
            'responsable_ocupacion'  : forms.TextInput(attrs={'class':'form-input', 'placeholder' :'OCUPACION'}),    
            'responsable_nivel_estudio' : forms.TextInput(attrs={'class':'form-input', 'placeholder' :'ESCOLARIDAD'}),
        }
        
class ArchivoForm (forms.ModelForm):
    class Meta: 
        model=Archivo
        fields=['pk_curp', 'archivo_curp', 'archivo_acta_nacimiento',
                'archivo_certificado_primaria','archivo_boleta_sexto'
        ]