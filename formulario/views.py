from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.db import transaction
from .forms import (
    PersonalDataForm, DatosFamiliaresForm, InformacionAcademicaForm,
    ReferenciasPersonalesForm, BienesRentasAEPForm, SituacionJuridicaForm,
     ConfirmacionForm, HijoFormSet, HermanoFormSet
)
from .models import Hijo, Hermano
from .utils import generar_documentos


class PersonalDataTabsView(TemplateView):
    template_name = "formulario/formulario_tabs.html"

    def get(self, request):
        context = {
            "f_PersonalData": PersonalDataForm(prefix="PersonalData"),
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
        f_PersonalData = PersonalDataForm(request.POST, request.FILES, prefix="PersonalData")
        f_DatosFamiliares = DatosFamiliaresForm(request.POST, prefix="DatosFamiliares")
        fs_hijos = HijoFormSet(request.POST or None, prefix="hijos")
        fs_hermanos = HermanoFormSet(request.POST or None, prefix="hermanos")
        f_informacion_academica = InformacionAcademicaForm(request.POST, prefix="InformacionAcademica")
        f_ReferenciasPersonales = ReferenciasPersonalesForm(request.POST, prefix="ReferenciasPersonales")
        f_BienesRentasAEP = BienesRentasAEPForm(request.POST, prefix="BienesRentasAEP")
        f_SituacionJuridica = SituacionJuridicaForm(request.POST, prefix="SituacionJuridica")
        f_confirm = ConfirmacionForm(request.POST, prefix="confirm")

        if all([
            f_PersonalData.is_valid(),
            f_DatosFamiliares.is_valid(),
            fs_hijos.is_valid(),
            fs_hermanos.is_valid(),
            f_informacion_academica.is_valid(),
            f_ReferenciasPersonales.is_valid(),
            f_BienesRentasAEP.is_valid(),
            f_SituacionJuridica.is_valid(),
            f_confirm.is_valid(),
        ]):
            PersonalData = f_PersonalData.save()

            datos_familiares = f_DatosFamiliares.save(commit=False)
            datos_familiares.PersonalData = PersonalData
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
                obj.PersonalData = PersonalData
                form.instance = obj
                obj.save()

            generar_documentos(PersonalData)
            return redirect("formulario_exito")

        context = {
            "f_PersonalData": f_PersonalData,
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
