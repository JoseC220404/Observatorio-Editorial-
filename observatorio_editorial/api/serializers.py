# Serializadores para la API del Observatorio Editorial

from rest_framework import serializers
from .models import (
    CampoDeConocimiento, Categoria, Cobertura, 
    CodigoPostal, CondicionDeLaLicencia, CorrespondeA, Auditoria
)


class CampoDeConocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoDeConocimiento
        fields = ['campo_id', 'nombre_del_campo']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria', 'nombre']


class CoberturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobertura
        fields = ['id_cobertura', 'cobertura']


class CodigoPostalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoPostal
        fields = ['id_codigo']


class CondicionDeLaLicenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicionDeLaLicencia
        fields = ['id_condicion_de_la_licencia', 'condicion_de_la_licencia']


class CorrespondeASerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrespondeA
        fields = ['materias__idem', 'ejetem__ideje']


class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = ['id_auditoria', 'tabla_afectada', 'operacion', 'usuario', 'fecha_hora', 'datos_antiguos', 'datos_nuevos']