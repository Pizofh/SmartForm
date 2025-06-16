from rest_framework import viewsets
from .models import (Recluta,DatosFamiliares, DireccionesAnteriores,Hijo,Hermano,InformacionAcademica,
                     ReferenciasPersonales,SectorDefensa,BienesRentasAEP,SituacionJuridica,OtrosDatos)
from .serializers import (ReclutaSerializer,DatosFamiliaresSerializer,DireccionesAnterioresSerializer,
                          HijoSerializer,HermanoSerializer,InformacionAcademicaSerializer,ReferenciasPersonalesSerializer,
                          SectorDefensaSerializer,BienesRentasAEPSerializer,SituacionJuridicaSerializer,OtrosDatosSerializer)
from rest_framework.permissions import IsAuthenticated


class ReclutaViewSet(viewsets.ModelViewSet):
    queryset = Recluta.objects.all()
    serializer_class = ReclutaSerializer
    permission_classes = [IsAuthenticated]

class DireccionesAnterioresViewSet(viewsets.ModelViewSet):
    queryset = DireccionesAnteriores.objects.all()
    serializer_class = DireccionesAnterioresSerializer
    permission_classes = [IsAuthenticated]

class DatosFamiliaresViewSet(viewsets.ModelViewSet):
    queryset = DatosFamiliares.objects.all()
    serializer_class = DatosFamiliaresSerializer
    permission_classes = [IsAuthenticated]

class HijoViewSet(viewsets.ModelViewSet):
    queryset = Hijo.objects.all()
    serializer_class = HijoSerializer
    permission_classes = [IsAuthenticated]
    
class HermanoViewSet(viewsets.ModelViewSet):
    queryset = Hermano.objects.all()
    serializer_class = HermanoSerializer
    permission_classes = [IsAuthenticated]
    
class InformacionAcademicaViewSet(viewsets.ModelViewSet):
    queryset = InformacionAcademica.objects.all()
    serializer_class = InformacionAcademicaSerializer
    permission_classes = [IsAuthenticated]

class ReferenciasPersonalesViewSet(viewsets.ModelViewSet):
    queryset = ReferenciasPersonales.objects.all()
    serializer_class = ReferenciasPersonalesSerializer
    permission_classes = [IsAuthenticated]

class SectorDefensaViewSet(viewsets.ModelViewSet):
    queryset = SectorDefensa.objects.all()
    serializer_class = SectorDefensaSerializer
    permission_classes = [IsAuthenticated]

class BienesRentasAEPViewSet(viewsets.ModelViewSet):
    queryset = BienesRentasAEP.objects.all()
    serializer_class = BienesRentasAEPSerializer
    permission_classes = [IsAuthenticated]

class SituacionJuridicaViewSet(viewsets.ModelViewSet):
    queryset = SituacionJuridica.objects.all()
    serializer_class = SituacionJuridicaSerializer
    permission_classes = [IsAuthenticated]

class OtrosDatosViewSet(viewsets.ModelViewSet):
    queryset = OtrosDatos.objects.all()
    serializer_class = OtrosDatosSerializer
    permission_classes = [IsAuthenticated]