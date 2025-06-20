# Configuración WSGI para el Observatorio Editorial

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'observatorio_editorial.settings')

application = get_wsgi_application()