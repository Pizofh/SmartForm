from django.contrib import admin
import nested_admin
from .models import (PersonalData, FamilyData, InformacionAcademica,
                     BienesRentasAEP, SituacionJuridica,Child,Sibling)
import nested_admin

# -------------------- INLINES ANIDADOS --------------------

# Inline para el modeloChild dentro de DatosFamiliares

class ChildInline(nested_admin.NestedTabularInline):
    model = Child
    extra = 0
    
# Inline para el modelo Sibling dentro de DatosFamiliares
class SiblingInline(nested_admin.NestedTabularInline):
    model = Sibling
    extra = 0

# Inline para el modelo DatosFamiliares que incluye Child y Sibling
class FamilyDataInline(nested_admin.NestedStackedInline):
    model = FamilyData
    inlines = [ChildInline,SiblingInline]  # Se anidan Child y Sibling
    extra = 0


# Inline para información académica
class InformacionAcademicaInline(nested_admin.NestedStackedInline):  #
    model = InformacionAcademica
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
@admin.register(PersonalData)
class PersonalDataAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        FamilyDataInline,
        InformacionAcademicaInline,
 
        BienesRentasAEPInline,
        SituacionJuridicaInline,
        
    ]
# Columnas visibles en la lista de reclutas
    list_display = (

#CLASE RECLUTA
            "first_name", "second_name", "lastname", "second_lastname",
            "document_type", "document_number", "expedition_date", "expedition_place",
            "passport_number", "passport_date",
             "birth_day",
            "birth_month", "birth_year", "relationships", "profession",
            "profesional_id", "body_marks", "height", "weight", "street_type",
            "principal_number", "principal_letter", "bis", "bis_letter", "quadrant",
            "secondary_number", "secondary_letter", "quadrant_2", "nmbr", "complement",
            "neighborhood","phone_number","landline_phone","city","department","personal_email",
        
    )

# Campos habilitados para búsqueda
    search_fields = (

#PersonalData
            "first_name", "second_name", "lastname", "second_lastname",
            "document_type", "document_number", "expedition_date", "expedition_place",
            "passport_number", "passport_date",
             "birth_day",
            "birth_month", "birth_year", "relationships", "profession",
            "profesional_id", "body_marks", "height", "weight", "street_type",
            "principal_number", "principal_letter", "bis", "bis_letter", "quadrant",
            "secondary_number", "secondary_letter", "quadrant_2", "nmbr", "complement",
            "neighborhood","phone_number","landline_phone","city","department","personal_email",
    )

 # Filtros disponibles en la barra lateral
    list_filter = (
    )


@admin.register(FamilyData)
class FamilyDataAdmin(admin.ModelAdmin):
    inlines = [ChildInline, SiblingInline]

    # ----------  COLUMNS TO DISPLAY IN LIST VIEW  ----------
    list_display = (
        # Spouse Data
        "spouse_name", "spouse_id", "spouse_profession", "spouse_phone",
        "spouse_street_type", "spouse_principal_number", "spouse_principal_letter",
        "spouse_bis", "spouse_bis_letter", "spouse_quadrant",
        "spouse_second_number", "spouse_second_letter", "spouse_second_quadrant",
        "spouse_nmbr", "spouse_complement", "spouse_built_address",

        # Father Data
        "father_name", "father_lives", "father_id", "father_phone", "father_profession",
        "father_street_type", "father_principal_number", "father_principal_letter",
        "father_bis", "father_bis_letter", "father_quadrant",
        "father_second_number", "father_second_letter", "father_second_quadrant",
        "father_nmbr", "father_complement", "father_built_address",

        # Mother Data
        "mother_name", "mother_lives", "mother_id", "mother_phone", "mother_profession",
        "mother_street_type", "mother_principal_number", "mother_principal_letter",
        "mother_bis", "mother_bis_letter", "mother_quadrant",
        "mother_second_number", "mother_second_letter", "mother_second_quadrant",
        "mother_nmbr", "mother_complement", "mother_built_address",
    )

    # ----------  SEARCH FIELDS  ----------
    search_fields = (
        # Spouse Data
        "spouse_name", "spouse_id", "spouse_profession", "spouse_phone",
        "spouse_street_type", "spouse_principal_number", "spouse_principal_letter",
        "spouse_bis", "spouse_bis_letter", "spouse_quadrant",
        "spouse_second_number", "spouse_second_letter", "spouse_second_quadrant",
        "spouse_nmbr", "spouse_complement", "spouse_built_address",

        # Father Data
        "father_name", "father_lives", "father_id", "father_phone", "father_profession",
        "father_street_type", "father_principal_number", "father_principal_letter",
        "father_bis", "father_bis_letter", "father_quadrant",
        "father_second_number", "father_second_letter", "father_second_quadrant",
        "father_nmbr", "father_complement", "father_built_address",

        # Mother Data
        "mother_name", "mother_lives", "mother_id", "mother_phone", "mother_profession",
        "mother_street_type", "mother_principal_number", "mother_principal_letter",
        "mother_bis", "mother_bis_letter", "mother_quadrant",
        "mother_second_number", "mother_second_letter", "mother_second_quadrant",
        "mother_nmbr", "mother_complement", "mother_built_address",
    )

    # ----------  SIDE FILTERS  ----------
    list_filter = ()

@admin.register(Sibling)
class SiblingAdmin(admin.ModelAdmin):

    list_display = (
        "sibling_first_name",
        "sibling_second_name",
        "sibling_lastname",
        "sibling_second_lastname",
        "sibling_id",
        "sibling_built_address",
    )

    search_fields = (
        "sibling_first_name",
        "sibling_second_name",
        "sibling_lastname",
        "sibling_second_lastname",
        "sibling_id",
        "sibling_built_address",
    )


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


