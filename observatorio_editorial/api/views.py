# Vistas para la API del Observatorio Editorial

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import (
    CampoDeConocimiento, Categoria, Cobertura, 
    CodigoPostal, CondicionDeLaLicencia, CorrespondeA, Auditoria
)
from .serializers import (
    CampoDeConocimientoSerializer, CategoriaSerializer, CoberturaSerializer,
    CodigoPostalSerializer, CondicionDeLaLicenciaSerializer, CorrespondeASerializer, AuditoriaSerializer
)


class CampoDeConocimientoViewSet(viewsets.ViewSet):
    """
    ViewSet para operaciones CRUD en CampoDeConocimiento
    """
    def list(self, request):
        campos = CampoDeConocimiento.objects.all()
        serializer = CampoDeConocimientoSerializer(campos, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        campo = get_object_or_404(CampoDeConocimiento, campo_id=pk)
        serializer = CampoDeConocimientoSerializer(campo)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CampoDeConocimientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        campo = get_object_or_404(CampoDeConocimiento, campo_id=pk)
        serializer = CampoDeConocimientoSerializer(campo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        campo = get_object_or_404(CampoDeConocimiento, campo_id=pk)
        campo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriaViewSet(viewsets.ViewSet):
    """
    ViewSet para operaciones CRUD en Categoria
    """
    def list(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        categoria = get_object_or_404(Categoria, id_categoria=pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        categoria = get_object_or_404(Categoria, id_categoria=pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        categoria = get_object_or_404(Categoria, id_categoria=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CoberturaViewSet(viewsets.ViewSet):
    """
    ViewSet para operaciones CRUD en Cobertura
    """
    def list(self, request):
        coberturas = Cobertura.objects.all()
        serializer = CoberturaSerializer(coberturas, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        cobertura = get_object_or_404(Cobertura, id_cobertura=pk)
        serializer = CoberturaSerializer(cobertura)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CoberturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        cobertura = get_object_or_404(Cobertura, id_cobertura=pk)
        serializer = CoberturaSerializer(cobertura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        cobertura = get_object_or_404(Cobertura, id_cobertura=pk)
        cobertura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CodigoPostalViewSet(viewsets.ViewSet):
    """
    ViewSet para operaciones CRUD en CodigoPostal
    """
    def list(self, request):
        codigos = CodigoPostal.objects.all()
        serializer = CodigoPostalSerializer(codigos, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        codigo = get_object_or_404(CodigoPostal, id_codigo=pk)
        serializer = CodigoPostalSerializer(codigo)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CodigoPostalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        codigo = get_object_or_404(CodigoPostal, id_codigo=pk)
        serializer = CodigoPostalSerializer(codigo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        codigo = get_object_or_404(CodigoPostal, id_codigo=pk)
        codigo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CondicionDeLaLicenciaViewSet(viewsets.ViewSet):
    """
    ViewSet para operaciones CRUD en CondicionDeLaLicencia
    """
    def list(self, request):
        condiciones = CondicionDeLaLicencia.objects.all()
        serializer = CondicionDeLaLicenciaSerializer(condiciones, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        condicion = get_object_or_404(CondicionDeLaLicencia, id_condicion_de_la_licencia=pk)
        serializer = CondicionDeLaLicenciaSerializer(condicion)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CondicionDeLaLicenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        condicion = get_object_or_404(CondicionDeLaLicencia, id_condicion_de_la_licencia=pk)
        serializer = CondicionDeLaLicenciaSerializer(condicion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        condicion = get_object_or_404(CondicionDeLaLicencia, id_condicion_de_la_licencia=pk)
        condicion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CorrespondeAViewSet(viewsets.ViewSet):
    """
    ViewSet para operaciones CRUD en CorrespondeA
    """
    def list(self, request):
        correspondencias = CorrespondeA.objects.all()
        serializer = CorrespondeASerializer(correspondencias, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        correspondencia = get_object_or_404(CorrespondeA, materias__idem=pk)
        serializer = CorrespondeASerializer(correspondencia)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CorrespondeASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        correspondencia = get_object_or_404(CorrespondeA, materias__idem=pk)
        serializer = CorrespondeASerializer(correspondencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        correspondencia = get_object_or_404(CorrespondeA, materias__idem=pk)
        correspondencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuditoriaViewSet(viewsets.ViewSet):
    """
    ViewSet para operaciones CRUD en Auditoria
    """
    def list(self, request):
        auditorias = Auditoria.objects.all().order_by('-fecha_hora')
        serializer = AuditoriaSerializer(auditorias, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        auditoria = get_object_or_404(Auditoria, id_auditoria=pk)
        serializer = AuditoriaSerializer(auditoria)
        return Response(serializer.data)
    
    # No implementamos create, update y destroy para Auditoria
    # ya que estos registros se generan automáticamente mediante triggers