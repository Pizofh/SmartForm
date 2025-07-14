from rest_framework import serializers
from .models import (
    Recluta,  DatosFamiliares, Hijo, Hermano,
    InformacionAcademica, ReferenciasPersonales, 
    BienesRentasAEP, SituacionJuridica, DocumentoGenerado
)

"""
serializers.py

Este módulo define los serializadores para todos los modelos relacionados con el formulario
de reclutamiento. Los serializadores permiten transformar instancias de modelos en formatos
como JSON, y viceversa, facilitando la comunicación con APIs REST.

Cada clase de serializador utiliza `ModelSerializer` de Django REST Framework, lo cual
automatiza el mapeo entre los campos del modelo y su representación serializada.

Serializadores definidos:

- HijoSerializer / HermanoSerializer:
    Serializan las relaciones familiares del recluta.

- DatosFamiliaresSerializer:
    Incluye hijos y hermanos como relaciones anidadas de solo lectura.



- BienesRentasAEPSerializer:
    Serializa la información patrimonial y económica del recluta.

- SituacionJuridicaSerializer:
    Serializa información jurídica del aspirante.



- DocumentoGeneradoSerializer:
    Serializa los documentos generados automáticamente por el sistema.

- ReclutaSerializer:
    Serializador principal que incluye relaciones anidadas de solo lectura con todos
    los modelos relacionados. Útil para obtener un perfil completo del recluta en una sola petición.
"""

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



class InformacionAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionAcademica
        fields = '__all__'

class ReferenciasPersonalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenciasPersonales
        fields = '__all__'



class BienesRentasAEPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BienesRentasAEP
        fields = '__all__'

class SituacionJuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacionJuridica
        fields = '__all__'



class DocumentoGeneradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoGenerado
        fields = '__all__'

class ReclutaSerializer(serializers.ModelSerializer):
    datosfamiliares = DatosFamiliaresSerializer(read_only=True)
    informaciones_academicas = InformacionAcademicaSerializer(many=True, read_only=True)
    referencias_personales = ReferenciasPersonalesSerializer(many=True, read_only=True)
    bienes_rentas = BienesRentasAEPSerializer(many=True, read_only=True)
    situaciones_juridicas = SituacionJuridicaSerializer(many=True, read_only=True)
    documentogenerado_set = DocumentoGeneradoSerializer(many=True, read_only=True)

    class Meta:
        model = Recluta
        fields = '__all__'
