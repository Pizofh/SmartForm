from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.db import transaction
from .forms import (
    FamilyDataForm, InformacionAcademicaForm,
   BienesRentasAEPForm, SituacionJuridicaForm,
     ConfirmacionForm, ChildFormSet, SiblingFormSet,PersonalDataForm

     
)
from .models import Child, Sibling
from .utils import generar_documentos


class PersonalDataTabsView(TemplateView):
    template_name = "formulario/formulario_tabs.html"

    def get(self, request):
        context = {
            "f_PersonalData": PersonalDataForm(prefix="PersonalData"),
            "f_FamilyData": FamilyDataForm(prefix="FamilyData"),
            "fs_Child": ChildFormSet(queryset=Child.objects.none(), prefix="Child"),
            "fs_Sibling": SiblingFormSet(queryset=Sibling.objects.none(), prefix="Sibling"),
            "f_informacion_academica": InformacionAcademicaForm(prefix="InformacionAcademica"),
            "f_BienesRentasAEP": BienesRentasAEPForm(prefix="BienesRentasAEP"),
            "f_SituacionJuridica": SituacionJuridicaForm(prefix="SituacionJuridica"),
            "f_confirm": ConfirmacionForm(prefix="confirm"),
        }
        return render(request, self.template_name, context)

    @transaction.atomic
    def post(self, request):
        f_PersonalData = PersonalDataForm(request.POST, request.FILES, prefix="PersonalData")
        f_FamilyData = FamilyDataForm(request.POST, prefix="FamilyData")
        fs_Child = ChildFormSet(request.POST or None, prefix="Child")
        fs_Sibling = SiblingFormSet(request.POST or None, prefix="Sibling")
        f_informacion_academica = InformacionAcademicaForm(request.POST, prefix="InformacionAcademica")
        f_BienesRentasAEP = BienesRentasAEPForm(request.POST, prefix="BienesRentasAEP")
        f_SituacionJuridica = SituacionJuridicaForm(request.POST, prefix="SituacionJuridica")
        f_confirm = ConfirmacionForm(request.POST, prefix="confirm")

        if all([
            f_PersonalData.is_valid(),
            f_FamilyData.is_valid(),
            fs_Child.is_valid(),
            fs_Sibling.is_valid(),
            f_informacion_academica.is_valid(),
            f_BienesRentasAEP.is_valid(),
            f_SituacionJuridica.is_valid(),
            f_confirm.is_valid(),
        ]):
            PersonalData = f_PersonalData.save()

            FamilyData = f_FamilyData.save(commit=False)
            FamilyData.PersonalData = PersonalData
            FamilyData.save()

            for Child_form in fs_Child:
                if Child_form.cleaned_data and not Child_form.cleaned_data.get("DELETE", False):
                    Child = Child_form.save(commit=False)
                    Child.FamilyData = FamilyData
                    Child.save()

            for Sibling_form in fs_Sibling:
                if Sibling_form.cleaned_data and not Sibling_form.cleaned_data.get("DELETE", False):
                    direccion = Sibling_form.cleaned_data.get("direccion_formateada_Sibling")
                    Sibling = Sibling_form.save(commit=False)
                    Sibling.direccion_formateada_Sibling = direccion
                    Sibling.FamilyData = FamilyData
                    Sibling.save()

            for form in [
                f_informacion_academica,
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
            "f_FamilyData": f_FamilyData,
            "fs_Child": fs_Child,
            "fs_Sibling": fs_Sibling,
            "f_informacion_academica": f_informacion_academica,
            "f_BienesRentasAEP": f_BienesRentasAEP,
            "f_SituacionJuridica": f_SituacionJuridica,
            "f_confirm": f_confirm,
        }

        return render(request, self.template_name, context)
