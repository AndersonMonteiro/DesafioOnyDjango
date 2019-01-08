import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from configurations import Configuration

load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).parent.parent

class Config(Configuration):
    SECRET_KEY = os.environ['SECRET_KEY']
    EMPRESA_URL = os.environ['EMPRESA_URL']
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


class Prod(Config):
    ALLOWED_HOSTS = ['des-onyo-promocao.herokuapp.com']
    STATIC_ROOT = str(BASE_DIR / 'staticfiles')
    STATICFILES_DIRS = [
        str(BASE_DIR / "static"),
    ]
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'dbpr6tqgkuhuo3',
    #         'USER': 'rbktrfeehyxvhv',
    #         'PASSWORD': 'bea3e32c796c88037ecb53ceb5ccff5b2bc292811e7a00b5c27fc6aa80182fa7',
    #         'HOST': 'ec2-107-20-183-142.compute-1.amazonaws.com',
    #         'PORT': '5432',
    #     }
    # }
