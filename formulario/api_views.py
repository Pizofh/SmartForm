from rest_framework import viewsets
from .models import (PersonalData,FamilyData, Child,Sibling,InformacionAcademica,
                    BienesRentasAEP,SituacionJuridica)
from .serializers import (PersonalDataSerializer,FamilyDataSerializer,
                          ChildSerializer,SiblingSerializer,InformacionAcademicaSerializer
                          ,BienesRentasAEPSerializer,SituacionJuridicaSerializer)
from rest_framework.permissions import IsAuthenticated


class PersonalDataViewSet(viewsets.ModelViewSet):
    """ API para el modelo principal Recluta. """
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataSerializer
    permission_classes = [IsAuthenticated]



class FamilyDataViewSet(viewsets.ModelViewSet):
    """ API para los datos familiares del recluta. """
    queryset = FamilyData.objects.all()
    serializer_class = FamilyDataSerializer
    permission_classes = [IsAuthenticated]

class ChildViewSet(viewsets.ModelViewSet):
    """ API para los Child del recluta. """
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]
    
class SiblingViewSet(viewsets.ModelViewSet):
    """ API para los Sibling del recluta. """
    queryset = Sibling.objects.all()
    serializer_class = SiblingSerializer
    permission_classes = [IsAuthenticated]
    
class InformacionAcademicaViewSet(viewsets.ModelViewSet):
    """ API para la información académica del recluta. """
    queryset = InformacionAcademica.objects.all()
    serializer_class = InformacionAcademicaSerializer
    permission_classes = [IsAuthenticated]





class BienesRentasAEPViewSet(viewsets.ModelViewSet):
    """ API para los datos patrimoniales y económicos del recluta. """
    queryset = BienesRentasAEP.objects.all()
    serializer_class = BienesRentasAEPSerializer
    permission_classes = [IsAuthenticated]

class SituacionJuridicaViewSet(viewsets.ModelViewSet):
    """ API para los antecedentes judiciales o disciplinarios del recluta. """
    queryset = SituacionJuridica.objects.all()
    serializer_class = SituacionJuridicaSerializer
    permission_classes = [IsAuthenticated]

