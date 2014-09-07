"""
Django settings for canalzoom project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')0+uhgtsyo-h3b8b^c7)=!3h@vb+!oom1q@0nezu-u=x=58#lr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

"""
ALLOWED_HOSTS = [
    '104.131.27.165',
    '104.131.27.165.',
    'zoomcanalonline.co',
    'zoomcanalonline.co.',
    'zoomcanal.com.co',
    'zoomcanal.com.co.',
]
"""

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "home.context_processors.myProcessor",
    "home.context_processors.google_analytics",
    "social.apps.django_app.context_processors.backends",
    "social.apps.django_app.context_processors.login_redirect", 
)

GRAPPELLI_ADMIN_TITLE = 'Administracion Sitio Web Canal ZOOM'

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'south',
    'home',
    'tags',
    'categorias',
    'imagenes',
    'franjas',
    'entidades',
    'tipos_entidades',
    'videos',
    'tipos_usuario',
    'userprofiles',
    'estados_comentarios',
    'comentarios',
    'documentos',
    'documentos_en_linea',
    'noticias',
    'eventos',
    'oportunidades',
    'entradas_blogs',
    'blogs',
    'capitulos',
    'programas',
    'banners_publicidad',
    'paginas',
    'programaciones',
    'horarios_programacion',
    'informacion_canal',
    'carrusel',
    'banner_sizes',
    'tipos_videos',
    'fondos',
    'noticias_destacadas',
    'encuestas',
    'respuestas_encuestas',
    'suscriptores',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'canalzoom.urls'

WSGI_APPLICATION = 'canalzoom.wsgi.application'

# Define user's profile
AUTH_PROFILE_MODULE = 'userprofiles.models.UserProfile'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'canalzoom',
        'USER': 'root',
        'PASSWORD': 'root_pwd',
        'HOST': 'localhost',
        'PORT': '',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

#TIME_ZONE = 'UTC'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_URL = '/media/'

#Backends

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '257656264425434'
SOCIAL_AUTH_FACEBOOK_SECRET = '5543b2e5830e411ed1b0aa8697d92fab'
SOCIAL_AUTH_FACEBOOK_NAMESPACE = 'canalzoom'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'es'}

SOCIAL_AUTH_TWITTER_KEY = 'foYyoV2wJhXAOG0cUrEHj4M8O'
SOCIAL_AUTH_TWITTER_SECRET = 'vSZj9QUwogvK5Ghzxi3xWDoFXPuQvJNfXXC3hLdDuebyFsfg4a'

# Configuracion de correo
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'administrador@zoomcanal.com.co'
EMAIL_HOST_PASSWORD = 'zoom2014'
EMAIL_USE_TLS = True

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-51345899-2'
GOOGLE_ANALYTICS_DOMAIN = 'zoomcanal.com.co'