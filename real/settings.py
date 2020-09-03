"""
Django settings for real project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Template_DIR = os.path.join(BASE_DIR, 'templates')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=0sm+-f63+ox@7z(9jw%orv_h89cd@8f!@+$jo9ru=1!-zt=1b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['45.79.120.98','127.0.0.1','0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'crispy_forms',
    'blog.apps.BlogConfig',
    'my_app.apps.MyAppConfig',
    # default Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'real.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Template_DIR,],
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

WSGI_APPLICATION = 'real.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default' : {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'USER': 'dumidu@djangomysql',
    #     'NAME': 'test',
    #     'PASSWORD': 'Withikuliya1',
    #     'HOST': 'djangomysql.mysql.database.azure.com',
    #     'PORT': '3306',
    # },
    # 'default' : {
    #     'ENGINE' : 'django.db.backends.mysql',
    #     'OPTIONS' : {
    #         'read_default_file' : os.path.join(BASE_DIR,'mysql.cnf'),
    #     },
    # },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

STATICFILES_DIR = (os.path.join(BASE_DIR, 'static'),)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

#B2

DEFAULT_FILE_STORAGE = 'b2_storage.storage.B2Storage'
BACKBLAZEB2_APP_KEY_ID = 'f39a22bb02f7'
BACKBLAZEB2_APP_KEY= '002d95770f8687e8a9d9e1f1539b321e348a0fbe90'
B2_BUCKET_NAME= 'fingershopping'
BACKBLAZEB2_BUCKET_ID = 'bf2349dad2624b9b70420f17'