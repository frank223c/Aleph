#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

SECRET_KEY = 'j_tk&q=p8nu_w*l)-(qi6)p7@72b(0%s=q5=pk8ofodllvp6ri'


ALLOWED_HOSTS=['*']
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

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


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

###############################
#
#        Aplicaciones necesarias
#
###############################

INSTALLED_APPS = [
#Extra para el admin
    'suitlocale',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#Extra para debug
    'django_extensions',
#Aplicaciones de terceros
    'crispy_forms',
    'bootstrap3',
    'Fondos',
    'django_filters',
    'widget_tweaks',
    'django.contrib.humanize',
    'bug',
]



# Django Suit 
SUIT_CONFIG = {
    # header
     'ADMIN_NAME': 'Administración de Aleph',
     'HEADER_DATE_FORMAT': 'l, j. F Y',
     'HEADER_TIME_FORMAT': 'H:i',

    # formulario
     'SHOW_REQUIRED_ASTERISK': True,  # Default True
     'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
     'SEARCH_URL': '/admin/auth/user/',
     'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
     },
     'MENU_OPEN_FIRST_CHILD': True, # Default True
     'MENU_EXCLUDE': ('auth.group',),
     'MENU': (
    #     'sitios',
         {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
         {'label': 'Configuración', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
         {'label': 'Ayuda', 'icon':'icon-question-sign', 'url': '/support/'},
     ),

     'LIST_PER_PAGE': 20
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Proyecto.urls'


WSGI_APPLICATION = 'Proyecto.wsgi.application'
LOGIN_REDIRECT_URL = '/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


###############################
#
#  Conexión en postgres
#
###############################

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



###############################
# Conexión a Active Directory realizada
# con la siguiente utilidad:
#    http://pythonhosted.org/django-auth-ldap/; he seguido este ejemplo de
# ¡¡cuidado con la cadena de conexión!!
###############################

#le decimos que use unicamente de backend en AD de nuestro servidor
AUTHENTICATION_BACKENDS = (
 #'django_auth_ldap.backend.LDAPBackend',
 'django.contrib.auth.backends.ModelBackend',
)


#AUTENTICACION LDAP CON SERVIDOR DE PRUEBA EN WINDOWS 2008 R2 SERVER CON ACTIVE DIRECTORY
import ldap
AUTH_LDAP_SERVER_URI = "ldap://10.17.11.3:389"

#bindeo simple de root dn
AUTH_LDAP_BIND_DN = 'Administrador@junta-andalucia.es'
AUTH_LDAP_BIND_PASSWORD = 'Contraseña1'

LDAP_IGNORE_CERT_ERRORS = False


from django_auth_ldap.config import LDAPSearch,NestedActiveDirectoryGroupType

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=MCA_usuarios,ou=Museo,ou=Unidades,DC=junta-andalucia,dc=es",
        ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")


AUTH_LDAP_USER_ATTR_MAP = {
 "first_name":"givenName", 
 "last_name":"sn",
 "email":"mail", 
 }

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=MCA_Grupos,ou=Museo,ou=Unidades,dc=junta-andalucia,dc=es",
ldap.SCOPE_SUBTREE,"(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

#flags por grupo
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
  "is_active":"cn=Activos,ou=MCA_Grupos,ou=Museo,ou=Unidades,dc=junta-andalucia,dc=es",
  "is_staff": "cn=Administradordca,ou=MCA_Grupos,ou=Museo,ou=Unidades,dc=junta-andalucia,dc=es",
  "is_superuser": "cn=Administradordca,ou=MCA_Grupos,ou=Museo,ou=Unidades,dc=junta-andalucia,dc=es",}
  
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600
#cache de una hora

#busqueda de usuarios
LDAP_DOMAIN_BASE = "dc=junta-andalucia,dc=es"
LDAP_USERS_BASE = "ou=MCA_usuarios," + LDAP_DOMAIN_BASE
LDAP_INVENTARIO_BASE = "ou=InventarioRegistro," + LDAP_USERS_BASE
LDAP_RESTAURADORBA_BASE = "ou=Restauracion," + LDAP_USERS_BASE
LDAP_RESTAURADORARQ_BASE = "ou=Arqueologia," + LDAP_USERS_BASE

#opcion necesaria
AUTH_LDAP_CONNECTION_OPTIONS = {
ldap.OPT_DEBUG_LEVEL: 1,
ldap.OPT_REFERRALS: 0,}


##################################
#   Comentar para entorno de producción
#   esto aparecerá en la consola cuand
#   haya un intento de inicio de sesión
#   se verá como se comprueba la existencia del usuario
################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'stream_to_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_auth_ldap': {
            'handlers': ['stream_to_console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


#~ SESSION_COOKIE_SECURE=True
#~ SESSION_COOKIE_HTTPONLY=True
#~ SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
#~ SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS =  True
SECURE_CONTENT_TYPE_NOSNIFF = True
