from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@wjge4yt=zqt3^8iz(6438o(@!oj+1ikhdq7@8+5bisl($4t7j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"] #["127.0.1.1", "192.168.1.170"]

INSTALLED_APPS = [
    "libres",
    'rest_framework',
    'rest_framework_simplejwt',
    #'rest_framework_simplejwt.token_blacklist',
    "djoser",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    "user"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
        'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'res.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'res.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE", 'django.db.backends.sqlite3'),
        'NAME': os.getenv("NAME", BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv("PASSWORD"),
        'HOST': 'localhost',
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
LOGOUT_REDIRECT_URL="/library/"
LOGIN_REDIRECT_URL="/library/"

LOGIN_URL="/library/login/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "user.User"
#STATICFILES_DIRS = [BASE_DIR/"static"]
#MEDIA_URL = "media/"
#MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
#MEDIA_ROOT = '/home/baun/Desktop/baun-lib/media/'
MEDIA_URL = '/media/'
FILE_UPLOAD_MAX_MEMORY_SIZE= 60000000 #15MB
USE_X_FORWARDED_HOST = True
CSRF_TRUSTED_ORIGINS = ["http://127.0.1.1", "http://192.168.1.170", "http://eduvault.local", "http://localhost:5173"]

CORS_ORIGIN_WHITELIST = [
    'http://127.0.1.1',
    "http://192.168.1.170",
   "http://eduvault.local",
   "http://localhost:5173"
]

MAX_UPLOAD_SIZE = "52428800"
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_CROSS_ORIGIN_OPENER_POLICY = None

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('JWT',),
}

REST_FRAMEWORK = {
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', 
    #'PAGE_SIZE': 2, 
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        #"rest_framework.authentication.SessionAuthentication",
        #"rest_framework.authentication.TokenAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}


SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_USER_MODEL_USERNAME_FIELD="username"
ACCOUNT_EMAIL_VERIFICATION = "none"#'mandatory'
ACCOUNT_USERNAME_REQUIRED = True#False
ACCOUNT_EMAIL_REQUIRED = False


# Additional configuration settings
#SOCIALACCOUNT_QUERY_EMAIL = True
#ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_EMAIL_FIELD = None
ACCOUNT_UNIQUE_EMAIL = False



DJOSER = {
    'USER_ID_FIELD': 'username',
    'LOGIN_FIELD': 'username',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_FIELD': 'username',
    
}
