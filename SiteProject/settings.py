"""
Django settings for SiteProject project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y-&1aa_oy78jjcl8*^=b3_4^%tyb94b&cip&p^pgy#rbt7nm62'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

"""CUSTOM SETTINGS FOR EMAIL"""
EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="rishikesh0014051992@gmail.com"
EMAIL_HOST_PASSWORD="29915041"
EMAIL_PORT=587
EMAIL_USE_TLS=True

# Application definition

INSTALLED_APPS = (
    #Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites' , #It will be added here only
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #I added it for django-registration-redux
    #3rd party app(s)
    "crispy_forms",
    "registration", #pip install django-registration-redux

    #My app(s)
    "HyGoApp",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'SiteProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'SiteProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT=os.path.join(BASE_DIR,"static_as_source_child","static_root")
#STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_as_source_sibling","static_root")

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"static_as_source_child","our_static"),
)


#Media(Profile Pic etc...)

MEDIA_URL ="/media/"
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_as_source_sibling","media_root")


#For crispy forms
CRISPY_TEMPLATE_PACK ="bootstrap3"

#Django Registration Redux
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1 #After setting only this ... visit accounts/login/ otherwise...site query does not
LOGIN_REDIRECT_URL = '/blogs/' #After login at /accounts/login/....it will, be the destination