# Script para inicializar la base de datos del Observatorio Editorial

import os
import sys
import psycopg2
from psycopg2 import sql
from sqlalchemy import inspect

# Agregar el directorio raíz al path para importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.base import Base, engine, DB_CONFIG
from config import DB_CONFIG


def create_database():
    """Crea la base de datos si no existe"""
    # Conectar a PostgreSQL sin especificar una base de datos
    conn = psycopg2.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Verificar si la base de datos existe
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_CONFIG['database'],))
    exists = cursor.fetchone()
    
    if not exists:
        print(f"Creando base de datos '{DB_CONFIG['database']}'...")
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(DB_CONFIG['database'])
        ))
        print(f"Base de datos '{DB_CONFIG['database']}' creada exitosamente.")
    else:
        print(f"La base de datos '{DB_CONFIG['database']}' ya existe.")
    
    cursor.close()
    conn.close()


def create_tables():
    """Crea las tablas definidas en los modelos"""
    print("Creando tablas en la base de datos...")
    
    # Crear todas las tablas definidas en los modelos
    Base.metadata.create_all(engine)
    
    print("Tablas creadas exitosamente.")


def create_triggers():
    """Crea los triggers de auditoría en la base de datos"""
    print("Creando triggers de auditoría...")
    
    # Conectar a la base de datos
    conn = psycopg2.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Crear los triggers de auditoría
    triggers = [
        # Trigger para la tabla fuente
        """
        CREATE OR REPLACE FUNCTION public.auditoria_fuente() RETURNS trigger
            LANGUAGE plpgsql
            AS $$
        BEGIN
            IF (TG_OP = 'INSERT') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_nuevos)
                VALUES ('fuente', 'INSERT', current_user, to_jsonb(NEW));
            ELSIF (TG_OP = 'UPDATE') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos, datos_nuevos)
                VALUES ('fuente', 'UPDATE', current_user, to_jsonb(OLD), to_jsonb(NEW));
            ELSIF (TG_OP = 'DELETE') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos)
                VALUES ('fuente', 'DELETE', current_user, to_jsonb(OLD));
            END IF;
            RETURN NULL;
        END;
        $$;
        
        DROP TRIGGER IF EXISTS trigger_auditoria_fuente ON fuente;
        CREATE TRIGGER trigger_auditoria_fuente
        AFTER INSERT OR UPDATE OR DELETE ON fuente
        FOR EACH ROW EXECUTE FUNCTION auditoria_fuente();
        """,
        
        # Trigger para la tabla organizacion
        """
        CREATE OR REPLACE FUNCTION public.auditoria_organizacion() RETURNS trigger
            LANGUAGE plpgsql
            AS $$
        BEGIN
            IF (TG_OP = 'INSERT') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_nuevos)
                VALUES ('organizacion', 'INSERT', current_user, to_jsonb(NEW));
            ELSIF (TG_OP = 'UPDATE') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos, datos_nuevos)
                VALUES ('organizacion', 'UPDATE', current_user, to_jsonb(OLD), to_jsonb(NEW));
            ELSIF (TG_OP = 'DELETE') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos)
                VALUES ('organizacion', 'DELETE', current_user, to_jsonb(OLD));
            END IF;
            RETURN NULL;
        END;
        $$;
        
        DROP TRIGGER IF EXISTS trigger_auditoria_organizacion ON organizacion;
        CREATE TRIGGER trigger_auditoria_organizacion
        AFTER INSERT OR UPDATE OR DELETE ON organizacion
        FOR EACH ROW EXECUTE FUNCTION auditoria_organizacion();
        """,
        
        # Trigger para la tabla persona
        """
        CREATE OR REPLACE FUNCTION public.auditoria_persona() RETURNS trigger
            LANGUAGE plpgsql
            AS $$
        BEGIN
            IF (TG_OP = 'INSERT') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_nuevos)
                VALUES ('persona', 'INSERT', current_user, to_jsonb(NEW));
            ELSIF (TG_OP = 'UPDATE') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos, datos_nuevos)
                VALUES ('persona', 'UPDATE', current_user, to_jsonb(OLD), to_jsonb(NEW));
            ELSIF (TG_OP = 'DELETE') THEN
                INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos)
                VALUES ('persona', 'DELETE', current_user, to_jsonb(OLD));
            END IF;
            RETURN NULL;
        END;
        $$;
        
        DROP TRIGGER IF EXISTS trigger_auditoria_persona ON persona;
        CREATE TRIGGER trigger_auditoria_persona
        AFTER INSERT OR UPDATE OR DELETE ON persona
        FOR EACH ROW EXECUTE FUNCTION auditoria_persona();
        """
    ]
    
    for trigger_sql in triggers:
        try:
            cursor.execute(trigger_sql)
            print("Trigger creado exitosamente.")
        except Exception as e:
            print(f"Error al crear trigger: {e}")
    
    cursor.close()
    conn.close()


def main():
    """Función principal para inicializar la base de datos"""
    try:
        create_database()
        create_tables()
        create_triggers()
        print("Inicialización de la base de datos completada exitosamente.")
    except Exception as e:
        print(f"Error durante la inicialización de la base de datos: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()