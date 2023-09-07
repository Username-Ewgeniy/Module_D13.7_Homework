"""
Django settings for billboard project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv #pip install python-dotenv

load_dotenv()
env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4#ux4j6yq5p2oetvtoxefllyjw!ytd2i!5r2vth4qmoj&-d-fn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_filters',
    'users',
    'ads'


]

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
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

ROOT_URLCONF = 'billboard_project.urls'

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

                "billboard_project.context_processors.counters"
            ],
        },
    },
]

WSGI_APPLICATION = 'billboard_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

LOGIN_URL = 'users/login'

LOGIN_REDIRECT_URL = '/'

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'none' 



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')




# [-- Модуль D6.2. Отправляем письма через Django
EMAIL_HOST = 'smtp.yandex.ru' # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465 # порт smtp сервера тоже одинаковый

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER') # ваше имя пользователя, 
# например если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') # пароль от почты


EMAIL_USE_SSL = True # Яндекс использует ssl, подробнее о том, что это, почитайте на Википедии, но включать его здесь обязательно
# --]

# [-- Модуль D6.2. Отправляем письма через Django
# Есть варианты отправлять информацию по почте, например, какой-то определённой группе пользователей — админам.
EMAIL_ADMIN = os.getenv('EMAIL_ADMIN')
SERVER_EMAIL = os.getenv('SERVER_EMAIL') # это будет у нас вместо аргумента FROM в массовой рассылке
# --]

# [-- D6.3. Django-allauth и email. Регистрация пользователя с подтверждением по электронной почте
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER # если вы используете Яндекс, то не забудьте добавить + ‘@yandex.ru’
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')  # здесь указываем уже свою ПОЛНУЮ почту с которой будут отправляться письма 
# если вы используете Яндекс, то не забудьте добавить + ‘@yandex.ru’
# --]