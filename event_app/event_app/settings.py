import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', default='super_secret_key_513115%')

DEBUG = os.getenv('DEBUG', default='False').lower() == 'true'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default='*').split()

CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', default='http://*').split()
CSRF_TRUSTED_ORIGINS.extend(os.getenv('CSRF_TRUSTED_ORIGINS', default='https://*').split())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular',
    'rest_framework',
    'rest_framework.authtoken',
    'users.apps.UsersConfig',
    'api.apps.ApiConfig',
    'mailings.apps.MailingsConfig',
    'djoser',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'event_app.wsgi.application'

DATABASES = {
    'production': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'events_db'),
        'USER': os.environ.get('POSTGRES_USER', 'events_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'events_password'),
        'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES_PORT', 5432),
    },
    'debug_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'debug_db.sqlite3',
    }
}

DATABASES['default'] = DATABASES['debug_db'] if DEBUG else DATABASES['production']

AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'reset-password-confirmation/?uid={uid}&token={token}',
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'EMAIL': {
        'activation': 'core.email_djoser.ActivationEmail',
        'confirmation': 'core.email_djoser.ConfirmationEmail',
        'password_reset': 'core.email_djoser.PasswordResetEmail',
        'password_changed_confirmation': 'core.email_djoser.PasswordConfirmationEmail',
    },
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'ACTIVATION_URL': 'activate/?uid={uid}&token={token}',
    'SEND_ACTIVATION_EMAIL': True,
    'LOGIN_FIELD': 'email',
    # 'PERMISSIONS': {
    #     'user': ['rest_framework.permissions.IsAuthenticated'],
    # },
    'SERIALIZERS': {
        # тут нужен сериализатор для активации
        'activation': 'users.serializers.CustomActivationSerializer',
        'user': 'users.serializers.CustomUserSerializer',
        'current_user': 'users.serializers.CustomUserSerializer',
    },
    # 'CONSTANTS': {
    #     'messages': 'api.constants.DjoserMessages',
    # },
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', default='False').lower() == 'true'
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', default='False').lower() == 'true'

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_BROKER', 'redis://localhost:6379/0')
WEEKLY_SUBJECT = os.environ.get('WEEKLY_SUBJECT', 'Еженедельная рассылка Event')
