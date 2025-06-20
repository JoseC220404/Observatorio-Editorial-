# Configuración del panel de administración para la API del Observatorio Editorial

from django.contrib import admin
from .models import (
    CampoDeConocimiento, Categoria, Cobertura, 
    CodigoPostal, CondicionDeLaLicencia, CorrespondeA, Auditoria
)

# Registrar los modelos en el panel de administración
@admin.register(CampoDeConocimiento)
class CampoDeConocimientoAdmin(admin.ModelAdmin):
    list_display = ('campo_id', 'nombre_del_campo')
    search_fields = ('nombre_del_campo',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre')
    search_fields = ('nombre',)

@admin.register(Cobertura)
class CoberturaAdmin(admin.ModelAdmin):
    list_display = ('id_cobertura', 'cobertura')
    search_fields = ('cobertura',)

@admin.register(CodigoPostal)
class CodigoPostalAdmin(admin.ModelAdmin):
    list_display = ('id_codigo',)
    search_fields = ('id_codigo',)

@admin.register(CondicionDeLaLicencia)
class CondicionDeLaLicenciaAdmin(admin.ModelAdmin):
    list_display = ('id_condicion_de_la_licencia', 'condicion_de_la_licencia')
    search_fields = ('condicion_de_la_licencia',)

@admin.register(CorrespondeA)
class CorrespondeAAdmin(admin.ModelAdmin):
    list_display = ('materias__idem', 'ejetem__ideje')
    search_fields = ('materias__idem', 'ejetem__ideje')

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('id_auditoria', 'tabla_afectada', 'operacion', 'usuario', 'fecha_hora')
    list_filter = ('tabla_afectada', 'operacion', 'usuario', 'fecha_hora')
    search_fields = ('tabla_afectada', 'operacion', 'usuario')
    readonly_fields = ('id_auditoria', 'tabla_afectada', 'operacion', 'usuario', 'fecha_hora', 'datos_antiguos', 'datos_nuevos')