import os
from .base import *

# Static files settings
STATIC_URL = 'https://<production_domain_name>/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files settings
MEDIA_URL = 'https://<production_domain_name>/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'media')

# Debug settings
DEBUG = False
ALLOWED_HOSTS = ['<production_domain_name>']

# Database settings
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, 'db.sqlite3')),
        "USER": os.environ.get("SQL_USER", "myuser"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "myuserpassword"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "3306"),
    }
}