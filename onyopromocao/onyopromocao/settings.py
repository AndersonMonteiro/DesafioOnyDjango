import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from configurations import Configuration

load_dotenv(find_dotenv())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config(Configuration):
    SECRET_KEY = '@5j_82@0g@+x0ydb!*$wwc8#!usk=u_rvhk%_@)sy-e^#z)gs='
    #SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = True
    ALLOWED_HOSTS = []
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'api',
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
    ROOT_URLCONF = 'onyopromocao.urls'
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
    WSGI_APPLICATION = 'onyopromocao.wsgi.application'
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
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    STATIC_URL = '/static/'

class Dev(Config):
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'OnyoPromocao',
            'USER': 'postgres',
            'PASSWORD': '123qwe!',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

class Test(Config):
    TESTING = True
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


# class Prod(Config):
#     ALLOWED_HOSTS = ['']
#     STATIC_ROOT = str(BASE_DIR / 'staticfiles')
#     STATICFILES_DIRS = [
#         str(BASE_DIR / "static"),
#     ]