from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2323jawerjwjr23j42jadkfajkdfjwejwl3242$$@@$5242jjF24' 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'beres',
        'USER': 'admin',
        'PASSWORD': 'abcd1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
