#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys 

SECRET_KEY = 'j_tk&q=p8nu_w*l)-(qi6)p7@72b(0%s=q5=pk8ofodllvp6ri'


ALLOWED_HOSTS=['*']
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.


#AUTHENTICATION_BACKENDS = (
#    'django_auth_ldap.backend.LDAPBackend',
#)


MEDIA_URL = '/media/'

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


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'crispy_forms',
    'bootstrap3',
    'Fondos',
    'django_filters',
    'widget_tweaks',
]

#LOGIN_REDIRECT_URL = '/inicio/' # It means home view
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
]

#LOGIN_URL = '/login/'

ROOT_URLCONF = 'Proyecto.urls'

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

WSGI_APPLICATION = 'Proyecto.wsgi.application'
LOGIN_REDIRECT_URL = '/' # It means home view


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#   'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'museo',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

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

#LOCALES
DEFAULT_CHARSET = 'utf-8'

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHELL_PLUS = "ipython"


STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)

#AUTENTICACION LDAP CON SERVIDOR DE PRUEBA EN WINDOWS 2008 R2 SERVER CON ACTIVE DIRECTORY

# LDAP ACTIVE DIRECTORY
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
)

# ldap authentication
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
)

# ldap authentication
import ldap
from django_auth_ldap.config import LDAPSearch, NestedActiveDirectoryGroupType

#IP de la intranet en mi máquina virtual
AUTH_LDAP_SERVER_URI = "ldap://10.17.11.3:389"
#root dn necesario para ver el arbol
AUTH_LDAP_BIND_DN = "cn=Administrador,dc=Museo,dc=es"
AUTH_LDAP_BIND_PASSWORD = "Contraseña1"

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=Unidades,dc=Museo,dc=es",
    ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=Museo,dc=es",
    ldap.SCOPE_SUBTREE, "(objectClass=group)"
)

AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=Activos,ou=Unidades,dc=Museo,dc=es",
    "is_staff": "cn=Administradores,ou=Unidades,dc=Museo,dc=es",
    "is_superuser": "cn=Administradores,ou=Unidades,dc=Museo,dc=es"
}

AUTH_LDAP_FIND_GROUP_PERMS = True
# Cache 
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

#nombre del servidor controlador de dominio
LDAP_SERVER_NAME = "Adriano"
LDAP_DOMAIN_BASE = "dc=Museo,dc=es"
LDAP_USERS_BASE = "ou=Unidades," + LDAP_DOMAIN_BASE
#aqui van los que pueden insertar datos
LDAP_INVENTARIO_BASE = "ou=InventarioRegistro," + LDAP_USERS_BASE
#aquí van los que pueden añadir informes y consultar
LDAP_RESTAURACION_BASE = "ou=Restauracion," + LDAP_USERS_BASE
LDAP_GROUPS_BASE = "ou=Grupos," + LDAP_DOMAIN_BASE
