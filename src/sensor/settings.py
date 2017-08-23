"""Django settings for scos-sensor project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/

"""

import os


# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    ('js', os.path.join(STATIC_ROOT, 'js')),
    ('css', os.path.join(STATIC_ROOT, 'css')),
    ('images', os.path.join(STATIC_ROOT, 'images')),
    ('fonts', os.path.join(STATIC_ROOT, 'fonts')),
)

# See scripts/setevn.template
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = bool(os.environ['DEBUG'])
ALLOWED_HOSTS = os.environ['DOMAINS'].split() + os.environ['IPS'].split()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    # project-local apps
    'acquisitions.apps.AcquisitionsConfig',
    'authentication.apps.AuthenticationConfig',
    'schedule.apps.ScheduleConfig',
    'scheduler.apps.SchedulerConfig',
    'status.apps.StatusConfig',
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

ROOT_URLCONF = 'sensor.urls'


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
            ],
        },
    },
]

WSGI_APPLICATION = 'sensor.wsgi.application'


# Django Rest Framework
# http://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'sensor.exceptions.exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# Django Rest Swagger
# http://marcgibbons.github.io/django-rest-swagger/
SWAGGER_SETTINGS = {
    'LOGIN_URL': '/api/auth/login',
    'LOGOUT_URL': '/api/auth/logout'
}


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('/tmp', 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 20
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'authentication.User'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'scos-sensor.log'
        }
    },
    'loggers': {
        'actions': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'acquisitions': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'capabilities': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'schedule': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'scheduler': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'sensor': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'status': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        }
    }
}
