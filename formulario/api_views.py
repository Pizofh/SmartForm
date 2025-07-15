from rest_framework import viewsets
from .models import (PersonalData,DatosFamiliares, Hijo,Hermano,InformacionAcademica,
                     ReferenciasPersonales,BienesRentasAEP,SituacionJuridica)
from .serializers import (PersonalDataSerializer,DatosFamiliaresSerializer,
                          HijoSerializer,HermanoSerializer,InformacionAcademicaSerializer,ReferenciasPersonalesSerializer
                          ,BienesRentasAEPSerializer,SituacionJuridicaSerializer)
from rest_framework.permissions import IsAuthenticated


class PersonalDataViewSet(viewsets.ModelViewSet):
    """ API para el modelo principal Recluta. """
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataSerializer
    permission_classes = [IsAuthenticated]



class DatosFamiliaresViewSet(viewsets.ModelViewSet):
    """ API para los datos familiares del recluta. """
    queryset = DatosFamiliares.objects.all()
    serializer_class = DatosFamiliaresSerializer
    permission_classes = [IsAuthenticated]

class HijoViewSet(viewsets.ModelViewSet):
    """ API para los hijos del recluta. """
    queryset = Hijo.objects.all()
    serializer_class = HijoSerializer
    permission_classes = [IsAuthenticated]
    
class HermanoViewSet(viewsets.ModelViewSet):
    """ API para los hermanos del recluta. """
    queryset = Hermano.objects.all()
    serializer_class = HermanoSerializer
    permission_classes = [IsAuthenticated]
    
class InformacionAcademicaViewSet(viewsets.ModelViewSet):
    """ API para la información académica del recluta. """
    queryset = InformacionAcademica.objects.all()
    serializer_class = InformacionAcademicaSerializer
    permission_classes = [IsAuthenticated]

class ReferenciasPersonalesViewSet(viewsets.ModelViewSet):
    """ API para las referencias personales del recluta. """
    queryset = ReferenciasPersonales.objects.all()
    serializer_class = ReferenciasPersonalesSerializer
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

