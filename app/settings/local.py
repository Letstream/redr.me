from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

STATIC_ROOT = env('STATIC_ROOT')
STATIC_URL = '/static/'

MEDIA_ROOT = env('UPLOAD_ROOT')
MEDIA_URL = '/uploads/'

USE_AWS = False
AWS_STATIC_LOCATION = None
AWS_PUBLIC_MEDIA_LOCATION = None
AWS_PRIVATE_MEDIA_LOCATION = None

INTERNAL_IPS = ['127.0.0.1', 'localhost']

SESSION_COOKIE_DOMAIN = 'localhost'
SESSION_COOKIE_SECURE = False

CSRF_COOKIE_DOMAIN = 'localhost'
CSRF_COOKIE_SECURE = False

LOGIN_REDIRECT_URL = "/dashboard/"
PORTAL_URL = "/dashboard/"
