from django.contrib import admin
import nested_admin
from .models import (Recluta, DatosFamiliares,DireccionesAnteriores, InformacionAcademica,
                     ReferenciasPersonales,SectorDefensa, BienesRentasAEP, SituacionJuridica, OtrosDatos,Hijo,Hermano)
import nested_admin


class HijoInline(nested_admin.NestedTabularInline):
    model = Hijo
    extra = 0
    
class HermanoInline(nested_admin.NestedTabularInline):
    model = Hermano
    extra = 0

class DatosFamiliaresInline(nested_admin.NestedStackedInline):
    model = DatosFamiliares
    inlines = [HijoInline,HermanoInline]  # 👈 Aquí anidamos los hijos
    extra = 0

class DireccionesAnterioresInline(nested_admin.NestedStackedInline):
    model = DireccionesAnteriores
    extra = 0

class InformacionAcademicaInline(nested_admin.NestedStackedInline):  #
    model = InformacionAcademica
    extra = 0


class ReferenciasPersonalesInline(nested_admin.NestedStackedInline):
    model = ReferenciasPersonales
    extra = 0

class SectorDefensaInline(nested_admin.NestedStackedInline):
    model = SectorDefensa
    extra = 0

class BienesRentasAEPInline(nested_admin.NestedStackedInline):
    model = BienesRentasAEP
    extra = 0

class SituacionJuridicaInline(nested_admin.NestedStackedInline):
    model = SituacionJuridica
    extra = 0

class OtrosDatosInline(nested_admin.NestedStackedInline):
    model = OtrosDatos
    extra = 0


@admin.register(Recluta)
class ReclutaAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        DatosFamiliaresInline,
        DireccionesAnterioresInline,
        InformacionAcademicaInline,
        ReferenciasPersonalesInline,
        SectorDefensaInline,
        BienesRentasAEPInline,
        SituacionJuridicaInline,
        OtrosDatosInline,
    ]
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (

#CLASE RECLUTA
            "primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido",
            "tipo_documento", "numero_documento", "fecha_expedición", "lugar_expedición",
            "pasaporte_numero", "fecha_pasaporte", "numero_libretamilitar", "clase_libretamilitar",
            "distrito_militar", "sobrenombres",  "dia_nacimiento",
            "mes_nacimiento", "año_nacimiento", "estado_civil", "profesion_oficio",
            "tarjeta_profesional", "señales_corporales", "estatura", "peso", "tipo_via",
            "numero_principal", "letra_principal", "bis", "letra_bis", "cuadrante",
            "numero_secundario", "letra_secundaria", "cuadrante_dos", "nro", "complemento",
            "barrio","numero_celular","telefono_fijo","ciudad","departamento","correo_electronico_personal",
            "correo_electronico_institucional","facebook","instagram","twitter","otras_redes","direccion_formateada",
        
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (

#CLASE RECLUTA
            "primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido",
            "tipo_documento", "numero_documento", "fecha_expedición", "lugar_expedición",
            "pasaporte_numero", "fecha_pasaporte", "numero_libretamilitar", "clase_libretamilitar",
            "distrito_militar", "sobrenombres",  "dia_nacimiento",
            "mes_nacimiento", "año_nacimiento", "estado_civil", "profesion_oficio",
            "tarjeta_profesional", "señales_corporales", "estatura", "peso", "tipo_via",
            "numero_principal", "letra_principal", "bis", "letra_bis", "cuadrante",
            "numero_secundario", "letra_secundaria", "cuadrante_dos", "nro", "complemento",
            "barrio","numero_celular","telefono_fijo","ciudad","departamento","correo_electronico_personal",
            "correo_electronico_institucional","facebook","instagram","twitter","otras_redes","direccion_formateada",
    )

    # ----------  FILTROS LATERALES  ----------
    list_filter = (
    )

@admin.register(DireccionesAnteriores)
class DireccionesAnterioresAdmin(admin.ModelAdmin):
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (

#CLASE DIRECCIONES ANTERIORES
            "desde_1","hasta_1", "tipo_via_anterior_1",
            "numero_principal_anterior_1", "letra_principal_anterior_1", "bis_anterior_1", "letra_bis_anterior_1", "cuadrante_anterior_1",
            "numero_secundario_anterior_1", "letra_secundaria_anterior_1", "cuadrante_dos_anterior_1", "nro_anterior_1", "complemento_anterior_1", 
            "telefono_direccion_anterior_1_1","telefono_direccion_anterior_1_2", "ciudad_direccion_anterior_1",
            "desde_2" ,"hasta_2", "tipo_via_anterior_2", "numero_principal_anterior_2", "letra_principal_anterior_2", "bis_anterior_2",
            "letra_bis_anterior_2", "cuadrante_anterior_2","numero_secundario_anterior_2", "letra_secundaria_anterior_2",
            "cuadrante_dos_anterior_2", "nro_anterior_2", "complemento_anterior_2", "telefono_direccion_anterior_2_1",
            "telefono_direccion_anterior_2_2","ciudad_direccion_anterior_2","direccion_completa_anterior_1","direccion_completa_anterior_2",
        
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (

#CLASE DIRECCIONES ANTERIORES
            "desde_1","hasta_1", "tipo_via_anterior_1",
            "numero_principal_anterior_1", "letra_principal_anterior_1", "bis_anterior_1", "letra_bis_anterior_1", "cuadrante_anterior_1",
            "numero_secundario_anterior_1", "letra_secundaria_anterior_1", "cuadrante_dos_anterior_1", "nro_anterior_1", "complemento_anterior_1", 
            "telefono_direccion_anterior_1_1","telefono_direccion_anterior_1_2", "ciudad_direccion_anterior_1",
            "desde_2" ,"hasta_2", "tipo_via_anterior_2", "numero_principal_anterior_2", "letra_principal_anterior_2", "bis_anterior_2",
            "letra_bis_anterior_2", "cuadrante_anterior_2","numero_secundario_anterior_2", "letra_secundaria_anterior_2",
            "cuadrante_dos_anterior_2", "nro_anterior_2", "complemento_anterior_2", "telefono_direccion_anterior_2_1",
            "telefono_direccion_anterior_2_2","ciudad_direccion_anterior_2","direccion_completa_anterior_1","direccion_completa_anterior_2",
    )

    # ----------  FILTROS LATERALES  ----------
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

@admin.register(InformacionAcademica)
class InformacionAcademicaAdmin(admin.ModelAdmin):
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (

#Estudios
            "estudios_1", "año_estudios_1", "titulo_estudios_1", "nombre_institucion_estudios_1", "ciudad_estudios_1",
            "estudios_2", "año_estudios_2", "titulo_estudios_2", "nombre_institucion_estudios_2", "ciudad_estudios_2",
            "estudios_3", "año_estudios_3", "titulo_estudios_3", "nombre_institucion_estudios_3", "ciudad_estudios_3",
            "estudios_4", "año_estudios_4", "titulo_estudios_4", "nombre_institucion_estudios_4", "ciudad_estudios_4",
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
            "estudios_3", "año_estudios_3", "titulo_estudios_3", "nombre_institucion_estudios_3", "ciudad_estudios_3",
            "estudios_4", "año_estudios_4", "titulo_estudios_4", "nombre_institucion_estudios_4", "ciudad_estudios_4",
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

@admin.register(SectorDefensa)
class SectorDefensaAdmin(admin.ModelAdmin):
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (
# Referencia 1
    "nombresyapellidos_sd_1", "cargo_sd_1","entidad_sd_1","unidad_militar_sd_1", "celular_sd_1", "tipo_via_sd_1",
    "numero_principal_sd_1","letra_principal_sd_1","bis_sd_1","letra_bis_sd_1", "cuadrante_sd_1", "numero_secundario_sd_1", 
    "letra_secundaria_sd_1","cuadrante_dos_sd_1","nro_sd_1", "complemento_sd_1","direccion_formateada_sd_1",

# Referencia 2
    "nombresyapellidos_sd_2", "cargo_sd_2","entidad_sd_2","unidad_militar_sd_2", "celular_sd_2", "tipo_via_sd_2",
    "numero_principal_sd_2","letra_principal_sd_2","bis_sd_2","letra_bis_sd_2", "cuadrante_sd_2", "numero_secundario_sd_2", 
    "letra_secundaria_sd_2","cuadrante_dos_sd_2","nro_sd_2", "complemento_sd_2","direccion_formateada_sd_2",
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (
# Referencia 1
    "nombresyapellidos_sd_1", "cargo_sd_1","entidad_sd_1","unidad_militar_sd_1", "celular_sd_1", "tipo_via_sd_1",
    "numero_principal_sd_1","letra_principal_sd_1","bis_sd_1","letra_bis_sd_1", "cuadrante_sd_1", "numero_secundario_sd_1", 
    "letra_secundaria_sd_1","cuadrante_dos_sd_1","nro_sd_1", "complemento_sd_1","direccion_formateada_sd_1",

# Referencia 2
    "nombresyapellidos_sd_2", "cargo_sd_2","entidad_sd_2","unidad_militar_sd_2", "celular_sd_2", "tipo_via_sd_2",
    "numero_principal_sd_2","letra_principal_sd_2","bis_sd_2","letra_bis_sd_2", "cuadrante_sd_2", "numero_secundario_sd_2", 
    "letra_secundaria_sd_2","cuadrante_dos_sd_2","nro_sd_2", "complemento_sd_2","direccion_formateada_sd_2"
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
            "entidad_financiera_3", "tipo_de_cuenta_3", "numero_de_cuenta_3","entidad_financiera_4", "tipo_de_cuenta_4", "numero_de_cuenta_4",
            "entidad_financiera_5", "tipo_de_cuenta_5", "numero_de_cuenta_5","entidad_financiera_6", "tipo_de_cuenta_6", "numero_de_cuenta_6",

            "tipo_bien_1","ubicacion_bien_1","identificacion_bien_1","avaluo_comercial_bien_1",
            "tipo_bien_2","ubicacion_bien_2","identificacion_bien_2","avaluo_comercial_bien_2",
            "tipo_bien_3","ubicacion_bien_3","identificacion_bien_3","avaluo_comercial_bien_3",
            "tipo_bien_4","ubicacion_bien_4","identificacion_bien_4","avaluo_comercial_bien_4",
            "tipo_bien_5","ubicacion_bien_5","identificacion_bien_5","avaluo_comercial_bien_5",

            "entidad_o_persona_obligacion_1", "concepto_obligacion_1", "valor_1",
            "entidad_o_persona_obligacion_2", "concepto_obligacion_2", "valor_2",
            "entidad_o_persona_obligacion_3", "concepto_obligacion_3", "valor_3",
            "entidad_o_persona_obligacion_4", "concepto_obligacion_4", "valor_4",

            "entidad_o_institucion_1","calidad_de_miembro_1",
            "entidad_o_institucion_2","calidad_de_miembro_2",
            "entidad_o_institucion_3","calidad_de_miembro_3",
            "entidad_o_institucion_4","calidad_de_miembro_4",

            "empresa_1","calidad_de_miembro_AEP_1",
            "empresa_2","calidad_de_miembro_AEP_2",
            "empresa_3","calidad_de_miembro_AEP_3",
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (
            "salarios_y_demas_ingresos_laborales","cesantías_e_intereses_de_cesantías","arriendos","honorarios","otros_ingresos_y_rentas",
            "entidad_financiera_1", "tipo_de_cuenta_1", "numero_de_cuenta_1","entidad_financiera_2", "tipo_de_cuenta_2", "numero_de_cuenta_2",
            "entidad_financiera_3", "tipo_de_cuenta_3", "numero_de_cuenta_3","entidad_financiera_4", "tipo_de_cuenta_4", "numero_de_cuenta_4",
            "entidad_financiera_5", "tipo_de_cuenta_5", "numero_de_cuenta_5","entidad_financiera_6", "tipo_de_cuenta_6", "numero_de_cuenta_6",

            "tipo_bien_1","ubicacion_bien_1","identificacion_bien_1","avaluo_comercial_bien_1",
            "tipo_bien_2","ubicacion_bien_2","identificacion_bien_2","avaluo_comercial_bien_2",
            "tipo_bien_3","ubicacion_bien_3","identificacion_bien_3","avaluo_comercial_bien_3",
            "tipo_bien_4","ubicacion_bien_4","identificacion_bien_4","avaluo_comercial_bien_4",
            "tipo_bien_5","ubicacion_bien_5","identificacion_bien_5","avaluo_comercial_bien_5",

            "entidad_o_persona_obligacion_1", "concepto_obligacion_1", "valor_1",
            "entidad_o_persona_obligacion_2", "concepto_obligacion_2", "valor_2",
            "entidad_o_persona_obligacion_3", "concepto_obligacion_3", "valor_3",
            "entidad_o_persona_obligacion_4", "concepto_obligacion_4", "valor_4",

            "entidad_o_institucion_1","calidad_de_miembro_1",
            "entidad_o_institucion_2","calidad_de_miembro_2",
            "entidad_o_institucion_3","calidad_de_miembro_3",
            "entidad_o_institucion_4","calidad_de_miembro_4",

            "empresa_1","calidad_de_miembro_AEP_1",
            "empresa_2","calidad_de_miembro_AEP_2",
            "empresa_3","calidad_de_miembro_AEP_3",
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


@admin.register(OtrosDatos)
class OtrosDatosAdmin(admin.ModelAdmin):


    
    # ----------  QUÉ COLUMNAS MOSTRAR EN LA LISTA  ----------
    list_display = (
                        "fecha_viaje_1","pais_visitado_1","motivo_1","permanencia_1",
                    "fecha_viaje_2","pais_visitado_2","motivo_2","permanencia_2",
                    "fecha_viaje_3","pais_visitado_3","motivo_3","permanencia_3",

                    "recomendante","celular_recomendante","labora_en_indumil","nombres_y_apellidos_recomendante_1", 
                    "nombres_y_apellidos_recomendante_2", "cargo_recomendante_1", "cargo_recomendante_2",
                    "unidad_negocio_recomendante_1","unidad_negocio_recomendante_2",

                    "tipo_via_recomendante","numero_principal_recomendante", "letra_principal_recomendante", "bis_recomendante",
                    "letra_bis_recomendante", "cuadrante_recomendante", "numero_secundario_recomendante","letra_secundaria_recomendante",
                    "cuadrante_dos_recomendante","nro_recomendante", "complemento_recomendante",
                    "razon_de_vinculo","direccion_formateada_recomendante"
    )

    # ----------  CAMPOS PARA BUSCAR  ----------
    search_fields = (
                           "fecha_viaje_1","pais_visitado_1","motivo_1","permanencia_1",
                    "fecha_viaje_2","pais_visitado_2","motivo_2","permanencia_2",
                    "fecha_viaje_3","pais_visitado_3","motivo_3","permanencia_3",

                    "recomendante","celular_recomendante","labora_en_indumil","nombres_y_apellidos_recomendante_1", 
                    "nombres_y_apellidos_recomendante_2", "cargo_recomendante_1", "cargo_recomendante_2",
                    "unidad_negocio_recomendante_1","unidad_negocio_recomendante_2",

                    "tipo_via_recomendante","numero_principal_recomendante", "letra_principal_recomendante", "bis_recomendante",
                    "letra_bis_recomendante", "cuadrante_recomendante", "numero_secundario_recomendante","letra_secundaria_recomendante",
                    "cuadrante_dos_recomendante","nro_recomendante", "complemento_recomendante",
                    "razon_de_vinculo","direccion_formateada_recomendante"
    )

    # ----------  FILTROS LATERALES  ----------
    list_filter = (
    )

    # Inlines para ReclutaAdmin

