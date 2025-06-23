import os
from urllib.parse import urlparse
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Use environment variables for sensitive data
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-dev-secret-key')
DEBUG = True

ALLOWED_HOSTS = ['*', 'ethiopoultry.up.railway.app']

# Redis URL (for Railway, use from env or fallback)
REDIS_URL = "redis://default:WwZOBGpRIdVuqPNppUuQGURrkKNXLXcr@redis.railway.internal:6379"

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "http://localhost:8000").split(',')

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Languages
LANGUAGES = [
    ('en', _('English')),
    ('am', _('Amharic')),
    ('om', _('Oromiffa')),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_SAMESITE = 'Lax'

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'channels',
    'rest_framework',
    'corsheaders',
    'cloudinary',
    'cloudinary_storage',
    'base',
    'items',
    'conversation',
    'users',
    'contact',
    'companies',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'ALLOW-FROM https://t.me/'

ROOT_URLCONF = 'project.urls'
ASGI_APPLICATION = 'project.asgi.application'
WSGI_APPLICATION = 'project.wsgi.application'
DAPHNE_TIMEOUT = 50

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}

AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = ['users.backends.UsernamePhoneBackend']
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'contact/static'),
    os.path.join(BASE_DIR, 'base/static'),
    os.path.join(BASE_DIR, 'conversation/static'),
    os.path.join(BASE_DIR, 'items/static'),
    os.path.join(BASE_DIR, 'users/static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Timezone and language
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Africa/Addis_Ababa'
USE_I18N = True
USE_TZ = True

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cloudinary
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME", "doixo5oiw"),
    api_key=os.environ.get("CLOUDINARY_API_KEY", "435759228322341"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET", "H3_ZVEXWGcyuE28IfKWUYsTo5sY"),
    secure=True
)



# database
DATABASE_URL = os.getenv('DATABASE_PUBLIC_URL') or os.getenv('DATABASE_URL')

db_info = urlparse(DATABASE_URL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_info.path[1:],
        'USER': db_info.username,
        'PASSWORD': db_info.password,
        'HOST': db_info.hostname,
        'PORT': db_info.port,
    }
}