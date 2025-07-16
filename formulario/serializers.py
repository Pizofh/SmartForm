from rest_framework import serializers
from .models import (
    PersonalData,  FamilyData, Child, Sibling,
    InformacionAcademica,
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

- ChildSerializer / SiblingoSerializer:
    Serializan las relaciones familiares del PersonalData.

- FamilyDataSerializer:
    Incluye Child y Sibling como relaciones anidadas de solo lectura.



- BienesRentasAEPSerializer:
    Serializa la información patrimonial y económica del PersonalData

- SituacionJuridicaSerializer:
    Serializa información jurídica del aspirante.



- DocumentoGeneradoSerializer:
    Serializa los documentos generados automáticamente por el sistema.

- PersonalDataSerializer:
    Serializador principal que incluye relaciones anidadas de solo lectura con todos
    los modelos relacionados. Útil para obtener un perfil completo del PersonalData en una sola petición.
"""

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class SiblingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sibling
        fields = '__all__'

class FamilyDataSerializer(serializers.ModelSerializer):
    Child = ChildSerializer(many=True, read_only=True)
    Sibling = SiblingSerializer(many=True, read_only=True)

    class Meta:
        model = FamilyData
        fields = '__all__'



class InformacionAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionAcademica
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

class PersonalDataSerializer(serializers.ModelSerializer):
    FamilyData = FamilyDataSerializer(read_only=True)
    informaciones_academicas = InformacionAcademicaSerializer(many=True, read_only=True)
    bienes_rentas = BienesRentasAEPSerializer(many=True, read_only=True)
    situaciones_juridicas = SituacionJuridicaSerializer(many=True, read_only=True)
    documentogenerado_set = DocumentoGeneradoSerializer(many=True, read_only=True)

    class Meta:
        model = PersonalData
        fields = '__all__'
