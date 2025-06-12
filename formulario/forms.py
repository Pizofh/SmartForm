from django import forms
from django.forms import inlineformset_factory 
from .models import (
    Recluta, DatosFamiliares,DireccionesAnteriores, InformacionAcademica,ReferenciasPersonales,
    SectorDefensa, BienesRentasAEP, SituacionJuridica, OtrosDatos, Hijo,Hermano
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, HTML,Field
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox




class BaseHelperMixin:
    def __init__(self, *args, **kwargs):
        self.prefix = kwargs.get("prefix", "")  # capturamos el prefix
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = f"{self.prefix}_form"  # opcional, ayuda a depurar
        self.helper.label_class = 'form-label'
        self.helper.field_class = 'form-control'
        self.helper.form_show_labels = True


class ReclutaForm(BaseHelperMixin, forms.ModelForm):

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
        model = Recluta
        fields = [
            "primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido",
            "tipo_documento", "numero_documento", "fecha_expedición", "lugar_expedición",
            "pasaporte_numero", "fecha_pasaporte", "numero_libretamilitar", "clase_libretamilitar",
            "distrito_militar", "sobrenombres",  "dia_nacimiento",
            "mes_nacimiento", "año_nacimiento", "estado_civil", "profesion_oficio",
            "tarjeta_profesional", "señales_corporales", "estatura", "peso", "tipo_via",
            "numero_principal", "letra_principal", "bis", "letra_bis", "cuadrante",
            "numero_secundario", "letra_secundaria", "cuadrante_dos", "nro", "complemento",
            "barrio","numero_celular","telefono_fijo","ciudad","departamento","correo_electronico_personal",
            "correo_electronico_institucional","facebook","instagram","twitter","otras_redes",
             ]

        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'fecha_expedición': forms.DateInput(attrs={'type': 'date'}),
            'fecha_pasaporte': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False 
        if self.instance.pk:
            self.fields["direccion_preview"].initial = self.instance.direccion_completa

        self.helper.layout = Layout(
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            'tipo_documento', 'numero_documento', 'fecha_expedición', 'lugar_expedición',
            'pasaporte_numero', 'fecha_pasaporte', 'numero_libretamilitar', 'clase_libretamilitar',
            'distrito_militar', 'sobrenombres',  'dia_nacimiento',
            'mes_nacimiento', 'año_nacimiento', 'estado_civil', 'profesion_oficio',
            'tarjeta_profesional', 'señales_corporales', 'estatura', 'peso',
            Fieldset(
                'Dirección',
                Row(
                    Column('tipo_via', css_class='col-md-2'),
                    Column('numero_principal', css_class='col-md-1'),
                    Column('letra_principal', css_class='col-md-2'),
                    Column('bis', css_class='col-md-1'),
                    Column('letra_bis', css_class='col-md-2'),
                    Column('cuadrante', css_class='col-md-2'),
                    Column('numero_secundario', css_class='col-md-1'),
                    Column('letra_secundaria', css_class='col-md-2'),
                    Column('cuadrante_dos', css_class='col-md-2'),
                    Column('nro', css_class='col-md-2'),
                    Column('complemento', css_class='col-md-2'),
                ),

        HTML("""
        <div class="mt-3">
        <h5>Dirección construida:</h5>
        <div id="direccion-preview" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
        </div>
            """),
        "direccion_preview"

            ),
            
            
            'barrio','numero_celular','telefono_fijo','ciudad','departamento','correo_electronico_personal','correo_electronico_institucional',
            'facebook','instagram','twitter','otras_redes',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.direccion_formateada = instance.direccion_completa
        if commit:
            instance.save()
        return instance


class DireccionesAnterioresForm(BaseHelperMixin, forms.ModelForm):

    direccion_preview_anterior_1 = forms.CharField(widget=forms.HiddenInput(), required=False)
    direccion_preview_anterior_2 = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model   = DireccionesAnteriores
        fields = [ "desde_1","hasta_1", "tipo_via_anterior_1",
            "numero_principal_anterior_1", "letra_principal_anterior_1", "bis_anterior_1", "letra_bis_anterior_1", "cuadrante_anterior_1",
            "numero_secundario_anterior_1", "letra_secundaria_anterior_1", "cuadrante_dos_anterior_1", "nro_anterior_1", "complemento_anterior_1", 
            "telefono_direccion_anterior_1_1","telefono_direccion_anterior_1_2", "ciudad_direccion_anterior_1",
            "desde_2" ,"hasta_2", "tipo_via_anterior_2", "numero_principal_anterior_2", "letra_principal_anterior_2", "bis_anterior_2",
            "letra_bis_anterior_2", "cuadrante_anterior_2","numero_secundario_anterior_2", "letra_secundaria_anterior_2",
            "cuadrante_dos_anterior_2", "nro_anterior_2", "complemento_anterior_2", "telefono_direccion_anterior_2_1",
            "telefono_direccion_anterior_2_2","ciudad_direccion_anterior_2","direccion_completa_anterior_1","direccion_completa_anterior_2"
             ]

        widgets = {
            'desde_1': forms.DateInput(attrs={'type': 'date'}),
            'hasta_1': forms.DateInput(attrs={'type': 'date'}),
            'desde_2': forms.DateInput(attrs={'type': 'date'}),
            'hasta_2': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False 

        if self.instance.pk:
            self.fields["direccion_preview_anterior_1"].initial = self.instance.direccion_completa_anterior_1
        if self.instance.pk:
            self.fields["direccion_preview_anterior_2"].initial = self.instance.direccion_completa_anterior_2

        self.helper.layout = Layout(
            Fieldset(
                'Dirección Anterior 1', "desde_1", "hasta_1",
                Row(
                    Column('tipo_via_anterior_1', css_class='col-md-2'),
                    Column('numero_principal_anterior_1', css_class='col-md-1'),
                    Column('letra_principal_anterior_1', css_class='col-md-2'),
                    Column('bis_anterior_1', css_class='col-md-1'),
                    Column('letra_bis_anterior_1', css_class='col-md-2'),
                    Column('cuadrante_anterior_1', css_class='col-md-2'),
                    Column('numero_secundario_anterior_1', css_class='col-md-1'),
                    Column('letra_secundaria_anterior_1', css_class='col-md-2'),
                    Column('cuadrante_dos_anterior_1', css_class='col-md-2'),
                    Column('nro_anterior_1', css_class='col-md-2'),
                    Column('complemento_anterior_1', css_class='col-md-2'),
                ),
        HTML("""
        <div class="mt-3">
        <h5>Dirección construida:</h5>
        <div id="direccion-preview_anterior_1" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
        </div>
            """),
                Row(
                    Column("telefono_direccion_anterior_1_1", css_class='col-md-2'),
                    Column("telefono_direccion_anterior_1_2", css_class='col-md-2'),
                    Column("ciudad_direccion_anterior_1", css_class='col-md-2'),
                )
         

        
            ),

            HTML("""<hr class="my-4">"""),

        Fieldset(
             'Dirección Anterior 2', "desde_2","hasta_2",
               Row(
                    Column('tipo_via_anterior_2', css_class='col-md-2'),
                    Column('numero_principal_anterior_2', css_class='col-md-1'),
                    Column('letra_principal_anterior_2', css_class='col-md-2'),
                    Column('bis_anterior_2', css_class='col-md-1'),
                    Column('letra_bis_anterior_2', css_class='col-md-2'),
                    Column('cuadrante_anterior_2', css_class='col-md-2'),
                    Column('numero_secundario_anterior_2', css_class='col-md-1'),
                    Column('letra_secundaria_anterior_2', css_class='col-md-2'),
                    Column('cuadrante_dos_anterior_2', css_class='col-md-2'),
                    Column('nro_anterior_2', css_class='col-md-2'),
                    Column('complemento_anterior_2', css_class='col-md-2'),
                    ),
        HTML("""
        <div class="mt-3">
        <h5>Dirección construida:</h5>
        <div id="direccion-preview_anterior_2" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
        </div>
            """),
                Row(
                    Column("telefono_direccion_anterior_2_1", css_class='col-md-2'),
                    Column("telefono_direccion_anterior_2_2", css_class='col-md-2'),
                    Column("ciudad_direccion_anterior_2", css_class='col-md-2'),
                )
                 

            
            
            #'barrio','numero_celular','telefono_fijo','ciudad','departamento','correo_electronico_personal','correo_electronico_institucional','facebook','instagram','twitter','otras_redes','genero',  'fecha_ingreso',
            #'dependencia_destino', 'unidad_negocio', 'cargo', 'tipo_contrato',
            #'hv_pdf', 'certificado_eps', 'certificado_arl', 'certificado_pension'
        )
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.direccion_completa_anterior_1 = self.cleaned_data.get("direccion_preview_anterior_1")
        instance.direccion_completa_anterior_2 = self.cleaned_data.get("direccion_preview_anterior_2")

        if commit:
            instance.save()
        return instance


class DatosFamiliaresForm(BaseHelperMixin, forms.ModelForm):
    direccion_preview_conyugue = forms.CharField(required=False, widget=forms.HiddenInput())
    direccion_preview_padre = forms.CharField(required=False, widget=forms.HiddenInput())
    direccion_preview_madre = forms.CharField(required=False, widget=forms.HiddenInput())
    direccion_preview_hermano = forms.CharField(required=False, widget=forms.HiddenInput())


    class Meta:
        model = DatosFamiliares
        exclude = ("recluta", )
        fields = [
#Datos Conyugue
            "nombre_conyugue", "cedula_conyugue", "profesion_oficio_conyugue", "celular_conyugue",
            "tipo_via_conyugue", "numero_principal_conyugue", "letra_principal_conyugue",
            "bis_conyugue", "letra_bis_conyugue", "cuadrante_conyugue",
            "numero_secundario_conyugue", "letra_secundaria_conyugue", "cuadrante_dos_conyugue",
            "nro_conyugue", "complemento_conyugue",

#Datos Padre
            "nombre_padre", "vive_padre","identificación_padre","telefono_padre", "oficio_profesion_padre",
            "tipo_via_padre", "numero_principal_padre", "letra_principal_padre","bis_padre", "letra_bis_padre", "cuadrante_padre",
            "numero_secundario_padre", "letra_secundaria_padre", "cuadrante_dos_padre","nro_padre", "complemento_padre",
#Datos Madre
            "nombre_madre", "vive_madre",
            "identificación_madre","telefono_madre", "oficio_profesion_madre","tipo_via_madre", "numero_principal_madre", "letra_principal_madre",
            "bis_madre", "letra_bis_madre", "cuadrante_madre","numero_secundario_madre", "letra_secundaria_madre", "cuadrante_dos_madre","nro_madre", "complemento_madre",

        ]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False 

        if self.instance.pk:
            self.fields["direccion_preview_conyugue"].initial = self.instance.direccion_completa_conyugue
            self.fields["direccion_preview_padre"].initial = self.instance.direccion_completa_padre
            self.fields["direccion_preview_madre"].initial = self.instance.direccion_completa_madre
            self.fields["direccion_preview_hermano"].initial = self.instance.direccion_completa_hermano


   

    
        self.helper.layout = Layout(
#ESPACIOS CONYGUE 
            HTML("<h5 class='mt-4'>Información del Cónyugue</h5>"),
            HTML("""<hr class="my-4">"""),
            "nombre_conyugue", "cedula_conyugue", "profesion_oficio_conyugue", "celular_conyugue", 
            
           
            Fieldset(
                "Dirección Residencia del Conyugue",
                Row(
                    Column("tipo_via_conyugue", css_class="col-md-2"),
                    Column("numero_principal_conyugue", css_class="col-md-1"),
                    Column("letra_principal_conyugue", css_class="col-md-2"),
                    Column("bis_conyugue", css_class="col-md-1"),
                    Column("letra_bis_conyugue", css_class="col-md-2"),
                    Column("cuadrante_conyugue", css_class="col-md-2"),
                    Column("numero_secundario_conyugue", css_class="col-md-1"),
                    Column("letra_secundaria_conyugue", css_class="col-md-2"),
                    Column("cuadrante_dos_conyugue", css_class="col-md-2"),
                    Column("nro_conyugue", css_class="col-md-2"),
                    Column("complemento_conyugue", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_conyugue" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_conyugue",    

                HTML("""<hr class="my-4">"""),
                HTML("<h5 class='mt-4'>Información del Padre</h5>"),
                HTML("""<hr class="my-4">"""),
#ESPACIOS PADRE   
                "nombre_padre", "vive_padre","identificación_padre","telefono_padre","oficio_profesion_padre",

            Fieldset(
                "Dirección Residencia del Padre",
                Row(
                    Column("tipo_via_padre", css_class="col-md-2"),
                    Column("numero_principal_padre", css_class="col-md-1"),
                    Column("letra_principal_padre", css_class="col-md-2"),
                    Column("bis_padre", css_class="col-md-1"),
                    Column("letra_bis_padre", css_class="col-md-2"),
                    Column("cuadrante_padre", css_class="col-md-2"),
                    Column("numero_secundario_padre", css_class="col-md-1"),
                    Column("letra_secundaria_padre", css_class="col-md-2"),
                    Column("cuadrante_dos_padre", css_class="col-md-2"),
                    Column("nro_padre", css_class="col-md-2"),
                    Column("complemento_padre", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_padre" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_padre",           
            ),
#ESPACIOS MADRE 

            HTML("""<hr class="my-4">"""),
                HTML("<h5 class='mt-4'>Información de la Madre</h5>"),
                HTML("""<hr class="my-4">"""),
                "nombre_madre", "vive_madre","identificación_madre","telefono_madre","oficio_profesion_madre",

            Fieldset(
                "Dirección Residencia de la madre",
                Row(
                    Column("tipo_via_madre", css_class="col-md-2"),
                    Column("numero_principal_madre", css_class="col-md-1"),
                    Column("letra_principal_madre", css_class="col-md-2"),
                    Column("bis_madre", css_class="col-md-1"),
                    Column("letra_bis_madre", css_class="col-md-2"),
                    Column("cuadrante_madre", css_class="col-md-2"),
                    Column("numero_secundario_madre", css_class="col-md-1"),
                    Column("letra_secundaria_madre", css_class="col-md-2"),
                    Column("cuadrante_dos_madre", css_class="col-md-2"),
                    Column("nro_madre", css_class="col-md-2"),
                    Column("complemento_madre", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_madre" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_madre",
            ),

            HTML("<hr class='my-4'>"),
            HTML("<h5>Hijos:</h5>"),
            HTML("{% include 'formulario/partials/_hijos_formset.html' %}"),  
    

            HTML("<hr class='my-4'>"),
            HTML("<h5>Hermanos:</h5>"),
            HTML("{% include 'formulario/partials/_hermanos_formset.html' %}"),  
       


            
            ),
            
        )
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.direccion_formateada_conyugue = self.cleaned_data.get("direccion_preview_conyugue")
        instance.direccion_formateada_padre = self.cleaned_data.get("direccion_preview_padre")
        instance.direccion_formateada_madre = self.cleaned_data.get("direccion_preview_madre")
        instance.direccion_formateada_hermano = self.cleaned_data.get("direccion_preview_hermano")

        if commit:
            instance.save()
        return instance


class HijoForm(forms.ModelForm):
    
    class Meta:
        model = Hijo
        fields = ['nombre', 'edad', 'identificacion']

    widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
            # ➜ ESTO da a cada hijo el mismo “look” crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper               = FormHelper()
        self.helper.form_tag      = False          # dentro del formset no queremos <form>
        self.helper.label_class   = "form-label"
        self.helper.field_class   = "form-control"
        self.helper.layout = Layout(
            Row(
                Column("nombre",         css_class="col-md-5"),
                Column("edad",           css_class="col-md-2"),
                Column("identificacion", css_class="col-md-3"),
            ),
                Field("id",     type="hidden"),
                Field("DELETE", type="hidden"),
        )

        self.helper.render_hidden_fields   = True
        self.helper.render_unmentioned_fields = False


HijoFormSet = inlineformset_factory(
    parent_model=DatosFamiliares,      # quién es el “padre”
    model=Hijo,                        # modelo hijo
    form=HijoForm,                     # el form que ya tenías
    extra=1,
    can_delete=True
)

class HermanoForm(forms.ModelForm):
    
    class Meta:
        model = Hermano
        fields = ["primer_apellido_hermano","segundo_apellido_hermano","primer_nombre_hermano", "segundo_nombre_hermano", "identificacion_hermano", "ocupacion_hermano",
            "celular_hermano","tipo_via_hermano","numero_principal_hermano", "letra_principal_hermano", "bis_hermano", "letra_bis_hermano", "cuadrante_hermano",
            "numero_secundario_hermano", "letra_secundaria_hermano", "cuadrante_dos_hermano", "nro_hermano", "complemento_hermano",]

    widgets = {

        }
        
            # ➜ ESTO da a cada hijo el mismo “look” crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper               = FormHelper()
        self.helper.form_tag      = False          # dentro del formset no queremos <form>
        self.helper.label_class   = "form-label"
        self.helper.field_class   = "form-control"
        self.helper.layout = Layout(
            Row(
                Column("primer_apellido_hermano",       css_class="col-md-4"),
                Column("segundo_apellido_hermano",      css_class="col-md-4"),
      
            ),
              Row(
                Column("primer_nombre_hermano",         css_class="col-md-4"),
                Column("segundo_nombre_hermano",       css_class="col-md-4"),
          
            ),
              Row(
                Column("identificacion_hermano",      css_class="col-md-3"),
                Column("ocupacion_hermano",         css_class="col-md-3"),
                Column("celular_hermano",       css_class="col-md-3"),
            ),
            HTML("<hr class='my-4'>"),
            
              Row(
                    Column("tipo_via_hermano", css_class="col-md-2"),
                    Column("numero_principal_hermano", css_class="col-md-2"),
                    Column("letra_principal_hermano", css_class="col-md-2"),
                    Column("bis_hermano", css_class="col-md-2"),
                    Column("letra_bis_hermano", css_class="col-md-2"),
                    Column("cuadrante_hermano", css_class="col-md-2"),
                    Column("numero_secundario_hermano", css_class="col-md-2"),
                    Column("letra_secundaria_hermano", css_class="col-md-2"),
                    Column("cuadrante_dos_hermano", css_class="col-md-2"),
                    Column("nro_hermano", css_class="col-md-2"),
                    Column("complemento_hermano", css_class="col-md-2"),
            ),
            
                Field("id",     type="hidden"),
                Field("DELETE", type="hidden"),
        )

        self.helper.render_hidden_fields   = True
        self.helper.render_unmentioned_fields = False


HermanoFormSet = inlineformset_factory(
    parent_model=DatosFamiliares,      # quién es el “padre”
    model=Hermano,                        # modelo hijo
    form=HermanoForm,                     # el form que ya tenías
    extra=1,
    can_delete=True
)



class InformacionAcademicaForm(BaseHelperMixin, forms.ModelForm):
    class Meta:
        model = InformacionAcademica
        fields = [
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
                
                Row(
                    Column("estudios_3", css_class="col-md-3"),
                    Column("año_estudios_3", css_class="col-md-1"),
                    Column("titulo_estudios_3", css_class="col-md-3"),
                    Column("nombre_institucion_estudios_3", css_class="col-md-3"),
                    Column("ciudad_estudios_3", css_class="col-md-2"),
                ),
               
                Row(
                    Column("estudios_4", css_class="col-md-3"),
                    Column("año_estudios_4", css_class="col-md-1"),
                    Column("titulo_estudios_4", css_class="col-md-3"),
                    Column("nombre_institucion_estudios_4", css_class="col-md-3"),
                    Column("ciudad_estudios_4", css_class="col-md-2"),
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


class ReferenciasPersonalesForm(forms.ModelForm):
    direccion_preview_referencia_1 = forms.CharField(required=False, widget=forms.HiddenInput())
    direccion_preview_referencia_2 = forms.CharField(required=False, widget=forms.HiddenInput())
    direccion_preview_referencia_3 = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = ReferenciasPersonales
        fields = [
# Referencia 1
            "nombre_referencia_1", "ocupacion_referencia_1", "empresa_referencia_1", "tiempo_referencia_1", "ciudad_referencia_1", "telefono_referencia_1",
            "tipo_via_referencia_1", "numero_principal_referencia_1", "letra_principal_referencia_1", "bis_referencia_1", "letra_bis_referencia_1",
            "cuadrante_referencia_1", "numero_secundario_referencia_1", "letra_secundaria_referencia_1", "cuadrante_dos_referencia_1",
            "nro_referencia_1", "complemento_referencia_1",

# Referencia 2
            "nombre_referencia_2", "ocupacion_referencia_2", "empresa_referencia_2", "tiempo_referencia_2", "ciudad_referencia_2", "telefono_referencia_2",
            "tipo_via_referencia_2", "numero_principal_referencia_2", "letra_principal_referencia_2", "bis_referencia_2", "letra_bis_referencia_2",
            "cuadrante_referencia_2", "numero_secundario_referencia_2", "letra_secundaria_referencia_2", "cuadrante_dos_referencia_2",
            "nro_referencia_2", "complemento_referencia_2",
# Referencia 3
            "nombre_referencia_3", "ocupacion_referencia_3", "empresa_referencia_3", "tiempo_referencia_3", "ciudad_referencia_3", "telefono_referencia_3",
            "tipo_via_referencia_3", "numero_principal_referencia_3", "letra_principal_referencia_3", "bis_referencia_3", "letra_bis_referencia_3",
            "cuadrante_referencia_3", "numero_secundario_referencia_3", "letra_secundaria_referencia_3", "cuadrante_dos_referencia_3",
            "nro_referencia_3", "complemento_referencia_3",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        if self.instance.pk:
            self.fields["direccion_preview_referencia_1"].initial = self.instance.direccion_completa_anterior_1
            self.fields["direccion_preview_referencia_2"].initial = self.instance.direccion_completa_anterior_2
            self.fields["direccion_preview_referencia_3"].initial = self.instance.direccion_completa_anterior_3
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
           
#Referencia 1
            Fieldset(
                "Referencia 1",
                HTML("""<hr class="my-4">"""),
                "nombre_referencia_1", "ocupacion_referencia_1", "empresa_referencia_1", "tiempo_referencia_1",
                "ciudad_referencia_1", "telefono_referencia_1",
                Row(
                    Column("tipo_via_referencia_1", css_class="col-md-2"),
                    Column("numero_principal_referencia_1", css_class="col-md-1"),
                    Column("letra_principal_referencia_1", css_class="col-md-2"),
                    Column("bis_referencia_1", css_class="col-md-1"),
                    Column("letra_bis_referencia_1", css_class="col-md-2"),
                    Column("cuadrante_referencia_1", css_class="col-md-2"),
                    Column("numero_secundario_referencia_1", css_class="col-md-1"),
                    Column("letra_secundaria_referencia_1", css_class="col-md-2"),
                    Column("cuadrante_dos_referencia_1", css_class="col-md-2"),
                    Column("nro_referencia_1", css_class="col-md-2"),
                    Column("complemento_referencia_1", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_referencia_1" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_referencia_1",
            ),
#Referencia 2
          
            Fieldset(
                "Referencia 2",
                HTML("""<hr class="my-4">"""),
                "nombre_referencia_2", "ocupacion_referencia_2", "empresa_referencia_2", "tiempo_referencia_2",
                "ciudad_referencia_2", "telefono_referencia_2",
                Row(
                    Column("tipo_via_referencia_2", css_class="col-md-2"),
                    Column("numero_principal_referencia_2", css_class="col-md-1"),
                    Column("letra_principal_referencia_2", css_class="col-md-2"),
                    Column("bis_referencia_2", css_class="col-md-1"),
                    Column("letra_bis_referencia_2", css_class="col-md-2"),
                    Column("cuadrante_referencia_2", css_class="col-md-2"),
                    Column("numero_secundario_referencia_2", css_class="col-md-1"),
                    Column("letra_secundaria_referencia_2", css_class="col-md-2"),
                    Column("cuadrante_dos_referencia_2", css_class="col-md-2"),
                    Column("nro_referencia_2", css_class="col-md-2"),
                    Column("complemento_referencia_2", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_referencia_2" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_referencia_2",
            ),
#Referencia 3
            Fieldset(
                "Referencia 3",
                HTML("""<hr class="my-4">"""),
                "nombre_referencia_3", "ocupacion_referencia_3", "empresa_referencia_3", "tiempo_referencia_3",
                "ciudad_referencia_3", "telefono_referencia_3",
                Row(
                    Column("tipo_via_referencia_3", css_class="col-md-2"),
                    Column("numero_principal_referencia_3",css_class="col-md-1"),
                    Column("letra_principal_referencia_3",css_class="col-md-2"),
                    Column("bis_referencia_3",css_class="col-md-1"),
                    Column("letra_bis_referencia_3",css_class="col-md-2"), 
                    Column("cuadrante_referencia_3",css_class="col-md-2"),
                    Column("numero_secundario_referencia_3",css_class="col-md-1"),
                    Column("letra_secundaria_referencia_3",css_class="col-md-2"),
                    Column("cuadrante_dos_referencia_3",css_class="col-md-2"),
                    Column("nro_referencia_3",css_class="col-md-2"),
                    Column("complemento_referencia_3",css_class="col-md-2")
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_referencia_3" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_referencia_3",
            ),
        )
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.direccion_formateada_referencia_1 = self.cleaned_data.get("direccion_preview_referencia_1")
        instance.direccion_formateada_referencia_2 = self.cleaned_data.get("direccion_preview_referencia_2")
        instance.direccion_formateada_referencia_3 = self.cleaned_data.get("direccion_preview_referencia_3")
        if commit:
            instance.save()
        return instance


class SectorDefensaForm(BaseHelperMixin, forms.ModelForm):
    direccion_preview_sd_1 = forms.CharField(required=False, widget=forms.HiddenInput())
    direccion_preview_sd_2 = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = SectorDefensa
        fields = [

# Referencia 1
    "nombresyapellidos_sd_1", "cargo_sd_1","entidad_sd_1","unidad_militar_sd_1", "celular_sd_1", "tipo_via_sd_1",
    "numero_principal_sd_1","letra_principal_sd_1","bis_sd_1","letra_bis_sd_1", "cuadrante_sd_1", "numero_secundario_sd_1", 
    "letra_secundaria_sd_1","cuadrante_dos_sd_1","nro_sd_1", "complemento_sd_1",

# Referencia 1
    "nombresyapellidos_sd_2", "cargo_sd_2","entidad_sd_2","unidad_militar_sd_2", "celular_sd_2", "tipo_via_sd_2",
    "numero_principal_sd_2","letra_principal_sd_2","bis_sd_2","letra_bis_sd_2", "cuadrante_sd_2", "numero_secundario_sd_2", 
    "letra_secundaria_sd_2","cuadrante_dos_sd_2","nro_sd_2", "complemento_sd_2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        if self.instance.pk:
            self.fields["direccion_preview_referencia_1"].initial = self.instance.direccion_completa_anterior_1
            self.fields["direccion_preview_referencia_2"].initial = self.instance.direccion_completa_anterior_2

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
           
#Referencia 1
            Fieldset(
                "Familiar o Conocido que trabaja en el Sector Defensa 1",
                HTML("""<hr class="my-4">"""),
                "nombresyapellidos_sd_1", "cargo_sd_1","entidad_sd_1","unidad_militar_sd_1", "celular_sd_1",

                Row(
                    Column("tipo_via_sd_1", css_class="col-md-2"),
                    Column("numero_principal_sd_1", css_class="col-md-1"),
                    Column("letra_principal_sd_1", css_class="col-md-2"),
                    Column("bis_sd_1", css_class="col-md-1"),
                    Column("letra_bis_sd_1", css_class="col-md-2"),
                    Column("cuadrante_sd_1", css_class="col-md-2"),
                    Column("numero_secundario_sd_1", css_class="col-md-1"),
                    Column("letra_secundaria_sd_1", css_class="col-md-2"),
                    Column("cuadrante_dos_sd_1", css_class="col-md-2"),
                    Column("nro_sd_1", css_class="col-md-2"),
                    Column("complemento_sd_1", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_sd_1" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_sd_1",
            ),

#Referencia 2
          
                 Fieldset(
                "Familiar o Conocido que trabaja en el Sector Defensa 1",
                HTML("""<hr class="my-4">"""),
                "nombresyapellidos_sd_2", "cargo_sd_2","entidad_sd_2","unidad_militar_sd_2", "celular_sd_2",

                Row(
                    Column("tipo_via_sd_2", css_class="col-md-2"),
                    Column("numero_principal_sd_2", css_class="col-md-1"),
                    Column("letra_principal_sd_2", css_class="col-md-2"),
                    Column("bis_sd_2", css_class="col-md-1"),
                    Column("letra_bis_sd_2", css_class="col-md-2"),
                    Column("cuadrante_sd_2", css_class="col-md-2"),
                    Column("numero_secundario_sd_2", css_class="col-md-1"),
                    Column("letra_secundaria_sd_2", css_class="col-md-2"),
                    Column("cuadrante_dos_sd_2", css_class="col-md-2"),
                    Column("nro_sd_2", css_class="col-md-2"),
                    Column("complemento_sd_2", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_sd_2" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_sd_2",
            ),

        )
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.direccion_formateada_sd_1 = self.cleaned_data.get("direccion_preview_sd_1")
        instance.direccion_formateada_sd_2 = self.cleaned_data.get("direccion_preview_sd_2")

        if commit:
            instance.save()
        return instance



class BienesRentasAEPForm(BaseHelperMixin, forms.ModelForm):
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
            Row(
                    Column("entidad_financiera_3", css_class="col-md-3"),
                    Column("tipo_de_cuenta_3", css_class="col-md-3"),
                    Column("numero_de_cuenta_3", css_class="col-md-3"),
                ),
            Row(
                    Column("entidad_financiera_4", css_class="col-md-3"),
                    Column("tipo_de_cuenta_4", css_class="col-md-3"),
                    Column("numero_de_cuenta_4", css_class="col-md-3"),
                ),
            Row(
                    Column("entidad_financiera_5", css_class="col-md-3"),
                    Column("tipo_de_cuenta_5", css_class="col-md-3"),
                    Column("numero_de_cuenta_5", css_class="col-md-3"),
                ),
            Row(
                    Column("entidad_financiera_6", css_class="col-md-3"),
                    Column("tipo_de_cuenta_6", css_class="col-md-3"),
                    Column("numero_de_cuenta_6", css_class="col-md-3"),
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
            Row(
                    Column("tipo_bien_3", css_class="col-md-3"),
                    Column("ubicacion_bien_3", css_class="col-md-3"),
                    Column("identificacion_bien_3", css_class="col-md-3"),
                    Column("avaluo_comercial_bien_3", css_class="col-md-3"),
                ),
            Row(
                    Column("tipo_bien_4", css_class="col-md-3"),
                    Column("ubicacion_bien_4", css_class="col-md-3"),
                    Column("identificacion_bien_4", css_class="col-md-3"),
                    Column("avaluo_comercial_bien_4", css_class="col-md-3"),
                ),
            Row(
                    Column("tipo_bien_5", css_class="col-md-3"),
                    Column("ubicacion_bien_5", css_class="col-md-3"),
                    Column("identificacion_bien_5", css_class="col-md-3"),
                    Column("avaluo_comercial_bien_5", css_class="col-md-3"),
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
    
            Row(
                    Column("entidad_o_persona_obligacion_3", css_class="col-md-3"),
                    Column("concepto_obligacion_3", css_class="col-md-3"),
                    Column("valor_3", css_class="col-md-3"),
                ),
    
            Row(
                    Column("entidad_o_persona_obligacion_4", css_class="col-md-3"),
                    Column("concepto_obligacion_4", css_class="col-md-3"),
                    Column("valor_4", css_class="col-md-3"),
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
            Row(
                    Column("entidad_o_institucion_3", css_class="col-md-4"),
                    Column("calidad_de_miembro_3", css_class="col-md-3"),
                ),
            Row(
                    Column("entidad_o_institucion_4", css_class="col-md-4"),
                    Column("calidad_de_miembro_4", css_class="col-md-3"),
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
            Row(
                    Column("empresa_3", css_class="col-md-4"),
                    Column("calidad_de_miembro_AEP_3", css_class="col-md-3"),
                ),   
            ),
        )


class SituacionJuridicaForm(BaseHelperMixin, forms.ModelForm):
    class Meta:
        model   = SituacionJuridica
        exclude = ("recluta",)
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


class OtrosDatosForm(BaseHelperMixin, forms.ModelForm):
    direccion_preview_recomendante = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model   = OtrosDatos
        exclude = ("recluta",)
        fields = {     
                    "fecha_viaje_1","pais_visitado_1","motivo_1","permanencia_1",
                    "fecha_viaje_2","pais_visitado_2","motivo_2","permanencia_2",
                    "fecha_viaje_3","pais_visitado_3","motivo_3","permanencia_3",

                    "recomendante","celular_recomendante","labora_en_indumil","nombres_y_apellidos_recomendante_1", 
                    "nombres_y_apellidos_recomendante_2", "cargo_recomendante_1", "cargo_recomendante_2",
                    "unidad_negocio_recomendante_1","unidad_negocio_recomendante_2",

                    "tipo_via_recomendante","numero_principal_recomendante", "letra_principal_recomendante", "bis_recomendante",
                    "letra_bis_recomendante", "cuadrante_recomendante", "numero_secundario_recomendante","letra_secundaria_recomendante",
                    "cuadrante_dos_recomendante","nro_recomendante", "complemento_recomendante",
                    "razon_de_vinculo",
                    "direccion_preview_recomendante",
                    }
        widgets = {
            "fecha_viaje_1": forms.DateInput(attrs={'type': 'date'}),
            "fecha_viaje_2": forms.DateInput(attrs={'type': 'date'}),
            "fecha_viaje_3": forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
  

        self.helper.layout = Layout(
            Fieldset("",
                HTML("""
                        <hr class="my-5">
                        <div class="p-3 mb-4" style="background-color: #f0f0f0; border-left: 4px solid #007bff;">
                        <h5 class="mb-0">VIAJES AL EXTERIOR</h5>
                        </div>
                    """),
                Row(
                    Column("fecha_viaje_1"),
                    Column("pais_visitado_1"),
                    Column("motivo_1"),
                    Column("permanencia_1"),
                ),
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("fecha_viaje_2"),
                    Column("pais_visitado_2"),
                    Column("motivo_2"),
                    Column("permanencia_2"),
                ),
                HTML("""<hr class="my-4">"""),
                Row(
                    Column("fecha_viaje_3"),
                    Column("pais_visitado_3"),
                    Column("motivo_3"),
                    Column("permanencia_3"),
                ),


                HTML("""
                        <hr class="my-5">
                        <div class="p-3 mb-4" style="background-color: #f0f0f0; border-left: 4px solid #007bff;">
                        <h5 class="mb-0">OTROS DATOS DE INTERÉS</h5>
                        </div>
                    """),
                
                "recomendante",
                HTML("<h5>Dirección</h5>"),
                HTML("""<hr class="my-4">"""),
                
             
                Row(
                    Column("tipo_via_recomendante", css_class="col-md-2"),
                    Column("numero_principal_recomendante", css_class="col-md-1"),
                    Column("letra_principal_recomendante", css_class="col-md-2"),
                    Column("bis_recomendante", css_class="col-md-1"),
                    Column("letra_bis_recomendante", css_class="col-md-2"),
                    Column("cuadrante_recomendante", css_class="col-md-2"),
                    Column("numero_secundario_recomendante", css_class="col-md-1"),
                    Column("letra_secundaria_recomendante", css_class="col-md-2"),
                    Column("cuadrante_dos_recomendante", css_class="col-md-2"),
                    Column("nro_recomendante", css_class="col-md-2"),
                    Column("complemento_recomendante", css_class="col-md-2"),
                ),
                HTML("""
                <div class="mt-3">
                    <h5>Dirección construida:</h5>
                    <div id="direccion-preview_recomendante" class="alert alert-info py-2 px-3 mb-0 fw-bold"></div>
                </div>
                """),
                "direccion_preview_recomendante",
                   "celular_recomendante","labora_en_indumil",
                   Row(
                       Column("nombres_y_apellidos_recomendante_1", css_class="col-md-4"),
                       Column("cargo_recomendante_1", css_class="col-md-3"),
                       Column("unidad_negocio_recomendante_1", css_class="col-md-3"),
                       ),

                    Row(
                        Column("nombres_y_apellidos_recomendante_2", css_class="col-md-4"),
                        Column("cargo_recomendante_2", css_class="col-md-3"),
                        Column("unidad_negocio_recomendante_2", css_class="col-md-3"),
                    ),
                    "razon_de_vinculo",
            )

        )
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.direccion_formateada_recomendante = self.cleaned_data.get("direccion_preview_recomendante")
        if commit:
            instance.save()
        return instance


class ConfirmacionForm(BaseHelperMixin, forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
