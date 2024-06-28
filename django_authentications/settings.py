"""
Django settings for django_authentications project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
#
from django.conf.global_settings import DATABASES
from pandas import Timedelta

import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =os.environ.get('DEBUG')





ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'todo.apps.TodoConfig',
    'blog.apps.BlogConfig',
    'ckeditor',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'drf.apps.DrfConfig',
    'rest_framework',
    'drf_api_view.apps.DrfApiViewConfig',
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",

]
import os

ROOT_URLCONF = 'django_authentications.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates')],
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

WSGI_APPLICATION = 'django_authentications.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


database_url=os.environ.get('DATABASE_URL')
DATABASES['default'] = dj_database_url.parse(database_url)

#("postgresql://django_blog_tdm1_user:CSeuCiOouLHcxVxLLL0WoqcfXjt0iZT9@dpg-cpu42phu0jms73eja4p0-a.singapore-postgres.render.com/django_blog_tdm1")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'

# settings.py
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend'

]

#
# REST_FRAMEWORK = {
#
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#     'DEFAULT_THROTTLE_RATES':{
#         'anon':'2/day',
#         'user':'5/hour',
#         'jack':'3/hour'
#     }
#
# }

# settings.py


SITE_ID = 1
LOGIN_REDIRECT_URL = 'home_blog',
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False

SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_LOGIN_ON_GET = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ankitdevkota107@gmail.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")  # Your Gmail password or app-specific password

SIMPLE_jWT = {
    'ACCESS_TOKEN_LIFETIME': Timedelta(minutes=10),
    'ROTATE_REFRESH_TOKENS': True

}
# REST_FRAMEWORK = {
#     # 'DEFAULT_AUTHENTICATION_CLASSES': (
#     #     'rest_framework_simplejwt.authentication.JWTAuthentication',
#     # ),
#     'DEFAULT_THROTTLE_CLASSES': [
#         'rest_framework.throttling.UserRateThrottle',
#         'rest_framework.throttling.AnonRateThrottle',
#         'rest_framework.throttling.ScopedRateThrottle',
#         'drf_api_view.throttless.JackThrottle'
#
#     ],
#     'DEFAULT_THROTTLE_RATES': {
#         'anon': '10/minute',
#         'user': '10/minute',
#         'jack': '5/day',
#     },
#     'DEFAULT_FILTER_BACKENDS' : [
#         'django_filters.rest_framework.DjangoFDilterBackend',
#     ],
#
# }
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle',
        'drf_api_view.throttless.JackThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '10/minute',
        'jack': '5/day',
    },
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}
import os

STATICFILES_DIRS=os.path.join(BASE_DIR,'static'),
STATIC_ROOT = BASE_DIR/"staticfiles_build"/"static"




