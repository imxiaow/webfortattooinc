"""
Django settings for tattowebsite project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
from dotenv import load_dotenv
import psycopg2
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#====================================================================
#======== DEVELOPMENT SETTING =======================================
#====================================================================
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

#dotenv_file = os.path.join(BASE_DIR, ".env")
#if os.path.isfile(dotenv_file):
#    load_dotenv(dotenv_file)

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ['SECRET_KEY'] 

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#ALLOWED_HOSTS = []


#====================================================================
#======== Production SETTING ========================================
#====================================================================
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.01','wildcranetattoowebxw.herokuapp.com', '.herokuapp.com', 'wildcranetattoos.com']
#'192.168.1.41'


#====================================================================
# ====== BASE Setting ===============================================
#====================================================================
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'firstversionweb',
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

ROOT_URLCONF = 'tattowebsite.urls'

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

WSGI_APPLICATION = 'tattowebsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/image')


ADMINS = [('Xiao','xiaow9596@gmail.com'),('Xiao2','xiaow.wang@mail.utoronto.ca')]
MANAGERS = ADMINS

#======== Email BASE Settings=======================
# myaccount.google.com/lesssecureapps
# myaccount.google.com/apppasswords
# SMTP Configuration
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@wildcranetattoos.com'
EMAIL_USE_TLS = True
#EMAIL_USE_SSL = True

#====================================================================
#======== DEVELOPMENT SETTING =======================================
#====================================================================
# Add .env variables anywhere before SECRET_KEY
#dotenv_file = os.path.join(BASE_DIR, ".env")
#if os.path.isfile(dotenv_file):
#    load_dotenv(dotenv_file)

# Update secret key
#EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] #Instead of your actual secret key

#GOOGLE_RECAPTCHA_SECRET_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_KEY'] 

#CORS_REPLACE_HTTPS_REFERER = False
#HOST_SCHEME = "http://"
#SECURE_PROXY_SSL_HEADER = None
#SECURE_SSL_REDIRECT = False
#SESSION_COOKIE_SECURE = False
#CSRF_COOKIE_SECURE = False
#SECURE_HSTS_SECONDS = None
#SECURE_HSTS_INCLUDE_SUBDOMAINS = False
#SECURE_FRAME_DENY = False

#====================================================================
#======== Production SETTING =======================================
#====================================================================
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv('GOOGLE_RECAPTCHA_SECRET_KEY')


# HTTPS setting 
SESSION_COOKIE_SECURE = True #make sure the cookie is served https 
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True 

# HTST setting
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Activate Django-Heroku
django_heroku.settings(locals())

# Debugging in heroku live
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)




#END 
#====================================================================
#====================================================================
# NOT USE/IMPLEMENT due to inconsistent cross different browser 
# ========Content Security Policy =======================================
#CSP_DEFAULT_SRC = ("'none'", )
#CSP_STYLE_SRC = ("'self'", "fonts.googleapis.com", "stackpath.bootstrapcdn.com", "code.jquery.com", "cdnjs.cloudflare.com", "fontawesome.com", "'unsafe-inline'",'')
#    "'unsafe-inline'",
#CSP_SCRIPT_SRC = ("'self'", "google.com/recaptcha/api.js", "stackpath.bootstrapcdn.com", "code.jquery.com", "cdnjs.cloudflare.com", 'https://www.google.com/recaptcha/api.js')
#CSP_IMG_SRC = ("'self'",)
#CSP_FONT_SRC = ("'self'",'fonts.gstatic.com', 'cdnjs.cloudflare.com')
#CSP_MANIFEST_SRC = ("'self'", )
#CSP_MEDIA_SRC = ("'self'",)
#CSP_SCRIPT_SRC_ELEM = ("'self'", 
#    'https://www.google.com/recaptcha/api.js', 
#    'https://code.jquery.com/jquery-3.3.1.slim.min.js', 
#    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js', 
#    'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js', 
#    'https://www.gstatic.com/recaptcha/releases/qc5B-qjP0QEimFYUxcpWJy5B/recaptcha__zh_cn.js',)
#CSP_CONNECT_SRC = ("'self'", )
#CSP_OBJECT_SRC = ("'none'", )
#CSP_BASE_URI = ("'none'", )
#CSP_FRAME_SRC =("'self'", 'https://www.google.com/',)
#CSP_FRAME_ANCESTORS = ("'self'", 'https://example.com/',)
#CSP_FORM_ACTION = ("'self'", )
#CSP_INCLUDE_NONCE_IN = ('script-src',)


#====================================================================
#===== END =======
#====================================================================