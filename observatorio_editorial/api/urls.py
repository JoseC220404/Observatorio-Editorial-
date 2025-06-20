# Configuración de URLs para la API del Observatorio Editorial

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CampoDeConocimientoViewSet, CategoriaViewSet, CoberturaViewSet,
    CodigoPostalViewSet, CondicionDeLaLicenciaViewSet, CorrespondeAViewSet, AuditoriaViewSet
)

# Crear un router y registrar nuestros viewsets
router = DefaultRouter()
router.register(r'campos', CampoDeConocimientoViewSet, basename='campo')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'coberturas', CoberturaViewSet, basename='cobertura')
router.register(r'codigos-postales', CodigoPostalViewSet, basename='codigo-postal')
router.register(r'condiciones-licencia', CondicionDeLaLicenciaViewSet, basename='condicion-licencia')
router.register(r'corresponde-a', CorrespondeAViewSet, basename='corresponde-a')
router.register(r'auditoria', AuditoriaViewSet, basename='auditoria')

# Las URLs de la API son determinadas automáticamente por el router
urlpatterns = [
    path('', include(router.urls)),
]