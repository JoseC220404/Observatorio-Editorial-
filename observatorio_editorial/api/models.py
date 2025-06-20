# Modelos para la aplicación API del Observatorio Editorial

from django.db import models
from django.utils import timezone


class CampoDeConocimiento(models.Model):
    campo_id = models.AutoField(primary_key=True)
    nombre_del_campo = models.CharField(max_length=100, null=False)
    
    class Meta:
        db_table = 'Campo_de_conocimiento'
        verbose_name = 'Campo de Conocimiento'
        verbose_name_plural = 'Campos de Conocimiento'
    
    def __str__(self):
        return self.nombre_del_campo


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, null=False)
    
    class Meta:
        db_table = 'Categoria'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre


class Cobertura(models.Model):
    id_cobertura = models.AutoField(primary_key=True)
    cobertura = models.CharField(max_length=250, null=False)
    
    class Meta:
        db_table = 'Cobertura'
        verbose_name = 'Cobertura'
        verbose_name_plural = 'Coberturas'
    
    def __str__(self):
        return self.cobertura


class CodigoPostal(models.Model):
    id_codigo = models.CharField(max_length=250, primary_key=True)
    
    class Meta:
        db_table = 'Codigo_Postal'
        verbose_name = 'Código Postal'
        verbose_name_plural = 'Códigos Postales'
    
    def __str__(self):
        return self.id_codigo


class CondicionDeLaLicencia(models.Model):
    id_condicion_de_la_licencia = models.AutoField(primary_key=True)
    condicion_de_la_licencia = models.CharField(max_length=250, null=False)
    
    class Meta:
        db_table = 'Condicion_de_la_licencia'
        verbose_name = 'Condición de la Licencia'
        verbose_name_plural = 'Condiciones de la Licencia'
    
    def __str__(self):
        return self.condicion_de_la_licencia


class CorrespondeA(models.Model):
    materias__idem = models.CharField(max_length=25, primary_key=True)
    ejetem__ideje = models.CharField(max_length=25)
    
    class Meta:
        db_table = 'Corresponde_A'
        verbose_name = 'Corresponde A'
        verbose_name_plural = 'Corresponde A'
        unique_together = ('materias__idem', 'ejetem__ideje')
    
    def __str__(self):
        return f"{self.materias__idem} - {self.ejetem__ideje}"


class Auditoria(models.Model):
    id_auditoria = models.AutoField(primary_key=True)
    tabla_afectada = models.CharField(max_length=100, null=False)
    operacion = models.CharField(max_length=10, null=False)
    usuario = models.CharField(max_length=100, null=False)
    fecha_hora = models.DateTimeField(default=timezone.now)
    datos_antiguos = models.JSONField(null=True, blank=True)
    datos_nuevos = models.JSONField(null=True, blank=True)
    
    class Meta:
        db_table = 'auditoria'
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'
    
    def __str__(self):
        return f"{self.id_auditoria} - {self.tabla_afectada} - {self.operacion}"