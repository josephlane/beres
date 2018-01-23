from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY'] 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['CONN_MAX_AGE'] = 500

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
