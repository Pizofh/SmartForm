from rest_framework import serializers
from .models import (
    Recluta, DireccionesAnteriores, DatosFamiliares, Hijo, Hermano,
    InformacionAcademica, ReferenciasPersonales, SectorDefensa,
    BienesRentasAEP, SituacionJuridica, OtrosDatos, DocumentoGenerado
)

class HijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hijo
        fields = '__all__'

class HermanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hermano
        fields = '__all__'

class DatosFamiliaresSerializer(serializers.ModelSerializer):
    hijos = HijoSerializer(many=True, read_only=True)
    hermanos = HermanoSerializer(many=True, read_only=True)

    class Meta:
        model = DatosFamiliares
        fields = '__all__'

class DireccionesAnterioresSerializer(serializers.ModelSerializer):
    class Meta:
        model = DireccionesAnteriores
        fields = '__all__'

class InformacionAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionAcademica
        fields = '__all__'

class ReferenciasPersonalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenciasPersonales
        fields = '__all__'

class SectorDefensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorDefensa
        fields = '__all__'

class BienesRentasAEPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BienesRentasAEP
        fields = '__all__'

class SituacionJuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacionJuridica
        fields = '__all__'

class OtrosDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtrosDatos
        fields = '__all__'

class DocumentoGeneradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoGenerado
        fields = '__all__'

class ReclutaSerializer(serializers.ModelSerializer):
    datosfamiliares = DatosFamiliaresSerializer(read_only=True)
    direcciones_anteriores = DireccionesAnterioresSerializer(many=True, read_only=True)
    informaciones_academicas = InformacionAcademicaSerializer(many=True, read_only=True)
    referencias_personales = ReferenciasPersonalesSerializer(many=True, read_only=True)
    sector_defensa = SectorDefensaSerializer(many=True, read_only=True)
    bienes_rentas = BienesRentasAEPSerializer(many=True, read_only=True)
    situaciones_juridicas = SituacionJuridicaSerializer(many=True, read_only=True)
    otrosdatos_set = OtrosDatosSerializer(many=True, read_only=True)
    documentogenerado_set = DocumentoGeneradoSerializer(many=True, read_only=True)

    class Meta:
        model = Recluta
        fields = '__all__'
