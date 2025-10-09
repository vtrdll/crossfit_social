"""
Django settings for app project (Railway Production).

Configuração pronta para:
- PostgreSQL (DATABASE_URL)
- Redis (REDIS_URL) + Celery + Beat
- Cloudinary (CLOUDINARY_URL)
- Static files com Whitenoise
"""

import os
from pathlib import Path
import dj_database_url
import sys
from dotenv import load_dotenv
load_dotenv()


print("DJANGO_SETTINGS_MODULE:", os.getenv("DJANGO_SETTINGS_MODULE"), file=sys.stderr)
print("DATABASE_URL:", os.getenv("DATABASE_URL"), file=sys.stderr)
print("REDIS_URL:", os.getenv("REDIS_URL"), file=sys.stderr)


# ------------------------------
# BASE
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# SECRET & DEBUG
# ------------------------------
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"

# ------------------------------
# HOSTS & CSRF
# ------------------------------
ALLOWED_HOSTS = "crossfitsocial-social.up.railway.app"
CSRF_TRUSTED_ORIGINS = ["https://crossfitsocial-social.up.railway.app", "https://127.0.0.1:8000/"]

# ------------------------------
# DATABASE
# ------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# ------------------------------
# STATIC FILES (Whitenoise)
# ------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'app' / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # servir static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ------------------------------
# TEMPLATES
# ------------------------------
ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# ------------------------------
# TIMEZONE
# ------------------------------
TIME_ZONE = os.getenv("TZ", "America/Sao_Paulo")
USE_TZ = True
USE_I18N = True
LANGUAGE_CODE = 'en-us'

# ------------------------------
# MEDIA / CLOUDINARY
# ------------------------------
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")
CLOUDINARY_SECURE = os.getenv("CLOUDINARY_SECURE", "True") == "True"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cloudinary',
    'cloudinary_storage',
    'django_celery_beat',

    # seus apps
    'Social',
    'account',
    'widget_tweaks',
    'Event',
    'WOD',
]



# ------------------------------
# CELERY
# ------------------------------
CELERY_BROKER_URL = os.getenv("REDIS_URL")
CELERY_RESULT_BACKEND = os.getenv("REDIS_URL")
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Exemplo de task agendada
from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    'deletar-imagens-antigas-diariamente': {
        'task': 'Social.tasks.delete_old_media',
        'schedule': crontab(minute='*'),  # todos os dias à meia-noite
    },
}


STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },

    "media_videos": {
        "BACKEND": "cloudinary_storage.storage.VideoMediaCloudinaryStorage",  
    },

    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ------------------------------
# AUTH / LOGIN
# ------------------------------
LOGIN_URL = '/login'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------
# DEFAULT PRIMARY KEY
# ------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
'''

DB_LIVE = os.getenv("DB_LIVE", "False")
if DB_LIVE in ["False", False]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
    }

'''