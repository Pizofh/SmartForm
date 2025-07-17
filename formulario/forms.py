from django import forms
from django.forms import inlineformset_factory 
from .models import (
    PersonalData, FamilyData, AcademicInformation, AssetsIncomeAEP, LegalSituation, Child,Sibling
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, HTML,Field
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.conf import settings
from django.forms import HiddenInput





class BaseHelperMixin:
    """
    Mixin reutilizable que configura un helper de django-crispy-forms para los formularios.
    
    Este helper:
    - Desactiva el <form> tag automático (`form_tag = False`).
    - Aplica clases Bootstrap ('form-label' y 'form-control').
    - Establece dinámicamente un ID en el formulario basado en su prefijo.
    """
    def __init__(self, *args, **kwargs):
        self.prefix = kwargs.get("prefix", "")
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = f"{self.prefix}_form"
        self.helper.label_class = 'form-label'
        self.helper.field_class = 'form-control'
        self.helper.form_show_labels = True


class PersonalDataForm(BaseHelperMixin, forms.ModelForm):

    """
    Formulario ModelForm para la clase `Recluta`.

    Utiliza django-crispy-forms para definir un layout personalizado con fieldsets y columnas.
    Se incluye un campo adicional llamado `direccion_preview` que muestra la dirección formateada
    construida automáticamente con base en los campos de dirección.

    - Los campos de fecha usan widgets tipo 'date'.
    - El layout agrupa los campos de dirección en un Fieldset con vista previa.
    - El método `save` sobrescrito asegura que se almacene la dirección formateada.
    """
   
    direccion_preview = forms.CharField(
        label="Vista previa de dirección",
        required=False,
        widget=forms.HiddenInput(attrs={
            "readonly": "readonly",
            "class": "form-control-plaintext",
            "style": "font-weight: bold;"
        }),
    )

    class Meta:
        model = PersonalData
        fields = [
            "first_name", "second_name", "lastname", "second_lastname",
            "document_type", "document_number", "expedition_date", "expedition_place",
            "passport_number", "passport_date",
            "birth_day","birth_month", "birth_year", "relationships", "profession",
            "profesional_id", "body_marks", "height", "weight", "street_type",
            "principal_number", "principal_letter", "bis", "bis_letter", "quadrant",
            "secondary_number", "secondary_letter", "quadrant_2", "nmbr", "complement",
            "neighborhood","phone_number","landline_phone","city","department","personal_email",
             ]

        widgets = {
            'expedition_date': forms.DateInput(attrs={'type': 'date'}),
            'passport_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False 
        if self.instance.pk:
            self.fields["direccion_preview"].initial = self.instance.direccion_completa

        self.helper.layout = Layout(
            "first_name", "second_name", "lastname", "second_lastname",
            "document_type", "document_number", "expedition_date", "expedition_place",
            "passport_number", "passport_date",
             "birth_day",
            "birth_month", "birth_year", "relationships", "profession",
            "profesional_id", "body_marks", "height", "weight",
       
            
            Fieldset(
                'Dirección',
                Row(
                    Column('street_type', css_class='col-md-2'),
                    Column('principal_number', css_class='col-md-1'),
                    Column('principal_letter', css_class='col-md-2'),
                    Column('bis', css_class='col-md-1'),
                    Column('bis_letter', css_class='col-md-2'),
                    Column('quadrant', css_class='col-md-2'),
                    Column('secondary_number', css_class='col-md-1'),
                    Column('secondary_letter', css_class='col-md-2'),
                    Column('quadrant_2', css_class='col-md-2'),
                    Column('nmbr', css_class='col-md-2'),
                    Column('complement', css_class='col-md-2'),
                ),

      HTML("""
        <div class="mt-3">
        <h5>Address built:</h5>
        <div id="direccion-preview" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
        </div>
            """),
        "direccion_preview"

            ),
            
            
            "neighborhood","phone_number","landline_phone","city","department","personal_email",
        )

    def save(self, commit=True):
        """
        Sobrescribe el método save para almacenar la dirección formateada
        basada en la lógica del modelo `Recluta`.
        """
        instance = super().save(commit=False)
        instance.direccion_formateada = instance.direccion_completa
        if commit:
            instance.save()
        return instance



class FamilyDataForm(BaseHelperMixin, forms.ModelForm):
    """
    Form linked to the FamilyData model.

    This form captures detailed information about the recruit's family background, including:
    - Spouse information (ID, profession, phone, address)
    - Father's and mother's data (alive status, contact, profession, address)
    - Structured address fields with preview hidden fields for dynamic rendering

    Additionally:
    - Uses `crispy-forms` for clean layout with `Fieldset` and `Row`.
    - Includes hidden fields (`*_preview_address`) to show generated formatted addresses.
    - Integrates partial views to add children and siblings via HTML includes.
    - Overrides `save()` to persist formatted address versions in the model.

    The collected data supports a complete family profile of the applicant.
    """

    spouse_preview_address = forms.CharField(required=False, widget=forms.HiddenInput())
    father_preview_address = forms.CharField(required=False, widget=forms.HiddenInput())
    mother_preview_address = forms.CharField(required=False, widget=forms.HiddenInput())
    sibling_preview_address = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = FamilyData
        exclude = ("PersonalData", )
        fields = [
            # Spouse
            "spouse_name", "spouse_id", "spouse_profession", "spouse_phone",
            "spouse_street_type", "spouse_principal_number", "spouse_principal_letter",
            "spouse_bis", "spouse_bis_letter", "spouse_quadrant",
            "spouse_second_number", "spouse_second_letter", "spouse_second_quadrant",
            "spouse_nmbr", "spouse_complement",

            # Father
            "father_name", "father_lives", "father_id", "father_phone", "father_profession",
            "father_street_type", "father_principal_number", "father_principal_letter",
            "father_bis", "father_bis_letter", "father_quadrant",
            "father_second_number", "father_second_letter", "father_second_quadrant",
            "father_nmbr", "father_complement",

            # Mother
            "mother_name", "mother_lives", "mother_id", "mother_phone", "mother_profession",
            "mother_street_type", "mother_principal_number", "mother_principal_letter",
            "mother_bis", "mother_bis_letter", "mother_quadrant",
            "mother_second_number", "mother_second_letter", "mother_second_quadrant",
            "mother_nmbr", "mother_complement",
        ]

    def __init__(self, *args, **kwargs):
        """
        Initializes the `FamilyData` form, configuring crispy-forms helper for layout.

        - Disables <form> tag (form_tag=False) to allow inclusion in composed forms.
        - For existing instances, populates the hidden preview fields with stored formatted addresses.
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        if self.instance.pk:
            self.fields["spouse_preview_address"].initial = self.instance.spouse_built_address
            self.fields["father_preview_address"].initial = self.instance.father_built_address
            self.fields["mother_preview_address"].initial = self.instance.mother_built_address
            self.fields["sibling_preview_address"].initial = self.instance.sibling_built_address

        self.helper.layout = Layout(
            # Spouse Section
            HTML("<h5 class='mt-4'>Spouse Information</h5>"),
            HTML("<hr class='my-4'>"),
            "spouse_name", "spouse_id", "spouse_profession", "spouse_phone",

            Fieldset(
                "Spouse Address",
                Row(
                    Column("spouse_street_type", css_class="col-md-2"),
                    Column("spouse_principal_number", css_class="col-md-1"),
                    Column("spouse_principal_letter", css_class="col-md-2"),
                    Column("spouse_bis", css_class="col-md-1"),
                    Column("spouse_bis_letter", css_class="col-md-2"),
                    Column("spouse_quadrant", css_class="col-md-2"),
                    Column("spouse_second_number", css_class="col-md-1"),
                    Column("spouse_second_letter", css_class="col-md-2"),
                    Column("spouse_second_quadrant", css_class="col-md-2"),
                    Column("spouse_nmbr", css_class="col-md-2"),
                    Column("spouse_complement", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Formatted address:</h5>
                    <div id="direccion-preview_conyugue" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "spouse_preview_address",
            ),

            # Father Section
            HTML("<hr class='my-4'>"),
            HTML("<h5 class='mt-4'>Father Information</h5>"),
            HTML("<hr class='my-4'>"),
            "father_name", "father_lives", "father_id", "father_phone", "father_profession",

            Fieldset(
                "Father Address",
                Row(
                    Column("father_street_type", css_class="col-md-2"),
                    Column("father_principal_number", css_class="col-md-1"),
                    Column("father_principal_letter", css_class="col-md-2"),
                    Column("father_bis", css_class="col-md-1"),
                    Column("father_bis_letter", css_class="col-md-2"),
                    Column("father_quadrant", css_class="col-md-2"),
                    Column("father_second_number", css_class="col-md-1"),
                    Column("father_second_letter", css_class="col-md-2"),
                    Column("father_second_quadrant", css_class="col-md-2"),
                    Column("father_nmbr", css_class="col-md-2"),
                    Column("father_complement", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Formatted address:</h5>
                    <div id="direccion-preview_padre" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "father_preview_address",
            ),

            # Mother Section
            HTML("<hr class='my-4'>"),
            HTML("<h5 class='mt-4'>Mother Information</h5>"),
            HTML("<hr class='my-4'>"),
            "mother_name", "mother_lives", "mother_id", "mother_phone", "mother_profession",

            Fieldset(
                "Mother Address",
                Row(
                    Column("mother_street_type", css_class="col-md-2"),
                    Column("mother_principal_number", css_class="col-md-1"),
                    Column("mother_principal_letter", css_class="col-md-2"),
                    Column("mother_bis", css_class="col-md-1"),
                    Column("mother_bis_letter", css_class="col-md-2"),
                    Column("mother_quadrant", css_class="col-md-2"),
                    Column("mother_second_number", css_class="col-md-1"),
                    Column("mother_second_letter", css_class="col-md-2"),
                    Column("mother_second_quadrant", css_class="col-md-2"),
                    Column("mother_nmbr", css_class="col-md-2"),
                    Column("mother_complement", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Formatted address:</h5>
                    <div id="direccion-preview_madre" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "mother_preview_address",
            ),

            # Children and Siblings Sections
            HTML("<hr class='my-4'>"),
            HTML("<h5>Children:</h5>"),
            HTML("{% include 'formulario/partials/_Child_formset.html' %}"),

            HTML("<hr class='my-4'>"),
            HTML("<h5>Siblings:</h5>"),
            HTML("{% include 'formulario/partials/_Sibling_formset.html' %}"),
        )

    def save(self, commit=True):
        """
        Saves the `FamilyData` instance, updating formatted address fields
        from the corresponding hidden preview inputs.

        If `commit=True`, immediately persists to the DB; otherwise,
        returns unsaved instance for later use.
        """
        instance = super().save(commit=False)
        instance.spouse_built_address = self.cleaned_data.get("spouse_preview_address")
        instance.father_built_address = self.cleaned_data.get("father_preview_address")
        instance.mother_built_address = self.cleaned_data.get("mother_preview_address")
        instance.sibling_built_address = self.cleaned_data.get("sibling_preview_address")

        if commit:
            instance.save()
        return instance


class ChildForm(forms.ModelForm):
    """
    Form for managing Child data (name, age, ID)
    associated with the `Child` model.

    This form uses `crispy-forms` for layout and styling,
    organizing fields in rows and columns for better UX.

    Hidden fields are included for integration with a formset
    (`id` and `DELETE`).
    """

    class Meta:
        model = Child
        fields = ['name', 'age', 'id']

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'age': forms.NumberInput(attrs={'class': 'form-control'}),
        'id': forms.TextInput(attrs={'class': 'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # No <form> inside formset
        self.helper.label_class = "form-label"
        self.helper.field_class = "form-control"
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-5"),
                Column("age", css_class="col-md-2"),
                Column("id", css_class="col-md-3"),
            ),
            Field("id", type="hidden"),
            Field("DELETE", type="hidden"),
        )

        self.helper.render_hidden_fields = True
        self.helper.render_unmentioned_fields = False


ChildFormSet = inlineformset_factory(
    parent_model=FamilyData,
    model=Child,
    form=ChildForm,
    extra=1,
    can_delete=True
)


class SiblingForm(forms.ModelForm):
    """
    Form associated with the `Sibling` model,
    used to capture sibling information of the recruit,
    including personal data, occupation, and structured address.

    Uses `crispy-forms` for visual layout.
    """

    class Meta:
        model = Sibling
        fields = [
            "sibling_lastname", "sibling_second_lastname", "sibling_first_name", "sibling_second_name",
            "sibling_id", "sibling_occupation", "sibling_phone",
            "sibling_street_type", "sibling_principal_number", "sibling_principal_letter",
            "sibling_bis", "sibling_bis_letter", "sibling_quadrant",
            "sibling_second_number", "sibling_second_letter", "sibling_second_quadrant",
            "sibling_nmbr", "sibling_complement", "sibling_built_address"
        ]
        widgets = {
            "sibling_built_address": HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form, configure crispy styles and mark
        the formatted address field as optional.
        """
        super().__init__(*args, **kwargs)
        self.fields['sibling_built_address'].required = False
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = "form-label"
        self.helper.field_class = "form-control"
        self.helper.layout = Layout(
            Row(
                Column("sibling_lastname", css_class="col-md-4"),
                Column("sibling_second_lastname", css_class="col-md-4"),
            ),
            Row(
                Column("sibling_first_name", css_class="col-md-4"),
                Column("sibling_second_name", css_class="col-md-4"),
            ),
            Row(
                Column("sibling_id", css_class="col-md-3"),
                Column("sibling_occupation", css_class="col-md-3"),
                Column("sibling_phone", css_class="col-md-3"),
            ),
            HTML("<hr class='my-4'>"),
            Row(
                Column("sibling_street_type", css_class="col-md-2"),
                Column("sibling_principal_number", css_class="col-md-2"),
                Column("sibling_principal_letter", css_class="col-md-2"),
                Column("sibling_bis", css_class="col-md-2"),
                Column("sibling_bis_letter", css_class="col-md-2"),
                Column("sibling_quadrant", css_class="col-md-2"),
                Column("sibling_second_number", css_class="col-md-2"),
                Column("sibling_second_letter", css_class="col-md-2"),
                Column("sibling_second_quadrant", css_class="col-md-2"),
                Column("sibling_nmbr", css_class="col-md-2"),
                Column("sibling_complement", css_class="col-md-2"),
            ),
            Field("id", type="hidden"),
            Field("DELETE", type="hidden"),
            Field("sibling_built_address", type="hidden"),
        )

        self.helper.render_hidden_fields = True
        self.helper.render_unmentioned_fields = False

    def save(self, commit=True):
        """
        Save the instance of `Sibling`, ensuring the formatted address
        from the hidden field is correctly assigned.
        """
        instance = super().save(commit=False)
        instance.sibling_built_address = self.cleaned_data.get("sibling_built_address")
        if commit:
            instance.save()
        return instance


SiblingFormSet = inlineformset_factory(
    parent_model=FamilyData,
    model=Sibling,
    form=SiblingForm,
    extra=1,
    can_delete=True
)


class AcademicInformationForm(BaseHelperMixin, forms.ModelForm):
    """
    Form associated with the `AcademicInformation` model. Allows registering up to two academic 
    records, foreign language skills (reading, writing, and speaking), and knowledge of 
    office tools such as Word, Excel, PowerPoint, Access, and Internet.

    The form uses `crispy-forms` to organize layout into sections using `Fieldset` and `Row`, 
    with clear visual labels. The `form_tag` is disabled as this form is used inside a larger parent form.
    """

    class Meta:
        model = AcademicInformation
        fields = [
            # Formal Education
            "studies_1", "studies_1_year", "studies_title_1", "studies_institution_name_1", "studies_city_1",
            "studies_2", "studies_2_year", "studies_title_2", "studies_institution_name_2", "studies_city_2",

            # Foreign Languages
            "foreign_language_1", "can_read_foreign_language_1", "can_speak_foreign_language_1", "can_write_foreign_language_1",
            "foreign_language_2", "can_read_foreign_language_2", "can_speak_foreign_language_2", "can_write_foreign_language_2",

            # Office Tools
            "word_check", "excel_check", "powerpoint_check", "access_check", "internet_check", "other_check"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(

            Fieldset(
                "Completed Studies",
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("studies_1", css_class="col-md-3"),
                    Column("studies_1_year", css_class="col-md-1"),
                    Column("studies_title_1", css_class="col-md-3"),
                    Column("studies_institution_name_1", css_class="col-md-3"),
                    Column("studies_city_1", css_class="col-md-2"),
                ),
                Row(
                    Column("studies_2", css_class="col-md-3"),
                    Column("studies_2_year", css_class="col-md-1"),
                    Column("studies_title_2", css_class="col-md-3"),
                    Column("studies_institution_name_2", css_class="col-md-3"),
                    Column("studies_city_2", css_class="col-md-2"),
                ),
            ),
            Fieldset(
                "Foreign Languages",
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("foreign_language_1", css_class="col-md-3"),
                    Column("can_read_foreign_language_1", css_class="col-md-2"),
                    Column("can_speak_foreign_language_1", css_class="col-md-2"),
                    Column("can_write_foreign_language_1", css_class="col-md-2"),
                ),
                Row(
                    Column("foreign_language_2", css_class="col-md-3"),
                    Column("can_read_foreign_language_2", css_class="col-md-2"),
                    Column("can_speak_foreign_language_2", css_class="col-md-2"),
                    Column("can_write_foreign_language_2", css_class="col-md-2"),
                ),
            ),
            Fieldset(
                "Office Tools Proficiency",
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("word_check", css_class="col-md-2"),
                    Column("excel_check", css_class="col-md-2"),
                    Column("powerpoint_check", css_class="col-md-2"),
                    Column("access_check", css_class="col-md-2"),
                    Column("internet_check", css_class="col-md-2"),
                ),
                "other_check",
            )
        )




class AssetsIncomeAEPForm(BaseHelperMixin, forms.ModelForm):
    """
    Form that allows the applicant to register their economic, asset, and financial situation
    corresponding to the AEP format. This form collects:

    - Income received during the last taxable year (salaries, professional fees, rentals, etc.).
    - Information on up to six national or international bank accounts.
    - Details of up to five assets, including type, location, ID, and appraisal.
    - Current financial obligations, specifying creditor, concept, and amount.
    - Participation in organizations or institutions (up to four).
    - Applicant's private economic activities (up to three).

    It also includes a `total_income` field displayed as read-only to reflect
    the total income, calculated dynamically on the client side.

    The `crispy-forms` library is used to visually lay out the form with `Fieldset`,
    `Row`, and `Column`, grouping fields into clear thematic sections with headings
    and visual separators (`<hr>` and HTML titles).

    This form inherits from `BaseHelperMixin` to ensure consistent design with other system forms.
    """

    total_income = forms.CharField(
        label="Total Income",
        required=False,
        widget=forms.TextInput(attrs={
            "readonly": "readonly",
            "class": "form-control fw-bold"
        })
    )

    class Meta:
        model = AssetsIncomeAEP
        fields = [
            "salary_and_other_income", "layoff_and_interests", "representation_expenses",
            "leases", "fee", "other_income",
            "financial_entity_1", "account_type_1", "account_number_1",
            "financial_entity_2", "account_type_2", "account_number_2",

            "good_type_1", "good_location_1", "good_id_1", "good_appraisal_1",
            "good_type_2", "good_location_2", "good_id_2", "good_appraisal_2",

            "obligation_entity_person_1", "obligation_concept_1", "value_1",
            "obligation_entity_person_2", "obligation_concept_2", "value_2",

            "entity_or_institution_1", "kind_of_member_1",
            "entity_or_institution_2", "kind_of_member_2",

            "company_1", "kind_of_member_AEP_1",
            "company_2", "kind_of_member_AEP_2",
        ]

        widgets = {
            "salary_and_other_income": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "layoff_and_interests": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "representation_expenses": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "leases": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "fee": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "other_income": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                "Total Income for the Last Taxable Year",
                HTML("""<hr class="my-4">"""),
                "salary_and_other_income",
                "layoff_and_interests",
                "representation_expenses",
                "leases",
                "fee",
                "other_income",
                HTML("""
                    <div class="mt-3">
                        <label for="id_AssetsIncomeAEPForm-total_income">Total Income</label>
                        <input type="text" id="id_AssetsIncomeAEPForm-total_income" class="form-control fw-bold" readonly />
                    </div>
                """),

                HTML("""<hr class="my-4">"""),
                HTML("<h5>The current, savings or credit card accounts I hold in Colombia and abroad are:</h5>"),
                HTML("""<hr class="my-4">"""),

                Row(
                    Column("financial_entity_1", css_class="col-md-3"),
                    Column("account_type_1", css_class="col-md-3"),
                    Column("account_number_1", css_class="col-md-3"),
                ),
                Row(
                    Column("financial_entity_2", css_class="col-md-3"),
                    Column("account_type_2", css_class="col-md-3"),
                    Column("account_number_2", css_class="col-md-3"),
                ),

                HTML("""<hr class="my-4">"""),
                HTML("<h5>My assets are the following:</h5>"),
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("good_type_1", css_class="col-md-3"),
                    Column("good_location_1", css_class="col-md-3"),
                    Column("good_id_1", css_class="col-md-3"),
                    Column("good_appraisal_1", css_class="col-md-3"),
                ),
                Row(
                    Column("good_type_2", css_class="col-md-3"),
                    Column("good_location_2", css_class="col-md-3"),
                    Column("good_id_2", css_class="col-md-3"),
                    Column("good_appraisal_2", css_class="col-md-3"),
                ),

                HTML("""<hr class="my-4">"""),
                HTML("<h5>My current financial obligations:</h5>"),
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("obligation_entity_person_1", css_class="col-md-3"),
                    Column("obligation_concept_1", css_class="col-md-3"),
                    Column("value_1", css_class="col-md-3"),
                ),
                Row(
                    Column("obligation_entity_person_2", css_class="col-md-3"),
                    Column("obligation_concept_2", css_class="col-md-3"),
                    Column("value_2", css_class="col-md-3"),
                ),

                HTML("""<hr class="my-4">"""),
                HTML("<h5>PARTICIPATION IN ORGANIZATIONS, CORPORATIONS, SOCIETIES, ASSOCIATIONS, NGOs OR OTHERS</h5>"),
                HTML("<h5>I am currently a member of the following organizations:</h5>"),
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("entity_or_institution_1", css_class="col-md-4"),
                    Column("kind_of_member_1", css_class="col-md-3"),
                ),
                Row(
                    Column("entity_or_institution_2", css_class="col-md-4"),
                    Column("kind_of_member_2", css_class="col-md-3"),
                ),

                HTML("""<hr class="my-4">"""),
                HTML("<h5>APPLICANT'S PRIVATE ECONOMIC ACTIVITY</h5>"),
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("company_1", css_class="col-md-4"),
                    Column("kind_of_member_AEP_1", css_class="col-md-3"),
                ),
                Row(
                    Column("company_2", css_class="col-md-4"),
                    Column("kind_of_member_AEP_2", css_class="col-md-3"),
                ),
            ),
        )

class LegalSituationForm(BaseHelperMixin, forms.ModelForm):
    """
    Form to register information about the applicant's legal situation,
    including up to two judicial, criminal, administrative, disciplinary,
    or other legal proceedings in which the applicant has been involved.

    Fields collected for each process:
    - Date of the process
    - Type of investigation
    - Cause or reason
    - Competent authority
    - Current status of the process
    - Applicant's responsibility in the process

    Features:
    - The `PersonalData` field is excluded because it is assigned automatically.
    - Custom widgets are used for date fields.
    - Layout built with `crispy-forms`, grouping information into two clear blocks using `Fieldset`
      and visual separators (`<hr>` and HTML titles).

    This form is part of the required data for background evaluation
    of the applicant, allowing a more complete analysis of their legal history.
    """

    class Meta:
        model = LegalSituation
        exclude = ("PersonalData",)
        fields = [
            "process_date_1", "investigation_type_1", "cause_1", "autority_1", "process_state_1", "responsible_1",
            "process_date_2", "investigation_type_2", "cause_2", "autority_2", "process_state_2", "responsible_2",
        ]

        widgets = {
            "process_date_1": forms.DateInput(attrs={'type': 'date'}),
            "process_date_2": forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                HTML("""<hr class="my-4">"""),
                HTML("<h5>LEGAL SITUATION</h5>"),
                HTML("""<hr class="my-4">"""),
                HTML("<h5>Judicial, criminal, administrative, disciplinary, or other proceedings in which the applicant has been involved</h5>"),
                HTML("""<hr class="my-4">"""),

                Row(
                    Column("process_date_1"),
                    Column("investigation_type_1"),
                    Column("cause_1"),
                ),
                Row(
                    Column("autority_1"),
                    Column("process_state_1"),
                    Column("responsible_1"),
                ),
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("process_date_2"),
                    Column("investigation_type_2"),
                    Column("cause_2"),
                ),
                Row(
                    Column("autority_2"),
                    Column("process_state_2"),
                    Column("responsible_2"),
                ),
            ),
        )




class ConfirmacionForm(BaseHelperMixin, forms.Form):

    """
    Formulario de confirmación que incluye validación CAPTCHA condicional.

    Características:
    - Este formulario se utiliza típicamente al final de un proceso de recolección de datos
      para confirmar la veracidad o aceptación de la información ingresada.
    - Si no se está ejecutando en un entorno de pruebas automatizadas (E2E),
      incluye un campo CAPTCHA (`ReCaptchaV2Checkbox`) para prevenir envíos automáticos.
    - Si la configuración `settings.IS_E2E_TEST` está activada, el campo CAPTCHA se excluye,
      permitiendo que las pruebas se realicen sin requerir validación humana.

    Este comportamiento permite pruebas automatizadas sin fricciones, sin comprometer
    la seguridad en producción.
    """
        
class TuFormulario(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not getattr(settings, 'DISABLE_CAPTCHA', False):
            print("✅ CAPTCHA INCLUIDO")
            self.fields['captcha'] = ReCaptchaField(widget=ReCaptchaV2Checkbox)
        else:
            print("❌ CAPTCHA EXCLUIDO")