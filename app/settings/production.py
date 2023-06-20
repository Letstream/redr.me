from .base import *

USE_AWS = True if env('USE_AWS') == 'True' else False

if USE_AWS:
    INSTALLED_APPS.append('storages')

    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    AWS_STATIC_LOCATION = 'static'
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
    STATICFILES_STORAGE = 'app.storage_backends.StaticStorage'

    AWS_PUBLIC_MEDIA_LOCATION = "media/public"
    DEFAULT_FILE_STORAGE = "app.storage_backends.PublicMediaStorage"

    AWS_PRIVATE_MEDIA_LOCATION = "media/private"
    PRIVATE_FILE_STORAGE = "app.storage_backends.PrivateMediaStorage"

    AWS_S3_SIGNATURE_VERSION = 's3v4'

    AWS_S3_REGION_NAME = env('AWS_REGION')
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = env('STATIC_ROOT')

    # # enable whitenoise
    # MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    MEDIA_URL = '/uploads/'
    MEDIA_ROOT = env('UPLOAD_ROOT')
    
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["redr.me", ] # Change this for deployment
 
SESSION_COOKIE_DOMAIN = 'redr.me' # Change this for Deployment
SESSION_COOKIE_SECURE = True

LOGIN_REDIRECT_URL = "https://app.redr.me"
PORTAL_URL = "https://app.redr.me"
