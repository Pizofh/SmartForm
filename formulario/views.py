from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.db import transaction
from .forms import (
    ReclutaForm, DatosFamiliaresForm, InformacionAcademicaForm,
    ReferenciasPersonalesForm, BienesRentasAEPForm, SituacionJuridicaForm,
     ConfirmacionForm, HijoFormSet, HermanoFormSet
)
from .models import Hijo, Hermano
from .utils import generar_documentos

"""
views.py

Este módulo define la vista principal `ReclutaTabsView` para el formulario inteligente de reclutamiento.

La vista está basada en `TemplateView` y se encarga de:

1. **GET request**:
   - Renderiza el formulario tabulado, agrupando múltiples secciones del proceso de reclutamiento.
   - Inicializa instancias de los formularios que capturan los datos del aspirante, incluyendo:
     - Información personal (`ReclutaForm`)
     - Datos familiares (`DatosFamiliaresForm`)
     - Hijos y hermanos (`HijoFormSet`, `HermanoFormSet`)
     - Educación y referencias
     - Bienes y rentas (`BienesRentasAEPForm`)
     - Situación jurídica
     - Confirmación (reCAPTCHA)

2. **POST request**:
   - Valida todos los formularios simultáneamente.
   - Si todos los formularios son válidos:
     - Guarda el objeto `Recluta`.
     - Asocia y guarda las entidades relacionadas (familiares, bienes, etc.).
     - Usa `@transaction.atomic` para asegurar consistencia y evitar registros parciales.
     - Genera automáticamente los documentos usando `generar_documentos(recluta)`.
     - Redirige a la página de éxito.
   - Si hay errores, vuelve a renderizar el formulario con los errores mostrados.

Notas:
- El campo `prefix` se utiliza en cada formulario para mantener un namespace y evitar colisiones de nombres en el HTML.
- Los formsets de hijos y hermanos permiten el manejo dinámico de múltiples instancias relacionadas.
- `Recluta` es la entidad principal y todas las demás dependen de esta.

Esta vista representa el punto de entrada principal del sistema de recolección de datos y es crucial para asegurar una experiencia de usuario fluida, validación de datos integral y persistencia robusta.
"""

class ReclutaTabsView(TemplateView):
    template_name = "formulario/formulario_tabs.html"

    def get(self, request):
        context = {
            "f_recluta": ReclutaForm(prefix="recluta"),
            "f_DatosFamiliares": DatosFamiliaresForm(prefix="DatosFamiliares"),
            "fs_hijos": HijoFormSet(queryset=Hijo.objects.none(), prefix="hijos"),
            "fs_hermanos": HermanoFormSet(queryset=Hermano.objects.none(), prefix="hermanos"),
            "f_informacion_academica": InformacionAcademicaForm(prefix="InformacionAcademica"),
            "f_ReferenciasPersonales": ReferenciasPersonalesForm(prefix="ReferenciasPersonales"),
            "f_BienesRentasAEP": BienesRentasAEPForm(prefix="BienesRentasAEP"),
            "f_SituacionJuridica": SituacionJuridicaForm(prefix="SituacionJuridica"),
            "f_confirm": ConfirmacionForm(prefix="confirm"),
        }
        return render(request, self.template_name, context)

    @transaction.atomic
    def post(self, request):
        f_recluta = ReclutaForm(request.POST, request.FILES, prefix="recluta")
        f_DatosFamiliares = DatosFamiliaresForm(request.POST, prefix="DatosFamiliares")
        fs_hijos = HijoFormSet(request.POST or None, prefix="hijos")
        fs_hermanos = HermanoFormSet(request.POST or None, prefix="hermanos")
        f_informacion_academica = InformacionAcademicaForm(request.POST, prefix="InformacionAcademica")
        f_ReferenciasPersonales = ReferenciasPersonalesForm(request.POST, prefix="ReferenciasPersonales")
        f_BienesRentasAEP = BienesRentasAEPForm(request.POST, prefix="BienesRentasAEP")
        f_SituacionJuridica = SituacionJuridicaForm(request.POST, prefix="SituacionJuridica")
        f_confirm = ConfirmacionForm(request.POST, prefix="confirm")

        if all([
            f_recluta.is_valid(),
            f_DatosFamiliares.is_valid(),
            fs_hijos.is_valid(),
            fs_hermanos.is_valid(),
            f_informacion_academica.is_valid(),
            f_ReferenciasPersonales.is_valid(),
            f_BienesRentasAEP.is_valid(),
            f_SituacionJuridica.is_valid(),
            f_confirm.is_valid(),
        ]):
            recluta = f_recluta.save()

            datos_familiares = f_DatosFamiliares.save(commit=False)
            datos_familiares.recluta = recluta
            datos_familiares.save()

            for hijo_form in fs_hijos:
                if hijo_form.cleaned_data and not hijo_form.cleaned_data.get("DELETE", False):
                    hijo = hijo_form.save(commit=False)
                    hijo.datos_familiares = datos_familiares
                    hijo.save()

            for hermano_form in fs_hermanos:
                if hermano_form.cleaned_data and not hermano_form.cleaned_data.get("DELETE", False):
                    direccion = hermano_form.cleaned_data.get("direccion_formateada_hermano")
                    hermano = hermano_form.save(commit=False)
                    hermano.direccion_formateada_hermano = direccion
                    hermano.datos_familiares = datos_familiares
                    hermano.save()

            for form in [
                f_informacion_academica,
                f_ReferenciasPersonales,
                f_BienesRentasAEP,
                f_SituacionJuridica,
            ]:
                obj = form.save(commit=False)
                obj.recluta = recluta
                form.instance = obj
                obj.save()

            generar_documentos(recluta)
            return redirect("formulario_exito")

        context = {
            "f_recluta": f_recluta,
            "f_DatosFamiliares": f_DatosFamiliares,
            "fs_hijos": fs_hijos,
            "fs_hermanos": fs_hermanos,
            "f_informacion_academica": f_informacion_academica,
            "f_ReferenciasPersonales": f_ReferenciasPersonales,
            "f_BienesRentasAEP": f_BienesRentasAEP,
            "f_SituacionJuridica": f_SituacionJuridica,
            "f_confirm": f_confirm,
        }

        return render(request, self.template_name, context)
