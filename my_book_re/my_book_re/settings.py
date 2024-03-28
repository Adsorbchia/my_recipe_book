"""
Django settings for my_book_re project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from re import L

from django.conf.global_settings import AUTH_USER_MODEL, INTERNAL_IPS, LOGIN_URL
from dotenv import load_dotenv  


load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$4yv@$c2lemes^l)0@3ami6y^n8#4*a2eee^@h(yolg)iq7duv'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")  

if os.environ.get("DEBUG") == "False":
    DEBUG = False
else:
    DEBUG = True

SESSION_COOKIE_SECURE = True  
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS =  ["127.0.0.1", "natniks.pythonanywhere.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
   
    
    'debug_toolbar',
    'main', 
    'recipe_catalog',
    'users',
    'carts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    

    'debug_toolbar.middleware.DebugToolbarMiddleware',
   
]

ROOT_URLCONF = 'my_book_re.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'my_book_re.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'home',
#         'USER': 'home',
#         'PASSWORD': 'home',
#         'HOST': 'localhost',
#         'PORT': '5432',

#     }
# }
DATABASES = {  
    "default": {  
        "ENGINE": "django.db.backends.mysql",  
        "NAME": os.environ("MYSQL_DBNAME"),  
        "USER": os.environ("MYSQL_USER"),  
        "PASSWORD": os.environ("MYSQL_PASSWORD"),  
        "HOST": os.environ("MYSQL_HOST"),  
        "OPTIONS": {  
            "init_command": "SET NAMES 'utf8mb4';SET sql_mode = 'STRICT_TRANS_TABLES'",  
            "charset": "utf8mb4",  
        },  
    }  
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "static/"  

# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
#     ]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

INTERNAL_IPS = [
    '127.0.0.1',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/user/login/'


