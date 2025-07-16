from django import forms
from django.forms import inlineformset_factory 
from .models import (
    PersonalData, FamilyData, InformacionAcademica, BienesRentasAEP, SituacionJuridica, Child,Sibling
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


class InformacionAcademicaForm(BaseHelperMixin, forms.ModelForm):
    """
    Formulario asociado al modelo `InformacionAcademica`. Permite registrar los estudios
    realizados por el recluta, hasta un máximo de cuatro registros académicos, el manejo de 
    idiomas extranjeros (lectura, escritura y habla), y conocimientos en herramientas ofimáticas 
    como Word, Excel, PowerPoint, Access e Internet.

    El formulario utiliza `crispy-forms` para estructurar el layout en secciones organizadas 
    mediante `Fieldset` y `Row`, con etiquetas visuales claras y sin `form_tag`, 
    ya que se usa dentro de un formulario principal más amplio.
    """

    class Meta:
        model = InformacionAcademica
        fields = [
#Estudios
            "estudios_1", "año_estudios_1", "titulo_estudios_1", "nombre_institucion_estudios_1", "ciudad_estudios_1",
            "estudios_2", "año_estudios_2", "titulo_estudios_2", "nombre_institucion_estudios_2", "ciudad_estudios_2",

#Idioma Extranjero
           "idioma_extranjero_1", "lee_idioma_extranjero_1","habla_idioma_extranjero_1","escribe_idioma_extranjero_1",
           "idioma_extranjero_2", "lee_idioma_extranjero_2","habla_idioma_extranjero_2","escribe_idioma_extranjero_2",
#Ofimática
            "word_check", "excel_check", "powerpoint_check", "access_check", "internet_check","otro_check"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            
            Fieldset(
                
              "Estudios Realizados",
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("estudios_1", css_class="col-md-3"),
                    Column("año_estudios_1", css_class="col-md-1"),
                    Column("titulo_estudios_1", css_class="col-md-3"),
                    Column("nombre_institucion_estudios_1", css_class="col-md-3"),
                    Column("ciudad_estudios_1", css_class="col-md-2"),
                ),
             
                Row(
                    Column("estudios_2", css_class="col-md-3"),
                    Column("año_estudios_2", css_class="col-md-1"),
                    Column("titulo_estudios_2", css_class="col-md-3"),
                    Column("nombre_institucion_estudios_2", css_class="col-md-3"),
                    Column("ciudad_estudios_2", css_class="col-md-2"),
                ),
                
            ),
            Fieldset(
                
                "Idiomas Extranjeros",
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("idioma_extranjero_1", css_class="col-md-3"),
                    Column("lee_idioma_extranjero_1", css_class="col-md-2"),
                    Column("habla_idioma_extranjero_1", css_class="col-md-2"),
                    Column("escribe_idioma_extranjero_1", css_class="col-md-2"),
                ),
                Row(
                    Column("idioma_extranjero_2", css_class="col-md-3"),
                    Column("lee_idioma_extranjero_2", css_class="col-md-2"),
                    Column("habla_idioma_extranjero_2", css_class="col-md-2"),
                    Column("escribe_idioma_extranjero_2", css_class="col-md-2"),
                ),
            ),
            Fieldset(
                
                "Especialidades en Sistemas",
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("word_check", css_class="col-md-2"),
                    Column("excel_check", css_class="col-md-2"),
                    Column("powerpoint_check", css_class="col-md-2"),
                    Column("access_check", css_class="col-md-2"),
                    Column("internet_check", css_class="col-md-2"),
                ),
                "otro_check",
            )
        )




class BienesRentasAEPForm(BaseHelperMixin, forms.ModelForm):

    """
    Formulario que permite al aspirante registrar su situación económica, patrimonial y financiera
    correspondiente al formato AEP. Este formulario recopila:

    - Ingresos percibidos durante el último año gravable (salarios, honorarios, arriendos, entre otros).
    - Información de hasta seis cuentas bancarias nacionales o extranjeras.
    - Detalles de hasta cinco bienes patrimoniales, con su tipo, ubicación, identificación y avalúo.
    - Obligaciones económicas vigentes, detallando acreedor, concepto y valor.
    - Participación en organizaciones o entidades (hasta cuatro).
    - Actividades económicas privadas del aspirante (hasta tres).

    Además, incluye un campo `total_ingresos` que se muestra como solo lectura para reflejar
    la suma total de ingresos y se calcula dinámicamente desde el cliente.

    Se utiliza la librería `crispy-forms` para maquetar visualmente el formulario con `Fieldset`,
    `Row` y `Column`, agrupando los campos en secciones temáticas claras con encabezados y separadores
    visuales (`<hr>` y títulos en HTML).

    Este formulario hereda de `BaseHelperMixin` para aplicar un diseño coherente con otros formularios del sistema.
    """
     

    total_ingresos = forms.CharField(
        label="Total de Ingresos",
        required=False,
        widget=forms.TextInput(attrs={
            "readonly": "readonly",
            "class": "form-control fw-bold"
        })
    )

    class Meta:
        model = BienesRentasAEP
        fields = [
        
            "salarios_y_demas_ingresos_laborales","cesantías_e_intereses_de_cesantías","gastos_de_representación","arriendos","honorarios","otros_ingresos_y_rentas",
            "entidad_financiera_1", "tipo_de_cuenta_1", "numero_de_cuenta_1","entidad_financiera_2", "tipo_de_cuenta_2", "numero_de_cuenta_2",
         

            "tipo_bien_1","ubicacion_bien_1","identificacion_bien_1","avaluo_comercial_bien_1",
            "tipo_bien_2","ubicacion_bien_2","identificacion_bien_2","avaluo_comercial_bien_2",
         

            "entidad_o_persona_obligacion_1", "concepto_obligacion_1", "valor_1",
            "entidad_o_persona_obligacion_2", "concepto_obligacion_2", "valor_2",


            "entidad_o_institucion_1","calidad_de_miembro_1",
            "entidad_o_institucion_2","calidad_de_miembro_2",
    

            "empresa_1","calidad_de_miembro_AEP_1",
            "empresa_2","calidad_de_miembro_AEP_2",
       
        ]

        widgets = {
            "salarios_y_demas_ingresos_laborales": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "cesantías_e_intereses_de_cesantías": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "gastos_de_representación" :forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "arriendos": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "honorarios": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
            "otros_ingresos_y_rentas": forms.TextInput(attrs={"inputmode": "numeric", "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                "Total de Ingresos Último Año Gravable",
                HTML("""<hr class="my-4">"""),
                "salarios_y_demas_ingresos_laborales",
                "cesantías_e_intereses_de_cesantías",
                "gastos_de_representación",
                "arriendos",
                "honorarios",
                "otros_ingresos_y_rentas",
                HTML("""
                    <div class="mt-3">
                        <label for="id_BienesRentasAEP-total_ingresos">Total de Ingresos</label>
                        <input type="text" id="id_BienesRentasAEP-total_ingresos" class="form-control fw-bold" readonly />
                    </div>
                """), 

                HTML("""<hr class="my-4">"""),
                HTML("<h5>Las cuentas corrientes, de ahorros o tarjeta de crédito que poseo en Colombia y el Exterior son:</h5>"),
                HTML("""<hr class="my-4">"""),

             Row(
                    Column("entidad_financiera_1", css_class="col-md-3"),
                    Column("tipo_de_cuenta_1", css_class="col-md-3"),
                    Column("numero_de_cuenta_1", css_class="col-md-3"),
                ),
            Row(
                    Column("entidad_financiera_2", css_class="col-md-3"),
                    Column("tipo_de_cuenta_2", css_class="col-md-3"),
                    Column("numero_de_cuenta_2", css_class="col-md-3"),
                ),
      
                HTML("""<hr class="my-4">"""),
                HTML("<h5>Mis bienes patrimoniales son los siguientes:</h5>"),
                HTML("""<hr class="my-4">"""),
            Row(
                    Column("tipo_bien_1", css_class="col-md-3"),
                    Column("ubicacion_bien_1", css_class="col-md-3"),
                    Column("identificacion_bien_1", css_class="col-md-3"),
                    Column("avaluo_comercial_bien_1", css_class="col-md-3"),
                ),
            Row(
                    Column("tipo_bien_2", css_class="col-md-3"),
                    Column("ubicacion_bien_2", css_class="col-md-3"),
                    Column("identificacion_bien_2", css_class="col-md-3"),
                    Column("avaluo_comercial_bien_2", css_class="col-md-3"),
                ),
         
                HTML("""<hr class="my-4">"""),
                HTML("<h5>Mis Obligaciones vigentes a la fecha:</h5>"),
                HTML("""<hr class="my-4">"""),

            Row(
                    Column("entidad_o_persona_obligacion_1", css_class="col-md-3"),
                    Column("concepto_obligacion_1", css_class="col-md-3"),
                    Column("valor_1", css_class="col-md-3"),
                ),
                  Row(
                    Column("entidad_o_persona_obligacion_2", css_class="col-md-3"),
                    Column("concepto_obligacion_2", css_class="col-md-3"),
                    Column("valor_2", css_class="col-md-3"),
                ),
    

                HTML("""<hr class="my-4">"""),
                HTML("<h5>PARTICIPACION EN ORGANIZACIONES, CORPORACIONES, SOCIEDADES, ASOCIACIONES, ONG's u OTROS.</h5>"),
                HTML("<h5>En la actualidad participo como miembro de las siguientes organizaciones:</h5>"),
                HTML("""<hr class="my-4">"""),

            Row(
                    Column("entidad_o_institucion_1", css_class="col-md-4"),
                    Column("calidad_de_miembro_1", css_class="col-md-3"),
                ),
            Row(
                    Column("entidad_o_institucion_2", css_class="col-md-4"),
                    Column("calidad_de_miembro_2", css_class="col-md-3"),
                ),


                HTML("""<hr class="my-4">"""),
                HTML("<h5>ACTIVIDAD ECONÓMICA PRIVADA DEL ASPIRANTE</h5>"),
                HTML("""<hr class="my-4">"""),  
            Row(
                    Column("empresa_1", css_class="col-md-4"),
                    Column("calidad_de_miembro_AEP_1", css_class="col-md-3"),
                ),   
            Row(
                    Column("empresa_2", css_class="col-md-4"),
                    Column("calidad_de_miembro_AEP_2", css_class="col-md-3"),
                ),   
   
            ),
        )


class SituacionJuridicaForm(BaseHelperMixin, forms.ModelForm):

    """
        Formulario para registrar información sobre la situación jurídica del aspirante,
        incluyendo hasta dos procesos judiciales, penales, administrativos, disciplinarios
        o de cualquier otra índole en los que haya estado vinculado.

        Campos recopilados por cada proceso:
        - Fecha del proceso
        - Tipo de investigación
        - Causa o motivo
        - Autoridad competente
        - Estado actual del proceso
        - Responsable del proceso

        Características:
        - Se excluye el campo `recluta` ya que se asigna automáticamente.
        - Se utilizan widgets personalizados para los campos de fecha.
        - Maquetación con `crispy-forms`, agrupando la información en dos bloques claros mediante `Fieldset`
        y separadores visuales (`<hr>` y títulos en HTML).
    
        Este formulario forma parte del conjunto de datos requeridos para la evaluación de antecedentes
        del aspirante, permitiendo un análisis más completo de su historial jurídico.
    """

    class Meta:
        model   = SituacionJuridica
        exclude = ("PersonalData",)
        fields = [
            "fecha_proceso_1", "tipo_de_investigacion_1", "causa_1", "autoridad_1", "estado_del_proceso_1", "responsable_1",
            "fecha_proceso_2", "tipo_de_investigacion_2", "causa_2", "autoridad_2", "estado_del_proceso_2", "responsable_2",
        ]

        widgets = {
            "fecha_proceso_1": forms.DateInput(attrs={'type': 'date'}),
            "fecha_proceso_2": forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                HTML("""<hr class="my-4">"""),
                HTML("<h5>SITUACIÓN JURÍDICA</h5>"),
                HTML("""<hr class="my-4">"""), 
                HTML("<h5>Procesos judiciales, penales, administrativos, querellas u otro tipo de investigaciones a la cual ha estado vinculado</h5>"),
                HTML("""<hr class="my-4">"""), 

            Row(
                Column("fecha_proceso_1"),
                Column("tipo_de_investigacion_1"),
                Column("causa_1"),
                ),
            Row(
                Column("autoridad_1"),
                Column("estado_del_proceso_1"),
                Column("responsable_1"),
            ),
            HTML("""<hr class="my-4">"""),
            Row(
                Column("fecha_proceso_2"),
                Column("tipo_de_investigacion_2"),
                Column("causa_2")
            ),
             Row(
                Column("autoridad_2"),
                Column("estado_del_proceso_2"),
                Column("responsable_2")
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