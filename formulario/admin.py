from django.contrib import admin
import nested_admin
from .models import (Recluta, DatosFamiliares, InformacionAcademica,
                     ReferenciasPersonales, BienesRentasAEP, SituacionJuridica,Hijo,Hermano)
import nested_admin

# -------------------- INLINES ANIDADOS --------------------

# Inline para el modelo Hijo dentro de DatosFamiliares

class HijoInline(nested_admin.NestedTabularInline):
    model = Hijo
    extra = 0
    
# Inline para el modelo Hermano dentro de DatosFamiliares
class HermanoInline(nested_admin.NestedTabularInline):
    model = Hermano
    extra = 0

# Inline para el modelo DatosFamiliares que incluye hijos y hermanos
class DatosFamiliaresInline(nested_admin.NestedStackedInline):
    model = DatosFamiliares
    inlines = [HijoInline,HermanoInline]  # Se anidan hijos y hermanos
    extra = 0


# Inline para información académica
class InformacionAcademicaInline(nested_admin.NestedStackedInline):  #
    model = InformacionAcademica
    extra = 0

# Inline para referencias personales
class ReferenciasPersonalesInline(nested_admin.NestedStackedInline):
    model = ReferenciasPersonales
    extra = 0



# Inline para bienes y rentas (AEP)
class BienesRentasAEPInline(nested_admin.NestedStackedInline):
    model = BienesRentasAEP
    extra = 0

# Inline para situación jurídica
class SituacionJuridicaInline(nested_admin.NestedStackedInline):
    model = SituacionJuridica
    extra = 0



# Admin del modelo Recluta con todos los inlines anidados
@admin.register(Recluta)
class ReclutaAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        DatosFamiliaresInline,
        InformacionAcademicaInline,
        ReferenciasPersonalesInline,
        BienesRentasAEPInline,
        SituacionJuridicaInline,
        
    ]
# Columnas visibles en la lista de reclutas
    list_display = (

#CLASE RECLUTA
            "primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido",
            "tipo_documento", "numero_documento", "fecha_expedición", "lugar_expedición",
            "pasaporte_numero", "fecha_pasaporte",
             "dia_nacimiento",
            "mes_nacimiento", "año_nacimiento", "estado_civil", "profesion_oficio",
            "tarjeta_profesional", "señales_corporales", "estatura", "peso", "tipo_via",
            "numero_principal", "letra_principal", "bis", "letra_bis", "cuadrante",
            "numero_secundario", "letra_secundaria", "cuadrante_dos", "nro", "complemento",
            "barrio","numero_celular","telefono_fijo","ciudad","departamento","correo_electronico_personal",
        
    )

# Campos habilitados para búsqueda
    search_fields = (

#CLASE RECLUTA
            "primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido",
            "tipo_documento", "numero_documento", "fecha_expedición", "lugar_expedición",
            "pasaporte_numero", "fecha_pasaporte",
            "dia_nacimiento",
            "mes_nacimiento", "año_nacimiento", "estado_civil", "profesion_oficio",
            "tarjeta_profesional", "señales_corporales", "estatura", "peso", "tipo_via",
            "numero_principal", "letra_principal", "bis", "letra_bis", "cuadrante",
            "numero_secundario", "letra_secundaria", "cuadrante_dos", "nro", "complemento",
            "barrio","numero_celular","telefono_fijo","ciudad","departamento","correo_electronico_personal",
    )

 # Filtros disponibles en la barra lateral
    list_filter = (
    )


@admin.register(DatosFamiliares)
class DatosFamiliaresAdmin(admin.ModelAdmin):
    inlines = [HijoInline,HermanoInline]
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (

#CLASE DATOS FAMILIARES
      #Datos Conyugue
            "nombre_conyugue", "cedula_conyugue", "profesion_oficio_conyugue", "celular_conyugue",
            "tipo_via_conyugue", "numero_principal_conyugue", "letra_principal_conyugue",
            "bis_conyugue", "letra_bis_conyugue", "cuadrante_conyugue",
            "numero_secundario_conyugue", "letra_secundaria_conyugue", "cuadrante_dos_conyugue",
            "nro_conyugue", "complemento_conyugue","direccion_formateada_conyugue",

#Datos Padre
            "nombre_padre", "vive_padre","identificación_padre","telefono_padre", "oficio_profesion_padre",
            "tipo_via_padre", "numero_principal_padre", "letra_principal_padre","bis_padre", "letra_bis_padre", "cuadrante_padre",
            "numero_secundario_padre", "letra_secundaria_padre", "cuadrante_dos_padre","nro_padre", "complemento_padre","direccion_formateada_padre",
#Datos Madre
            "nombre_madre", "vive_madre",
            "identificación_madre","telefono_madre", "oficio_profesion_madre","tipo_via_madre", "numero_principal_madre", "letra_principal_madre",
            "bis_madre", "letra_bis_madre", "cuadrante_madre","numero_secundario_madre", "letra_secundaria_madre",
            "cuadrante_dos_madre","nro_madre", "complemento_madre","direccion_formateada_madre",

        
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (

#CLASE DATOS FAMILIARES
#Datos Conyugue
            "nombre_conyugue", "cedula_conyugue", "profesion_oficio_conyugue", "celular_conyugue",
            "tipo_via_conyugue", "numero_principal_conyugue", "letra_principal_conyugue",
            "bis_conyugue", "letra_bis_conyugue", "cuadrante_conyugue",
            "numero_secundario_conyugue", "letra_secundaria_conyugue", "cuadrante_dos_conyugue",
            "nro_conyugue", "complemento_conyugue","direccion_formateada_conyugue",

#Datos Padre
            "nombre_padre", "vive_padre","identificación_padre","telefono_padre", "oficio_profesion_padre",
            "tipo_via_padre", "numero_principal_padre", "letra_principal_padre","bis_padre", "letra_bis_padre", "cuadrante_padre",
            "numero_secundario_padre", "letra_secundaria_padre", "cuadrante_dos_padre","nro_padre", "complemento_padre","direccion_formateada_padre",
#Datos Madre
            "nombre_madre", "vive_madre",
            "identificación_madre","telefono_madre", "oficio_profesion_madre","tipo_via_madre", "numero_principal_madre", "letra_principal_madre",
            "bis_madre", "letra_bis_madre", "cuadrante_madre","numero_secundario_madre",
            "letra_secundaria_madre", "cuadrante_dos_madre","nro_madre", "complemento_madre","direccion_formateada_madre",


    )

    # ----------  FILTROS LATERALES  ----------
    list_filter = (
    )

@admin.register(Hermano)
class HermanoAdmin(admin.ModelAdmin):
    
    list_display = (
        "primer_nombre_hermano",
        "segundo_nombre_hermano",
        "primer_apellido_hermano",
        "segundo_apellido_hermano",
        "identificacion_hermano",
        "direccion_formateada_hermano",
    )

    search_fields = (
        "primer_nombre_hermano",
        "segundo_nombre_hermano",
        "primer_apellido_hermano",
        "segundo_apellido_hermano",
        "identificacion_hermano",
        "direccion_formateada_hermano",
    )
# El resto de los modelos siguen el patrón similar:
# 1. Se registran con el decorador @admin.register
# 2. Se definen sus columnas a mostrar en list_display
# 3. Se agregan campos relevantes en search_fields
# 4. Se dejan list_filter vacíos por ahora para evitar sobrecargar la interfaz

# Nota: Este archivo permite una visualización y gestión avanzada de los modelos
# en el panel de administración de Django, usando `nested_admin` para relaciones complejas.

@admin.register(InformacionAcademica)
class InformacionAcademicaAdmin(admin.ModelAdmin):
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (

#Estudios
            "estudios_1", "año_estudios_1", "titulo_estudios_1", "nombre_institucion_estudios_1", "ciudad_estudios_1",
            "estudios_2", "año_estudios_2", "titulo_estudios_2", "nombre_institucion_estudios_2", "ciudad_estudios_2",

#Idioma Extranjero
           "idioma_extranjero_1", "lee_idioma_extranjero_1","habla_idioma_extranjero_1","escribe_idioma_extranjero_1",
           "idioma_extranjero_2", "lee_idioma_extranjero_2","habla_idioma_extranjero_2","escribe_idioma_extranjero_2",
#Ofimática
            "word_check", "excel_check", "powerpoint_check", "access_check", "internet_check","otro_check"
        
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (


#Estudios
            "estudios_1", "año_estudios_1", "titulo_estudios_1", "nombre_institucion_estudios_1", "ciudad_estudios_1",
            "estudios_2", "año_estudios_2", "titulo_estudios_2", "nombre_institucion_estudios_2", "ciudad_estudios_2",

#Idioma Extranjero
           "idioma_extranjero_1", "lee_idioma_extranjero_1","habla_idioma_extranjero_1","escribe_idioma_extranjero_1",
           "idioma_extranjero_2", "lee_idioma_extranjero_2","habla_idioma_extranjero_2","escribe_idioma_extranjero_2",
#Ofimática
            "word_check", "excel_check", "powerpoint_check", "access_check", "internet_check","otro_check"
    )

    # ----------  FILTROS LATERALES  ----------
    list_filter = (
    )

@admin.register(ReferenciasPersonales)
class ReferenciasPersonalesAdmin(admin.ModelAdmin):

    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (
# Referencia 1
            "nombre_referencia_1", "ocupacion_referencia_1", "empresa_referencia_1", "tiempo_referencia_1", "ciudad_referencia_1", "telefono_referencia_1",
            "tipo_via_referencia_1", "numero_principal_referencia_1", "letra_principal_referencia_1", "bis_referencia_1", "letra_bis_referencia_1",
            "cuadrante_referencia_1", "numero_secundario_referencia_1", "letra_secundaria_referencia_1", "cuadrante_dos_referencia_1",
            "nro_referencia_1", "complemento_referencia_1","direccion_formateada_referencia_1",

# Referencia 2
            "nombre_referencia_2", "ocupacion_referencia_2", "empresa_referencia_2", "tiempo_referencia_2", "ciudad_referencia_2", "telefono_referencia_2",
            "tipo_via_referencia_2", "numero_principal_referencia_2", "letra_principal_referencia_2", "bis_referencia_2", "letra_bis_referencia_2",
            "cuadrante_referencia_2", "numero_secundario_referencia_2", "letra_secundaria_referencia_2", "cuadrante_dos_referencia_2",
            "nro_referencia_2", "complemento_referencia_2","direccion_formateada_referencia_2",
# Referencia 3
            "nombre_referencia_3", "ocupacion_referencia_3", "empresa_referencia_3", "tiempo_referencia_3", "ciudad_referencia_3", "telefono_referencia_3",
            "tipo_via_referencia_3", "numero_principal_referencia_3", "letra_principal_referencia_3", "bis_referencia_3", "letra_bis_referencia_3",
            "cuadrante_referencia_3", "numero_secundario_referencia_3", "letra_secundaria_referencia_3", "cuadrante_dos_referencia_3",
            "nro_referencia_3", "complemento_referencia_3","direccion_formateada_referencia_3",
        
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (

# Referencia 1
            "nombre_referencia_1", "ocupacion_referencia_1", "empresa_referencia_1", "tiempo_referencia_1", "ciudad_referencia_1", "telefono_referencia_1",
            "tipo_via_referencia_1", "numero_principal_referencia_1", "letra_principal_referencia_1", "bis_referencia_1", "letra_bis_referencia_1",
            "cuadrante_referencia_1", "numero_secundario_referencia_1", "letra_secundaria_referencia_1", "cuadrante_dos_referencia_1",
            "nro_referencia_1", "complemento_referencia_1","direccion_formateada_referencia_1",

# Referencia 2
            "nombre_referencia_2", "ocupacion_referencia_2", "empresa_referencia_2", "tiempo_referencia_2", "ciudad_referencia_2", "telefono_referencia_2",
            "tipo_via_referencia_2", "numero_principal_referencia_2", "letra_principal_referencia_2", "bis_referencia_2", "letra_bis_referencia_2",
            "cuadrante_referencia_2", "numero_secundario_referencia_2", "letra_secundaria_referencia_2", "cuadrante_dos_referencia_2",
            "nro_referencia_2", "complemento_referencia_2","direccion_formateada_referencia_2",
# Referencia 3
            "nombre_referencia_3", "ocupacion_referencia_3", "empresa_referencia_3", "tiempo_referencia_3", "ciudad_referencia_3", "telefono_referencia_3",
            "tipo_via_referencia_3", "numero_principal_referencia_3", "letra_principal_referencia_3", "bis_referencia_3", "letra_bis_referencia_3",
            "cuadrante_referencia_3", "numero_secundario_referencia_3", "letra_secundaria_referencia_3", "cuadrante_dos_referencia_3",
            "nro_referencia_3", "complemento_referencia_3","direccion_formateada_referencia_3",
    )

    # ----------  FILTROS LATERALES  ----------
    list_filter = (
    )


@admin.register(BienesRentasAEP)
class BienesRentasAEPAdmin(admin.ModelAdmin):
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (
            "salarios_y_demas_ingresos_laborales","cesantías_e_intereses_de_cesantías","arriendos","honorarios","otros_ingresos_y_rentas",
            "entidad_financiera_1", "tipo_de_cuenta_1", "numero_de_cuenta_1","entidad_financiera_2", "tipo_de_cuenta_2", "numero_de_cuenta_2",
       

            "tipo_bien_1","ubicacion_bien_1","identificacion_bien_1","avaluo_comercial_bien_1",
            "tipo_bien_2","ubicacion_bien_2","identificacion_bien_2","avaluo_comercial_bien_2",
     

            "entidad_o_persona_obligacion_1", "concepto_obligacion_1", "valor_1",
            "entidad_o_persona_obligacion_2", "concepto_obligacion_2", "valor_2",


            "entidad_o_institucion_1","calidad_de_miembro_1",
            "entidad_o_institucion_2","calidad_de_miembro_2",
        

            "empresa_1","calidad_de_miembro_AEP_1",
            "empresa_2","calidad_de_miembro_AEP_2",
        
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (
            "salarios_y_demas_ingresos_laborales","cesantías_e_intereses_de_cesantías","arriendos","honorarios","otros_ingresos_y_rentas",
            "entidad_financiera_1", "tipo_de_cuenta_1", "numero_de_cuenta_1","entidad_financiera_2", "tipo_de_cuenta_2", "numero_de_cuenta_2",
         

            "tipo_bien_1","ubicacion_bien_1","identificacion_bien_1","avaluo_comercial_bien_1",
            "tipo_bien_2","ubicacion_bien_2","identificacion_bien_2","avaluo_comercial_bien_2",
  

            "entidad_o_persona_obligacion_1", "concepto_obligacion_1", "valor_1",
            "entidad_o_persona_obligacion_2", "concepto_obligacion_2", "valor_2",
 

            "entidad_o_institucion_1","calidad_de_miembro_1",
            "entidad_o_institucion_2","calidad_de_miembro_2",
    

            "empresa_1","calidad_de_miembro_AEP_1",
            "empresa_2","calidad_de_miembro_AEP_2",
       
    )

    # ----------  FILTROS LATERALES  ----------
    list_filter = (
    )

@admin.register(SituacionJuridica)
class SituacionJuridicaAdmin(admin.ModelAdmin):
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (
            "fecha_proceso_1", "tipo_de_investigacion_1", "causa_1", "autoridad_1", "estado_del_proceso_1", "responsable_1",
            "fecha_proceso_2", "tipo_de_investigacion_2", "causa_2", "autoridad_2", "estado_del_proceso_2", "responsable_2",
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (
            "fecha_proceso_1", "tipo_de_investigacion_1", "causa_1", "autoridad_1", "estado_del_proceso_1", "responsable_1",
            "fecha_proceso_2", "tipo_de_investigacion_2", "causa_2", "autoridad_2", "estado_del_proceso_2", "responsable_2",
    )

    # ----------  FILTROS LATERALES  ----------
    list_filter = (
    )


