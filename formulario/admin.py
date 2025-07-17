from django.contrib import admin
import nested_admin
from .models import (PersonalData, FamilyData, AcademicInformation,
                     AssetsIncomeAEP, LegalSituation,Child,Sibling)
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


# Inline para AcademicInformation
class AcademicInformationInline(nested_admin.NestedStackedInline):  #
    model = AcademicInformation
    extra = 0




# Inline para AssetsIncomeAEP
class AssetsIncomeAEPInline(nested_admin.NestedStackedInline):
    model = AssetsIncomeAEP
    extra = 0

# Inline para situación jurídica
class SituacionJuridicaInline(nested_admin.NestedStackedInline):
    model = LegalSituation
    extra = 0



# Admin del modelo Recluta con todos los inlines anidados
@admin.register(PersonalData)
class PersonalDataAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        FamilyDataInline,
        AcademicInformationInline,
 
        AssetsIncomeAEPInline,
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


@admin.register(AcademicInformation)
class AcademicInformationAdmin(admin.ModelAdmin):
    # ----------  COLUMNS TO DISPLAY IN THE LIST VIEW  ----------
    list_display = (
        # Formal Education
        "studies_1", "studies_1_year", "studies_title_1", "studies_institution_name_1", "studies_city_1",
        "studies_2", "studies_2_year", "studies_title_2", "studies_institution_name_2", "studies_city_2",

        # Foreign Languages
        "foreign_language_1", "can_read_foreign_language_1", "can_speak_foreign_language_1", "can_write_foreign_language_1",
        "foreign_language_2", "can_read_foreign_language_2", "can_speak_foreign_language_2", "can_write_foreign_language_2",

        # Office Tools
        "word_check", "excel_check", "powerpoint_check", "access_check", "internet_check", "other_check"
    )

    # ----------  SEARCHABLE FIELDS  ----------
    search_fields = (
        # Formal Education
        "studies_1", "studies_1_year", "studies_title_1", "studies_institution_name_1", "studies_city_1",
        "studies_2", "studies_2_year", "studies_title_2", "studies_institution_name_2", "studies_city_2",

        # Foreign Languages
        "foreign_language_1", "can_read_foreign_language_1", "can_speak_foreign_language_1", "can_write_foreign_language_1",
        "foreign_language_2", "can_read_foreign_language_2", "can_speak_foreign_language_2", "can_write_foreign_language_2",

        # Office Tools
        "word_check", "excel_check", "powerpoint_check", "access_check", "internet_check", "other_check"
    )

    # ----------  SIDEBAR FILTERS (EMPTY FOR NOW)  ----------
    list_filter = (
        # You can add filters here later if needed
    )

@admin.register(AssetsIncomeAEP)
class AssetsIncomeAEPAdmin(admin.ModelAdmin):
    # ----------  COLUMNS TO DISPLAY IN THE LIST VIEW  ----------
    list_display = (
        "salary_and_other_income", "layoff_and_interests", "leases", "fee", "other_income",
        "financial_entity_1", "account_type_1", "account_number_1", "financial_entity_2", "account_type_2", "account_number_2",

        "good_type_1", "good_location_1", "good_id_1", "good_appraisal_1",
        "good_type_2", "good_location_2", "good_id_2", "good_appraisal_2",

        "obligation_entity_person_1", "obligation_concept_1", "value_1",
        "obligation_entity_person_2", "obligation_concept_2", "value_2",

        "entity_or_institution_1", "kind_of_member_1",
        "entity_or_institution_2", "kind_of_member_2",

        "company_1", "kind_of_member_AEP_1",
        "company_2", "kind_of_member_AEP_2",
    )

    # ----------  FIELDS TO ENABLE SEARCHING  ----------
    search_fields = (
        "salary_and_other_income", "layoff_and_interests", "leases", "fee", "other_income",
        "financial_entity_1", "account_type_1", "account_number_1", "financial_entity_2", "account_type_2", "account_number_2",

        "good_type_1", "good_location_1", "good_id_1", "good_appraisal_1",
        "good_type_2", "good_location_2", "good_id_2", "good_appraisal_2",

        "obligation_entity_person_1", "obligation_concept_1", "value_1",
        "obligation_entity_person_2", "obligation_concept_2", "value_2",

        "entity_or_institution_1", "kind_of_member_1",
        "entity_or_institution_2", "kind_of_member_2",

        "company_1", "kind_of_member_AEP_1",
        "company_2", "kind_of_member_AEP_2",
    )

    # ----------  SIDEBAR FILTERS  ----------
    list_filter = (
    )


@admin.register(LegalSituation)
class LegalSituationAdmin(admin.ModelAdmin):
    # ----------  COLUMNS TO DISPLAY IN THE LIST VIEW  ----------
    list_display = (
        "process_date_1", "investigation_type_1", "cause_1", "autority_1", "process_state_1", "responsible_1",
        "process_date_2", "investigation_type_2", "cause_2", "autority_2", "process_state_2", "responsible_2",
    )

    # ----------  FIELDS TO ENABLE SEARCHING  ----------
    search_fields = (
        "process_date_1", "investigation_type_1", "cause_1", "autority_1", "process_state_1", "responsible_1",
        "process_date_2", "investigation_type_2", "cause_2", "autority_2", "process_state_2", "responsible_2",
    )

    # ----------  SIDEBAR FILTERS  ----------
    list_filter = (
    )