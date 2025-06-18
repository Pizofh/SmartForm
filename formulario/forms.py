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


class ReclutaForm(BaseHelperMixin, forms.ModelForm):

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
        """
        Sobrescribe el método save para almacenar la dirección formateada
        basada en la lógica del modelo `Recluta`.
        """
        instance = super().save(commit=False)
        instance.direccion_formateada = instance.direccion_completa
        if commit:
            instance.save()
        return instance


class DireccionesAnterioresForm(BaseHelperMixin, forms.ModelForm):

    """
    Formulario para el modelo DireccionesAnteriores.

    Permite capturar hasta dos direcciones anteriores de un recluta, incluyendo:
    - Períodos de residencia (desde/hasta)
    - Componentes estructurados de dirección (tipo de vía, número, letra, bis, cuadrante)
    - Ciudad y teléfonos asociados a cada dirección

    Este formulario:
    - Usa campos ocultos para mostrar una vista previa de las direcciones formateadas (`direccion_preview_anterior_1`, `direccion_preview_anterior_2`)
    - Utiliza `crispy-forms` para organizar visualmente las secciones en fieldsets
    - Sobrescribe el método `save()` para almacenar correctamente las vistas previas en los campos de modelo `direccion_completa_anterior_1` y `direccion_completa_anterior_2`
    """


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
        
        )
        )

    def save(self, commit=True):
        """
        Guarda el formulario incluyendo los campos de dirección formateada que fueron generados
        dinámicamente y asignados desde los campos ocultos de vista previa.
        """

        instance = super().save(commit=False)
        instance.direccion_completa_anterior_1 = self.cleaned_data.get("direccion_preview_anterior_1")
        instance.direccion_completa_anterior_2 = self.cleaned_data.get("direccion_preview_anterior_2")

        if commit:
            instance.save()
        return instance


class DatosFamiliaresForm(BaseHelperMixin, forms.ModelForm):
    """
    Formulario asociado al modelo DatosFamiliares.

    Este formulario captura información detallada del entorno familiar del recluta, incluyendo:
    - Datos del cónyuge (identificación, profesión, celular, dirección)
    - Datos del padre y la madre (estado vital, contacto, profesión, dirección)
    - Dirección estructurada para cada persona, con vista previa en campo oculto

    Además:
    - Integra `crispy-forms` para una visualización más ordenada con `Fieldset` y `Row`.
    - Utiliza campos ocultos (`direccion_preview_*`) para mostrar dinámicamente las direcciones generadas.
    - Incluye vistas parciales para agregar hijos y hermanos mediante `include` en plantillas HTML.
    - Sobrescribe el método `save()` para almacenar las versiones formateadas de las direcciones en el modelo.

    Los datos capturados en este formulario permiten una caracterización completa del núcleo familiar del aspirante.
    """

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

        """
        Inicializa el formulario `DatosFamiliaresForm`, configurando el helper de crispy-forms
        para personalizar el renderizado del formulario.

        - Desactiva el tag <form> (form_tag=False) para permitir inclusión en formularios compuestos.
        - Si se trata de una instancia existente (`self.instance.pk`), inicializa los campos ocultos 
          que contienen vistas previas de direcciones para el cónyuge, el padre, la madre y un hermano,
          a partir de los valores calculados y almacenados en el modelo.
        """

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

        """
        Guarda la instancia del formulario `DatosFamiliaresForm`, actualizando los campos de
        dirección formateada del cónyuge, padre, madre y hermanos con la información ingresada 
        desde los campos ocultos (`direccion_preview_*`).

        Si `commit=True`, persiste inmediatamente los cambios en la base de datos. 
        De lo contrario, retorna la instancia sin guardar para posterior manipulación.
        """
              
        instance = super().save(commit=False)
        instance.direccion_formateada_conyugue = self.cleaned_data.get("direccion_preview_conyugue")
        instance.direccion_formateada_padre = self.cleaned_data.get("direccion_preview_padre")
        instance.direccion_formateada_madre = self.cleaned_data.get("direccion_preview_madre")
        instance.direccion_formateada_hermano = self.cleaned_data.get("direccion_preview_hermano")

        if commit:
            instance.save()
        return instance


class HijoForm(forms.ModelForm):

    """
    Formulario para la gestión de datos de un hijo (nombre, edad, identificación) 
    asociado al modelo `Hijo`.

    Este formulario personaliza la presentación con `crispy-forms`, utilizando un 
    diseño basado en filas (`Row`) y columnas (`Column`) para mejorar la usabilidad.

    También incluye campos ocultos necesarios para la integración con un `formset`
    (el campo `id` y el campo `DELETE`).
    """

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
    
    """
    Formulario asociado al modelo `Hermano`, utilizado para capturar la información
    de hermanos del recluta, incluyendo datos personales, ocupación y dirección estructurada.

    El formulario está personalizado con `crispy-forms` para organizar los campos en filas
    y columnas, con soporte para edición y eliminación dentro de un `formset`. También
    incluye un campo oculto para almacenar la dirección formateada.
    """


    
    class Meta:
        model = Hermano
        fields = [
            "primer_apellido_hermano", "segundo_apellido_hermano", "primer_nombre_hermano", "segundo_nombre_hermano",
            "identificacion_hermano", "ocupacion_hermano", "celular_hermano",
            "tipo_via_hermano", "numero_principal_hermano", "letra_principal_hermano",
            "bis_hermano", "letra_bis_hermano", "cuadrante_hermano",
            "numero_secundario_hermano", "letra_secundaria_hermano", "cuadrante_dos_hermano",
            "nro_hermano", "complemento_hermano", "direccion_formateada_hermano"
        ]
        widgets = {
            "direccion_formateada_hermano": HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        """
        Inicializa el formulario, configurando los estilos visuales y el layout
        de los campos. Marca el campo de dirección formateada como no requerido.
        """
        super().__init__(*args, **kwargs)
        self.fields['direccion_formateada_hermano'].required = False
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
            
            Field("id", type="hidden"),
            Field("DELETE", type="hidden"),
            Field("direccion_formateada_hermano", type="hidden"),
        )

        self.helper.render_hidden_fields   = True
        self.helper.render_unmentioned_fields = False

    def save(self, commit=True):

        """
        Guarda la instancia del modelo `Hermano`, asegurándose de que la dirección formateada
        capturada desde el campo oculto se asigne correctamente al campo correspondiente del modelo.
        """
        
        instance = super().save(commit=False)
        instance.direccion_formateada_hermano = self.cleaned_data.get("direccion_formateada_hermano")
        if commit:
            instance.save()
        return instance


HermanoFormSet = inlineformset_factory(
    parent_model=DatosFamiliares,      # quién es el “padre”
    model=Hermano,                        # modelo hijo
    form=HermanoForm,                     # el form que ya tenías
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

    """
    Formulario para capturar hasta tres referencias personales del recluta, incluyendo su nombre,
    ocupación, empresa, ciudad, teléfono y una dirección completa construida a partir de múltiples 
    campos (tipo de vía, número, letras, complementos, etc.).

    Utiliza `crispy-forms` para organizar el formulario en tres secciones claramente separadas mediante
    `Fieldset`, y añade un campo oculto para previsualizar la dirección construida de cada referencia.
    El método `save()` guarda esta dirección en campos formateados del modelo `ReferenciasPersonales`.

    Este formulario no incluye la etiqueta `<form>` (`form_tag = False`) porque se renderiza dentro de
    un formulario principal.
    """

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

    """
    Formulario para registrar información de hasta dos personas relacionadas con el recluta
    que trabajan en el sector defensa. Se capturan sus datos personales, cargos, entidad de
    pertenencia, unidad militar y dirección detallada.

    Cada dirección se construye a partir de múltiples campos individuales y se presenta como
    una previsualización en el formulario. Los campos `direccion_preview_sd_1` y
    `direccion_preview_sd_2` son ocultos y almacenan la dirección formateada generada.

    Se utiliza `crispy-forms` para estructurar el formulario visualmente mediante `Fieldset`
    y `Row`, permitiendo una disposición clara de los campos. El método `save()` guarda las
    direcciones formateadas en el modelo `SectorDefensa`.

    La clase hereda de `BaseHelperMixin` para mantener la consistencia en el diseño con otros formularios.
    """

    direccion_preview_sd_1 = forms.CharField(required=False, widget=forms.HiddenInput())
    direccion_preview_sd_2 = forms.CharField(required=False, widget=forms.HiddenInput())
    class Meta:
        model = SectorDefensa
        fields = [

# Referencia 1
    "nombresyapellidos_sd_1", "cargo_sd_1","entidad_sd_1","unidad_militar_sd_1", "celular_sd_1", "tipo_via_sd_1",
    "numero_principal_sd_1","letra_principal_sd_1","bis_sd_1","letra_bis_sd_1", "cuadrante_sd_1", "numero_secundario_sd_1", 
    "letra_secundaria_sd_1","cuadrante_dos_sd_1","nro_sd_1", "complemento_sd_1",

# Referencia 2
    "nombresyapellidos_sd_2", "cargo_sd_2","entidad_sd_2","unidad_militar_sd_2", "celular_sd_2", "tipo_via_sd_2",
    "numero_principal_sd_2","letra_principal_sd_2","bis_sd_2","letra_bis_sd_2", "cuadrante_sd_2", "numero_secundario_sd_2", 
    "letra_secundaria_sd_2","cuadrante_dos_sd_2","nro_sd_2", "complemento_sd_2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        if self.instance.pk:
            self.fields["direccion_preview_sd_1"].initial = self.instance.direccion_preview_sd_1
            self.fields["direccion_preview_sd_2"].initial = self.instance.direccion_preview_sd_2

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

    """
    Formulario para capturar información adicional del aspirante, incluyendo viajes internacionales
    y datos de recomendantes relacionados con la postulación.

    Secciones:
    - **Viajes al exterior**: Permite registrar hasta tres viajes internacionales, con fecha, país,
      motivo y tiempo de permanencia.
    - **Datos del recomendante**: Recoge información personal del recomendante, su relación con el
      aspirante, su lugar de trabajo (si aplica en Indumil), su dirección completa (dividida en campos),
      y dos contactos adicionales dentro de la organización.

    Características destacadas:
    - Campo oculto `direccion_preview_recomendante` que almacena una dirección construida a partir
      de los fragmentos ingresados manualmente, mostrado en una vista previa interactiva.
    - La dirección formateada se guarda en el campo `direccion_formateada_recomendante` del modelo.
    - Usa `crispy-forms` para una disposición clara, con secciones diferenciadas visualmente mediante HTML.

    Este formulario complementa el perfil del aspirante con información útil para el proceso
    de evaluación de idoneidad y referencias laborales.
    """

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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not getattr(settings, 'IS_E2E_TEST', False):
            print("✅ CAPTCHA INCLUIDO")
            self.fields['captcha'] = ReCaptchaField(widget=ReCaptchaV2Checkbox)
        else:
            print("❌ CAPTCHA EXCLUIDO")