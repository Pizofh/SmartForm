from rest_framework import viewsets
from .models import (Recluta,DatosFamiliares, DireccionesAnteriores,Hijo,Hermano,InformacionAcademica,
                     ReferenciasPersonales,SectorDefensa,BienesRentasAEP,SituacionJuridica,OtrosDatos)
from .serializers import (ReclutaSerializer,DatosFamiliaresSerializer,DireccionesAnterioresSerializer,
                          HijoSerializer,HermanoSerializer,InformacionAcademicaSerializer,ReferenciasPersonalesSerializer,
                          SectorDefensaSerializer,BienesRentasAEPSerializer,SituacionJuridicaSerializer,OtrosDatosSerializer)
from rest_framework.permissions import IsAuthenticated


class ReclutaViewSet(viewsets.ModelViewSet):
    """ API para el modelo principal Recluta. """
    queryset = Recluta.objects.all()
    serializer_class = ReclutaSerializer
    permission_classes = [IsAuthenticated]

class DireccionesAnterioresViewSet(viewsets.ModelViewSet):
    """ API para las direcciones anteriores del recluta. """
    queryset = DireccionesAnteriores.objects.all()
    serializer_class = DireccionesAnterioresSerializer
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

class SectorDefensaViewSet(viewsets.ModelViewSet):
    """ API para contactos del sector defensa relacionados con el recluta. """
    queryset = SectorDefensa.objects.all()
    serializer_class = SectorDefensaSerializer
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

class OtrosDatosViewSet(viewsets.ModelViewSet):
    """ API para información adicional del recluta, como viajes y recomendantes. """
    queryset = OtrosDatos.objects.all()
    serializer_class = OtrosDatosSerializer
    permission_classes = [IsAuthenticated]