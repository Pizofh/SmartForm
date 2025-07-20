from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.db import transaction
from .forms import (
    FamilyDataForm, AcademicInformationForm,
   AssetsIncomeAEPForm, LegalSituationForm,
     ConfirmacionForm, ChildFormSet, SiblingFormSet,PersonalDataForm

     
)
from .models import Child, Sibling
from .utils import generar_documentos


class PersonalDataTabsView(TemplateView):
    template_name = "form/form_tabs.html"

    def get(self, request):
        context = {
            "f_PersonalData": PersonalDataForm(prefix="PersonalData"),
            "f_FamilyData": FamilyDataForm(prefix="FamilyData"),
            "fs_Child": ChildFormSet(queryset=Child.objects.none(), prefix="Child"),
            "fs_Sibling": SiblingFormSet(queryset=Sibling.objects.none(), prefix="Sibling"),
            "f_AcademicInformation": AcademicInformationForm(prefix="AcademicInformation"),
            "f_AssetsIncomeAEP": AssetsIncomeAEPForm(prefix="AssetsIncomeAEP"),
            "f_LegalSituation": LegalSituationForm(prefix="LegalSituation"),
            "f_confirm": ConfirmacionForm(prefix="confirm"),
        }
        return render(request, self.template_name, context)

    @transaction.atomic
    def post(self, request):
        f_PersonalData = PersonalDataForm(request.POST, request.FILES, prefix="PersonalData")
        f_FamilyData = FamilyDataForm(request.POST, prefix="FamilyData")
        fs_Child = ChildFormSet(request.POST or None, prefix="Child")
        fs_Sibling = SiblingFormSet(request.POST or None, prefix="Sibling")
        f_AcademicInformation = AcademicInformationForm(request.POST, prefix="AcademicInformation")
        f_AssetsIncomeAEP = AssetsIncomeAEPForm(request.POST, prefix="AssetsIncomeAEP")
        f_LegalSituation = LegalSituationForm(request.POST, prefix="LegalSituation")
        f_confirm = ConfirmacionForm(request.POST, prefix="confirm")

        if all([
            f_PersonalData.is_valid(),
            f_FamilyData.is_valid(),
            fs_Child.is_valid(),
            fs_Sibling.is_valid(),
            f_AcademicInformation.is_valid(),
            f_AssetsIncomeAEP.is_valid(),
            f_LegalSituation.is_valid(),
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
                    address = Sibling_form.cleaned_data.get("sibling_built_address")
                    Sibling = Sibling_form.save(commit=False)
                    Sibling.sibling_built_address = address
                    Sibling.FamilyData = FamilyData
                    Sibling.save()

            for form in [
                f_AcademicInformation,
                f_AssetsIncomeAEP,
                f_LegalSituation,
            ]:
                obj = form.save(commit=False)
                obj.PersonalData = PersonalData
                form.instance = obj
                obj.save()

            generar_documentos(PersonalData)
            return redirect("form_success")

        context = {
            "f_PersonalData": f_PersonalData,
            "f_FamilyData": f_FamilyData,
            "fs_Child": fs_Child,
            "fs_Sibling": fs_Sibling,
            "f_AcademicInformation": f_AcademicInformation,
            "f_AssetsIncomeAEP": f_AssetsIncomeAEP,
            "f_LegalSituation": f_LegalSituation,
            "f_confirm": f_confirm,
        }

        return render(request, self.template_name, context)
