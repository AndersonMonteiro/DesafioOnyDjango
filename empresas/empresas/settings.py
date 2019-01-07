import os
from configurations import Configuration
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(find_dotenv())

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent.parent

class Config(Configuration):
    SECRET_KEY = 'wq9j93ziqrg1f95a*=e5_r)+d#iwud#l^*rag3zd-al638y5bs'
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
        'rest_framework_swagger',
        'api',
    ]
    MIDDLEWARE = [
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ROOT_URLCONF = 'empresas.urls'
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
    WSGI_APPLICATION = 'empresas.wsgi.application'
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
    CACHE = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        }
    }

class Dev(Config):
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'OnyoEmpresa',
            'USER': 'postgres',
            'PASSWORD': '123qwe!',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }

class Test(Config):
    TESTING = True
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

class Prod(Config):
    ALLOWED_HOSTS = ['des-onyo-empresas.herokuapp.com']
    STATIC_ROOT = str(BASE_DIR / 'staticfiles')
    STATICFILES_DIRS = [
        str(BASE_DIR / "static"),
    ]
