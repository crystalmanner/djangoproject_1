from .base import *
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = [
#     # 'https://jgiapp1.herokuapp.com/',  # heroku url
#     '*',
# ]
#
# DATABASES = {'default': dj_database_url.config()}
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
#
# MIDDLEWARE += [
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]
#
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#     'compressor.finders.CompressorFinder',
# )
#
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# DEFAULT_FILE_STORAGE = 'whitenoise.storage.'
#
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)