# Modelos base para la aplicación del Observatorio Editorial

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import json

from config import DB_CONFIG

# Crear la conexión a la base de datos
db_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
engine = create_engine(db_url)

# Crear la base para los modelos declarativos
Base = declarative_base()

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()


class CampoDeConocimiento(Base):
    __tablename__ = 'Campo_de_conocimiento'
    
    campo_id = Column(Integer, primary_key=True)
    nombre_del_campo = Column(String(100), nullable=False)
    
    def __repr__(self):
        return f"<CampoDeConocimiento(campo_id={self.campo_id}, nombre_del_campo='{self.nombre_del_campo}')"


class Categoria(Base):
    __tablename__ = 'Categoria'
    
    id_categoria = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    
    def __repr__(self):
        return f"<Categoria(id_categoria={self.id_categoria}, nombre='{self.nombre}')"


class Cobertura(Base):
    __tablename__ = 'Cobertura'
    
    id_cobertura = Column(Integer, primary_key=True)
    cobertura = Column(String(250), nullable=False)
    
    def __repr__(self):
        return f"<Cobertura(id_cobertura={self.id_cobertura}, cobertura='{self.cobertura}')"


class CodigoPostal(Base):
    __tablename__ = 'Codigo_Postal'
    
    id_codigo = Column(String(250), primary_key=True)
    
    def __repr__(self):
        return f"<CodigoPostal(id_codigo='{self.id_codigo}')"


class CondicionDeLaLicencia(Base):
    __tablename__ = 'Condicion_de_la_licencia'
    
    id_condicion_de_la_licencia = Column(Integer, primary_key=True)
    condicion_de_la_licencia = Column(String(250), nullable=False)
    
    def __repr__(self):
        return f"<CondicionDeLaLicencia(id_condicion_de_la_licencia={self.id_condicion_de_la_licencia}, condicion_de_la_licencia='{self.condicion_de_la_licencia}')"


class CorrespondeA(Base):
    __tablename__ = 'Corresponde_A'
    
    materias__idem = Column(String(25), primary_key=True)
    ejetem__ideje = Column(String(25), primary_key=True)
    
    def __repr__(self):
        return f"<CorrespondeA(materias__idem='{self.materias__idem}', ejetem__ideje='{self.ejetem__ideje}')"


class Auditoria(Base):
    __tablename__ = 'auditoria'
    
    id_auditoria = Column(Integer, primary_key=True, autoincrement=True)
    tabla_afectada = Column(String(100), nullable=False)
    operacion = Column(String(10), nullable=False)
    usuario = Column(String(100), nullable=False)
    fecha_hora = Column(DateTime, default=datetime.now)
    datos_antiguos = Column(JSON)
    datos_nuevos = Column(JSON)
    
    def __repr__(self):
        return f"<Auditoria(id_auditoria={self.id_auditoria}, tabla_afectada='{self.tabla_afectada}', operacion='{self.operacion}')>"