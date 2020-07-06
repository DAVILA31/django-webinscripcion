from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UpperCaseCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)

class Curp(models.Model):
        user=models.OneToOneField(User, max_length=18,on_delete=models.CASCADE)
        pk_curp=models.CharField(primary_key=True, max_length=18,verbose_name="CURP")
        curp_ap_paterno =UpperCaseCharField(verbose_name="APELLIDO PATERNO", max_length=45)
        curp_ap_materno = UpperCaseCharField(verbose_name="APELLIDO MATERNO", max_length=45)
        curp_nombre = UpperCaseCharField(verbose_name="NOMBRE", max_length=45)

        created = models.DateTimeField(auto_now_add=True, verbose_name="FECHA DE CREACION")
        updated = models.DateTimeField(auto_now=True, verbose_name="FECHA DE EDICION")
    
        class Meta:
            db_table = "Curp"
            verbose_name = "Curp"
            verbose_name_plural = "Curp de alumnos"
            ordering = ['user', 'curp_ap_paterno']

        def __str__(self):
            return f'{self.user.username}Curp'

class Alumno(models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)
        alumno_nom_esc =UpperCaseCharField(verbose_name="NOMBRE DE LA ESCUELA", max_length=45, default="ESCUELA SECUNDARIA TECNICA INDUSTRIAL No 8")
        alumno_fecha_nacimiento = models.DateField(null=True, blank=True,verbose_name="FECHA DE NACIMIENTO")
        SEXO=(
            ('M','MASCULINO'),
            ('F','FEMENINO'),
        )

        alumno_sexo =UpperCaseCharField(verbose_name="SEXO", choices=SEXO, max_length=1,null=True, blank=True)
        alumno_calle = UpperCaseCharField(verbose_name="NOMBRE DE LA CALLE", max_length=45,null=True, blank=True)
        alumno_num_int= UpperCaseCharField(verbose_name="NUM. INTERIOR", max_length=6,null=True, blank=True) 
        alumno_num_ext = UpperCaseCharField(verbose_name="NUM. EXTERIOR", max_length=6,null=True, blank=True) 
        alumno_colonia = UpperCaseCharField(verbose_name="NOMBRE DE LA COLONIA", max_length=45,null=True, blank=True) 
        alumno_cp = models.CharField (verbose_name="CODIGO POSTAL", max_length=5,null=True, blank=True)
        alumno_telefono = models.CharField(verbose_name="TELEFONO", max_length=10,null=True, blank=True)
        alumno_nacionalidad =UpperCaseCharField(verbose_name="NACIONALIDAD", max_length=45, default="MEXICANA",null=True, blank=True)        
        alumno_entidad =UpperCaseCharField(verbose_name="NOMBRE DE LA ENTIDAD", max_length=45, default="VERACRUZ",null=True, blank=True)        
        alumno_municipio =UpperCaseCharField(verbose_name="NOMBRE DEL MUNICIPIO", max_length=45,null=True, blank=True)        
        alumno_localidad =UpperCaseCharField(verbose_name="NOMBRE DE LA LOCALIDAD", max_length=45,null=True, blank=True) 
             



        class Meta:
            db_table = "Alumno"
            verbose_name = "Alumno"
            verbose_name_plural = "Alumnos"
            ordering = ['pk_curp', 'alumno_colonia']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Alumno'
     


class Alumnogg (models.Model):

        TURNO =(
                ('MATUTINO','MATUTINO'),
                ('VESPERTINO','VESPERTINO'),
            )

        GRADO =(
                ('1','PRIMERO'),
                ('2','SEGUNDO'),
                ('3','TERCERO'),
            )

        LETRA=(
                ('A','A'),
                ('B','B'), 
                ('C','C'),
                ('D','D'),
                ('E','E'),
                ('F','F'),
                ('G','G'),
                ('H','H'),
                ('I','I'),
                ('J','J'),
                ('K','K'),
                ('L','L'),
            )

        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)
        alumnogg_grupo=UpperCaseCharField(verbose_name="LETRA", choices=LETRA, max_length=1)
        alumnogg_turno= UpperCaseCharField(verbose_name="TURNO", choices=TURNO, max_length=10, default='MATUTINO')
        alumnogg_grado= UpperCaseCharField(verbose_name='GRADO',choices=GRADO, max_length=1)
        alumnogg_ciclo_escolar=UpperCaseCharField(verbose_name='CICLO ESCOLAR',max_length=9, default='2020-2021')
        alumnogg_promedio=models.FloatField(verbose_name='PROMEDIO DEL ALUMNO',blank=True, null=True)


        class Meta:
            db_table = "Alumnogg"
            verbose_name = "Grado y Grupo"
            verbose_name_plural = "Grado y Grupo de Alumnos"
            ordering = ['pk_curp', 'alumnogg_grupo']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Alumnogg'

class Ficha_medica(models.Model):
        TIPO_SANGRE=(
                ('O+','O+'),
                ('O-','O-'),
                ('A+','A+'),
                ('A-','A-'),
                ('B+','B+'),
                ('B-','B-'),   
                ('AB+','AB+'),
                ('AB-','AB-'), 
        )

        SERVICIO_MEDICO=(
                ('IMSS','IMSS'),
                ('ISSTE','ISSTE'),
                ('ISSFAM','ISSFAM'),
                ('SERVCIO MEDICO DE PEMEX','SERVICIO MEDICO DE PEMEX'),
                ('SEGURO POPULAR','SEGURO POPULAR'),
                ('SIN SEGURO','SIN SEGURO'),
                ('OTRO','OTRO'),
        )

        OPCION=(
                ('SI','SI'),
                ('NO','NO'),
        )
        

        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        fmedica_talla=models.FloatField(verbose_name='ALTURA EN CM', blank=True ,null=True)
        fmedica_peso=models.FloatField(verbose_name='PESO EN KG', blank=True ,null=True)
        fmedica_medida_cintura=models.FloatField(verbose_name='MEDIDA DE LA CINTURA EN CM.', blank=True ,null=True)
        fmedica_medida_cadera=models.FloatField(verbose_name='MEDIDA DE LA CADERA EN CM', blank=True ,null=True)
        fmedica_tipo_sangre=UpperCaseCharField(verbose_name="TIPO DE SANGRE", choices=TIPO_SANGRE, max_length=3, blank=True, null=True)
        fmedica_servicio_medico=UpperCaseCharField(verbose_name="SERVICIO MEDICO", choices=SERVICIO_MEDICO, max_length=25, blank=True, null=True)
        fmedica_educacion_especial =UpperCaseCharField(verbose_name="¿REQUIERE EDUCACION ESPECIAL?", choices=OPCION, max_length=2, blank=True, null=True)
        fmedica_es_alergico_medicamento= UpperCaseCharField(verbose_name="¿ES ALERGICO A ALGUN MEDICAMENTO?", choices=OPCION, max_length=2, blank=True, null=True)
        fmedica_cual_medicamento= UpperCaseCharField(verbose_name="¿CUAL MEDICAMENTO?", max_length=40, blank=True, null=True)
        fmedica_es_alergico_alimento=UpperCaseCharField(verbose_name="ES ALERGICO A ALGUN ALIMENTO?", choices=OPCION, max_length=2, blank=True, null=True )
        fmedica_cual_alimento= UpperCaseCharField(verbose_name="¿CUAL ALIMENTO?", max_length=40,blank=True, null=True)
        fmedica_problema_postural =UpperCaseCharField(verbose_name='¿TIENE PROBLEMA POSTURAL?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        fmedica_usa_aparato_ortopedico=UpperCaseCharField(verbose_name='¿UTILIZA APARATO ORTOPEDICO?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        
        class Meta:
            db_table = "Ficha_medica"
            verbose_name = "Ficha Medica general"
            verbose_name_plural = "Fichas medicas"
            ordering = ['pk_curp', 'fmedica_servicio_medico']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Ficha_medica'    

class Ficha_medica_visual(models.Model):
        
        OPCION=(
                ('SI','SI'),
                ('NO','NO'),
        )
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        fvisual_ojo_izquierdo_num_linea= models.IntegerField(verbose_name="OJO IZQUIERDO NUMERO DE LINEA",null=True, blank=True )
        fvisual_ojo_derecho_num_linea=models.IntegerField(verbose_name="OJO DERECHO NUMERO DE LINEA",null=True, blank=True)
        fvisual_usa_lentes=UpperCaseCharField(verbose_name='¿USA LENTES?', choices=OPCION, null=True, blank=True, max_length=2)
        
        class Meta:
            db_table = "Ficha_medica_visual"
            verbose_name = "Ficha Medica Visual"
            verbose_name_plural = "Fichas medicas visuales"
            ordering = ['pk_curp', 'fvisual_usa_lentes']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Ficha_medica_visual'  


class Ficha_medica_dental (models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        OPCION=(
            ('SI','SI'),
            ('NO','NO'),
        )
        fdental_tiene_caries= UpperCaseCharField(verbose_name='¿TIENE CARIES?', choices=OPCION, null=True, blank=True, max_length=2)
        fdental_numero_caries = models.IntegerField(verbose_name="NUMERO DE CARIES",null=True, blank=True)
        fdental_tiene_inflamacion_o_sangrado_al_cepillarse=UpperCaseCharField(verbose_name='¿TIENE INFLAMACION O SANGRADO AL CEPILLARSE?', choices=OPCION, null=True, blank=True, max_length=2)
        fdental_tiene_dientes_chuecos_malaposicion=UpperCaseCharField(verbose_name='¿TIENE DIENTES CHUECOS O EN MALA POSICION?', choices=OPCION, null=True, blank=True, max_length=2)
	
        class Meta:
            db_table = "Ficha_medica_dental"
            verbose_name = "Ficha Medica Dental"
            verbose_name_plural = "Fichas medicas dentales"
            ordering = ['pk_curp', 'fdental_tiene_caries']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Ficha_medica_dental'  


class Ficha_medica_auditiva (models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        OPCION=(
            ('SI','SI'),
            ('NO','NO'),
        )
        TRANSMISION=(
            ('TA','TRANSMISION AÉREA'),
            ('TO','TRANSMISION ÓSEA'),
        )

        fauditiva_agudeza_oido_izquierdo = UpperCaseCharField(verbose_name='TIPO DE TRANSMISION DEL OIDO IZQUIERDO', choices=TRANSMISION, null=True, blank=True, max_length=2)
        fauditiva_agudeza_oido_derecho =  UpperCaseCharField(verbose_name='TIPO DE TRANSMISION DEL OIDO DERECHO', choices=TRANSMISION, null=True, blank=True, max_length=2)
        fauditiva_usa_aparato_oido_izquierdo = UpperCaseCharField(verbose_name='¿USA APARATO EN EL OIDO IZQUIERDO?', choices=OPCION, null=True, blank=True, max_length=2)
        fauditiva_usa_aparato_oido_derecho = UpperCaseCharField(verbose_name='¿USA APARATO EN EL OIDO DERECHO?', choices=OPCION, null=True, blank=True, max_length=2)

        class Meta:
            db_table = "Ficha_medica_auditiva"
            verbose_name = "Ficha Medica auditiva"
            verbose_name_plural = "Fichas medicas auditivas"
            ordering = ['pk_curp']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Ficha_medica_auditiva'  

class Alumno_bajo_tratamiento(models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        OPCION=(
            ('SI','SI'),
            ('NO','NO'),
        )
        atratamiento_tiene_cardiopatias=UpperCaseCharField(verbose_name='¿TIENE CARDIOPATIAS ?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_hipertension =UpperCaseCharField(verbose_name='¿TIENE HIPERTENSIÓN?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_cancer=UpperCaseCharField(verbose_name='¿TIENE CANCER?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_diabetes=UpperCaseCharField(verbose_name='¿TIENE DIABETES?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_obesidad=UpperCaseCharField(verbose_name='¿TIENE OBESIDAD?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_desnutricion=UpperCaseCharField(verbose_name='¿TIENE DESNUTRICIÓN?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_VIH_sida=UpperCaseCharField(verbose_name='¿TIENE VIH SIDA?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_asma=UpperCaseCharField(verbose_name='¿TIENE ASMA?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_depresion=UpperCaseCharField(verbose_name='¿TIENE DEPRESION?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_lupus=UpperCaseCharField(verbose_name='¿TIENE LUPUS?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_insuficiencia_renal =UpperCaseCharField(verbose_name='¿TIENE INSUFICIENCIA RENAL?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_artritis =UpperCaseCharField(verbose_name='¿TIENE PROBLEMA ARTRITIS?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_epilepsia_o_convulsiones =UpperCaseCharField(verbose_name='¿TIENE EPILEPSIA O CONVULSIONES?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_tuberculosis=UpperCaseCharField(verbose_name='¿TIENE TUBERCULOSIS?', choices=OPCION, null=True, blank=True, max_length=2)
        atratamiento_tiene_otras_enfermedades_cronicas =UpperCaseCharField(verbose_name='¿TIENE ALGUNA OTRA ENFERMEDAD CRoNICA?', choices=OPCION, null=True, blank=True, max_length=2)

        class Meta:
            db_table = "Alumno_bajo_tratamiento"
            verbose_name = "Tratamiento"
            verbose_name_plural = "Tratamientos"
            ordering = ['pk_curp']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Alumno_bajo_tratamiento' 


class Acta_nacimiento(models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        acta_nacimiento_numero_control_o_folio =UpperCaseCharField(verbose_name="NUMERO DE CONTROL O FOLIO DEL ACTA", max_length=40,blank=True, null=True)
        acta_nacimiento_numero_libro= UpperCaseCharField(verbose_name="NUMERO DEL LIBRO", max_length=40,blank=True, null=True)
        acta_nacimiento_año_registro=UpperCaseCharField(verbose_name="AÑO DE REGISTRO", max_length=4,blank=True, null=True)
        acta_nacimiento_numero_acta=UpperCaseCharField(verbose_name="NUMERO DE ACTA", max_length=40,blank=True, null=True)
        acta_nacimiento_folio_curp=UpperCaseCharField(verbose_name="NUMERO DE FOLIO DEL CURP", max_length=40,blank=True, null=True)
        class Meta:
            db_table = "Acta_nacimiento"
            verbose_name = "Acta de nacimiento"
            verbose_name_plural = "Datos del acta"
            ordering = ['pk_curp']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Acta_nacimiento' 

class Datos_familiares(models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        OPCION=(
            ('SI','SI'),
            ('NO','NO'),
        )
        pcasa_padres=UpperCaseCharField(verbose_name='¿VIVES CON TUS PADRES?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pcasa_madre =UpperCaseCharField(verbose_name='¿VIVES CON TU MADRE?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pcasa_padre=UpperCaseCharField(verbose_name='¿VIVES CON TU PADRE?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pcasa_hermanos=UpperCaseCharField(verbose_name='¿VIVES CON HERMANOS?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pcasa_abuelos=UpperCaseCharField(verbose_name='¿VIVES CON TUS ABUELOS?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pcasa_tios=UpperCaseCharField(verbose_name='¿VIVES CON TUS TIOS?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pcasa_otro = UpperCaseCharField(verbose_name='OTRO(A)', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pcasa_solo =UpperCaseCharField(verbose_name='¿VIVES SOLO?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
       
        class Meta:
            db_table = "Datos_familiares"
            verbose_name = "Dato Familiar"
            verbose_name_plural = "Datos Familiares"
            ordering = ['pk_curp']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Datos_familiares' 

class Alumno_convivencia(models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        OPCION=(
            ('SI','SI'),
            ('NO','NO'),
        )
        ACTIVIDAD=(
            ('JUGAR','JUGAR'),
            ('HACER ALGUN DEPORTE','HACER ALGUN DEPORTE'),
            ('HACER TAREA','HACER TAREA'),
            ('UTILIZAR UN APARATO ELECTRONICO','UTILIZAR UN APARATO ELECTRONICO'),
            ('SALIR CON AMIGOS','SALIR CON AMIGOS'),
            ('TRABAJAR','TRABAJAR'),
            ('HACER TAREAS DOMESTICAS','HACER TAREAS DOMESTICAS'),
            ('OTROS','OTROS'),
        )
        pconvive_padres=UpperCaseCharField(verbose_name='¿PASAS LA MAYOR PARTE DEL TIEMPO CON TUS PADRES?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pconvive_madre=UpperCaseCharField(verbose_name='PASAS LA MAYOR PARTE DEL TIEMPO CON TU MADRE', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pconvive_padre=UpperCaseCharField(verbose_name='PASAS LA MAYOR PARTE DEL TIEMPO CON TU PADRE', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pconvive_hermanos=UpperCaseCharField(verbose_name='PASAS LA MAYOR PARTE DEL TIEMPO CON TUS HERMANOS', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pconvive_abuelos=UpperCaseCharField(verbose_name='PASAS LA MAYOR PARTE DEL TIEMPO CON TUS ABUELOS', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pconvive_tios=UpperCaseCharField(verbose_name='PASAS LA MAYOR PARTE DEL TIEMPO CON TUS TIOS', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pconvive_otro =UpperCaseCharField(verbose_name='PASAS LA MAYOR PARTE DEL TIEMPO CON OTROS', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pconvive_solo=UpperCaseCharField(verbose_name='PASAS LA MAYOR PARTE DEL TIEMPO SOLO', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        pconvive_numero_hermanos= models.IntegerField(verbose_name='¿CUANTOS HERMANOS TIENES?', null=True, blank=True )
        pconvive_lugar_entre_hermanos=models.IntegerField(verbose_name='¿CUAl ES TU LUGAR ENTRE HERMANOS?', null=True, blank=True )
        pconvive_actividad_dedica_mas_tiempo= UpperCaseCharField(verbose_name='¿A QUÉ ACTIVIDAD LE DEDICAS MAS TIEMPO?', choices=ACTIVIDAD, max_length=35, null=True)
        
        class Meta:
            db_table = "Alumno_convivencia"
            verbose_name = "Convivencia"
            verbose_name_plural = "Convivencias"
            ordering = ['pk_curp']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Alumno_convivencia' 


class Discapacidad(models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        OPCION=(
            ('SI','SI'),
            ('NO','NO'),
        )
        discapacidad_tiene_autismo=UpperCaseCharField(verbose_name='¿TIENE AUTISMO?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_baja_vision=UpperCaseCharField(verbose_name='¿TIENE BAJA VISIÓN?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_ceguera=UpperCaseCharField(verbose_name='¿TIENE CEGUERA?', choices=OPCION, null=True, blank=True, max_length=2,default="NO")
        discapacidad_intelectual=UpperCaseCharField(verbose_name='¿TIENE DISCAPACIDAD INTELECTUAL?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_motriz=UpperCaseCharField(verbose_name='¿TIENE DISCAPACIDAD MOTRIZ?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_multiple =UpperCaseCharField(verbose_name='¿TIENE DISCAPACIDAD MULTIPLE?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_baja_audicion=UpperCaseCharField(verbose_name='¿TIENE BAJA AUDICIÓN?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_mental=UpperCaseCharField(verbose_name='¿TIENE DISCAPACIDAD MENTAL?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_problema_comunicacion_lenguaje=UpperCaseCharField(verbose_name='¿TIENE PROBLEMAS DE COMUNICACION O LENGUAJE?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_problema_conducta=UpperCaseCharField(verbose_name='¿TIENE PROBLEMAS DE CONDUCTA?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_sordera=UpperCaseCharField(verbose_name='¿TIENE SORDERA?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_sordoceguera=UpperCaseCharField(verbose_name='¿TIENE SORDOCEGUERA?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_transtorno_del_desarrollo=UpperCaseCharField(verbose_name='¿TIENE TRANSTORNO DEL DESARROLLO?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        discapacidad_tiene_transtorno_deficit_atencion_hiperactividad=UpperCaseCharField(verbose_name='¿TIENE TRANSTORNO DE DEFICIT DE ATENCION O HIPERACTIVIDAD?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")

        class Meta:
            db_table="Discapacidad"
            verbose_name="Discapacidad"
            verbose_name_plural ="Discapacidades"
            ordering = ['pk_curp']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Discapacidad' 

class Aptitud_sobresaliente(models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)       
        OPCION=(
            ('SI','SI'),
            ('NO','NO'),
        )
        aptitud_intelectual=UpperCaseCharField(verbose_name='¿TIENE APTITUD INTELECTUAL?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        aptitud_psicomotriz=UpperCaseCharField(verbose_name='¿TIENE APTITUD PSICOMOTRIZ?', choices=OPCION, null=True, blank=True, max_length=2, default="NO")
        aptitud_socioafectiva=UpperCaseCharField(verbose_name='¿TIENE APTITUD SOCIOAFECTIVA?', choices=OPCION, null=True, blank=True, max_length=2, default="NO" )
        aptitud_creativa=UpperCaseCharField(verbose_name='¿TIENE APTITUD CREATIVA?', choices=OPCION, null=True, blank=True, max_length=2, default="NO" )

        class Meta:
            db_table = "Aptitud_sobresaliente"
            verbose_name = "Aptitud"
            verbose_name_plural = "Aptitudes"
            ordering = ['pk_curp']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Aptitud_sobresaliente' 

class Responsable(models.Model):
        pk_responsable_curp=UpperCaseCharField(primary_key=True,verbose_name="CURP DEL RESPONSABLE", max_length=18)
        pk_curp= models.ForeignKey(Curp, verbose_name="CURP DEL ALUMNO", max_length=18,on_delete=models.ProtectedError)       
        responsable_parentesco=UpperCaseCharField(verbose_name="PARENTESCO", max_length=6)
        responsable_ap_paterno= UpperCaseCharField(verbose_name="APELLIDO PATERNO", max_length=45)
        responsable_ap_materno=UpperCaseCharField(verbose_name="APELLIDO MATERNO", max_length=45)
        responsable_nombre= UpperCaseCharField(verbose_name="NOMBRE", max_length=45)
        responsable_fecha_nacimiento = models.DateField(verbose_name="FECHA DE NACIMIENTO")
        responsable_correo= models.EmailField(verbose_name="CORREO ELECTRONICO")
        responsable_telefono=UpperCaseCharField(verbose_name="TELEFONO", max_length=10)
        ESCOLARIDAD=(
                ('NINGUNA','NINGUNA'),
                ('PRIMARIA','PRIMARIA'),
                ('SECUNDARIA','SECUNDARIA'),
                ('BACHILLERATO','BACHILLERATO'),
                ('TECNICO','TECNICO'),
                ('PROFESIONAL','PROFESIONAL'),
                ('POSGRADO','POSGRADO'),
        )
        responsable_nivel_estudio= UpperCaseCharField(verbose_name="NIVEL DE ESTUDIOS", choices=ESCOLARIDAD, max_length= 12)
        OCUPACION=(
            ('HOGAR','HOGAR'),
            ('DESEMPLEADO','DESEMPLEADO'),
            ('EMPLEADO','EMPLEADO'),
            ('JUBILADO','JUBILADO'),
            ('ESTUDIANTE','ESTUDIANTE'),
            ('JORNALERO','JORNALERO'),
            ('CUENTA PROPIA','CUENTA PROPIA'),
            ('OTRO','OTRO'),
        )
        responsable_ocupacion =UpperCaseCharField(verbose_name="OCUPACION", choices=OCUPACION, max_length= 13, null=True)
        created = models.DateTimeField(auto_now_add=True, verbose_name="FECHA DE CREACION")
        updated = models.DateTimeField(auto_now=True, verbose_name="FECHA DE EDICION")

        class Meta:
            db_table = "responsable"
            verbose_name = "Responsable"
            verbose_name_plural = "Responsables"
            ordering = ['pk_curp','pk_responsable_curp']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Responsable' 


class Archivo(models.Model):
        pk_curp= models.OneToOneField(Curp, max_length=18,on_delete=models.CASCADE)
        archivo_curp=models.FileField(verbose_name="Archivo CURP", upload_to="curp/%Y")
        archivo_acta_nacimiento = models.FileField(verbose_name="Archivo Acta de Nacimiento", upload_to="actan/%Y")
        archivo_certificado_primaria= models.FileField(verbose_name="Archivo Certificado Primaria", upload_to="certificado/%Y")
        archivo_boleta_sexto=models.FileField(verbose_name="Archivo Boleta", upload_to="Boleta/%Y")
        created = models.DateTimeField(auto_now_add=True, verbose_name="FECHA DE CREACION")

        class Meta:
            db_table = "Archivo"
            verbose_name = "Archivo"
            verbose_name_plural = "Archivos"
            ordering = ['pk_curp','created']

        def __str__(self):
            return f'{self.pk_curp.pk_curp}Archivo' 
