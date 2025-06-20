# Observatorio Editorial

Este proyecto implementa un sistema de gestión para un observatorio editorial, permitiendo el seguimiento y análisis de publicaciones, organizaciones, personas y otros elementos relacionados con el ámbito editorial.

## Estructura de la Base de Datos

El sistema utiliza PostgreSQL como motor de base de datos. La estructura incluye tablas para:

- Campos de conocimiento
- Categorías
- Coberturas
- Códigos Postales
- Condiciones de licencia
- Relaciones entre materias y ejes temáticos
- Sistema de auditoría para seguimiento de cambios

## Requisitos

- Python 3.8+
- PostgreSQL 12+
- Dependencias de Python (ver requirements.txt o requirements_django.txt)

## Configuración

1. Clonar el repositorio
2. Crear un entorno virtual: `python -m venv venv`
3. Activar el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalar dependencias según la versión que desees usar:
   - Para la versión con Django: `pip install -r requirements_django.txt`
   - Para la versión con Flask: `pip install -r requirements.txt`
5. Configurar las variables de entorno (opcional):
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=observatorio_editorial
   DB_USER=postgres
   DB_PASSWORD=tu_contraseña
   DEBUG=True
   ```

## Inicialización de la Base de Datos

### Opción 1: Usando SQLAlchemy

```bash
python setup_database.py
```

Este script creará la base de datos, las tablas y los triggers de auditoría necesarios.

### Opción 2: Usando Django

```bash
python setup_django_database.py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Estructura del Proyecto

```
.
├── api/                      # Aplicación Django para la API REST
├── models/                   # Modelos SQLAlchemy para acceso directo a la BD
├── observatorio_editorial/   # Configuración principal de Django
├── config.py                 # Configuración general del proyecto
├── database_schema.sql       # Esquema de la base de datos
├── setup_database.py         # Script para inicializar la BD con SQLAlchemy
├── setup_django_database.py  # Script para inicializar la BD con Django
└── requirements.txt          # Dependencias del proyecto
```

## Uso

### API REST con Django

```bash
python manage.py runserver
```

La API estará disponible en http://localhost:8000/api/
El panel de administración estará disponible en http://localhost:8000/admin/

### Aplicación Flask (pendiente de implementación)

```bash
python app.py
```

La aplicación estará disponible en http://localhost:5000

## Endpoints de la API

La API REST proporciona los siguientes endpoints:

- `/api/campos/` - Campos de conocimiento
- `/api/categorias/` - Categorías
- `/api/coberturas/` - Coberturas
- `/api/codigos-postales/` - Códigos postales
- `/api/condiciones-licencia/` - Condiciones de licencia
- `/api/corresponde-a/` - Relaciones entre materias y ejes temáticos
- `/api/auditoria/` - Registros de auditoría

Cada endpoint soporta las operaciones CRUD estándar:
- GET / - Listar todos los registros
- GET /{id}/ - Obtener un registro específico
- POST / - Crear un nuevo registro
- PUT /{id}/ - Actualizar un registro existente
- DELETE /{id}/ - Eliminar un registro

## Auditoría

El sistema incluye un mecanismo de auditoría que registra automáticamente los cambios realizados en las tablas principales. Los registros de auditoría se pueden consultar a través del endpoint `/api/auditoria/` o en el panel de administración.