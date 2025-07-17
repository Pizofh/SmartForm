from rest_framework import viewsets
from .models import (PersonalData, FamilyData, Child, Sibling, AcademicInformation,
                     AssetsIncomeAEP, LegalSituation)
from .serializers import (PersonalDataSerializer, FamilyDataSerializer,
                          ChildSerializer, SiblingSerializer, AcademicInformationSerializer,
                          AssetsIncomeAEPSerializer, LegalSituationSerializer)
from rest_framework.permissions import IsAuthenticated


class PersonalDataViewSet(viewsets.ModelViewSet):
    """ API for the main model Recruit (Personal Data). """
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataSerializer
    permission_classes = [IsAuthenticated]


class FamilyDataViewSet(viewsets.ModelViewSet):
    """ API for the recruit's family data. """
    queryset = FamilyData.objects.all()
    serializer_class = FamilyDataSerializer
    permission_classes = [IsAuthenticated]


class ChildViewSet(viewsets.ModelViewSet):
    """ API for the recruit's children. """
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]


class SiblingViewSet(viewsets.ModelViewSet):
    """ API for the recruit's siblings. """
    queryset = Sibling.objects.all()
    serializer_class = SiblingSerializer
    permission_classes = [IsAuthenticated]


class AcademicInformationViewSet(viewsets.ModelViewSet):
    """ API for the recruit's academic information. """
    queryset = AcademicInformation.objects.all()
    serializer_class = AcademicInformationSerializer
    permission_classes = [IsAuthenticated]


class AssetsIncomeAEPViewSet(viewsets.ModelViewSet):
    """ API for the recruit's assets and economic information. """
    queryset = AssetsIncomeAEP.objects.all()
    serializer_class = AssetsIncomeAEPSerializer
    permission_classes = [IsAuthenticated]


class LegalSituationViewSet(viewsets.ModelViewSet):
    """ API for the recruit's legal or disciplinary background. """
    queryset = LegalSituation.objects.all()
    serializer_class = LegalSituationSerializer
    permission_classes = [IsAuthenticated]




class AssetsIncomeAEPViewSet(viewsets.ModelViewSet):
    """ API para los datos patrimoniales y económicos del recluta. """
    queryset = AssetsIncomeAEP.objects.all()
    serializer_class = AssetsIncomeAEPSerializer
    permission_classes = [IsAuthenticated]

class LegalSituationViewSet(viewsets.ModelViewSet):
    """ API para los antecedentes judiciales o disciplinarios del recluta. """
    queryset = LegalSituation.objects.all()
    serializer_class = LegalSituationSerializer
    permission_classes = [IsAuthenticated]

