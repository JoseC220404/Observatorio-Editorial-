# Script para inicializar la base de datos del Observatorio Editorial con Django

import os
import sys
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

# Cargar variables de entorno desde .env si existe
load_dotenv()

# Configuración de la base de datos
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'observatorio_editorial'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', ''),
}


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


def main():
    """Función principal para inicializar la base de datos"""
    create_database()
    print("\nPara completar la configuración de la base de datos, ejecute los siguientes comandos:")
    print("1. Instalar las dependencias de Django:")
    print("   pip install -r requirements_django.txt")
    print("2. Generar las migraciones de Django:")
    print("   python manage.py makemigrations")
    print("3. Aplicar las migraciones a la base de datos:")
    print("   python manage.py migrate")
    print("4. Crear un superusuario para acceder al panel de administración:")
    print("   python manage.py createsuperuser")
    print("5. Iniciar el servidor de desarrollo:")
    print("   python manage.py runserver")


if __name__ == '__main__':
    main()