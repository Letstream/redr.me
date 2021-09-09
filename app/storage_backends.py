from django.conf import settings
from django.core.files.storage import default_storage
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION

    def __init__(self, *args, **kwargs):
        
        super().__init__(
            access_key=settings.AWS_S3_STATIC_ACCESS_KEY_ID,
            secret_key=settings.AWS_S3_STATIC_SECRET_ACCESS_KEY,
            bucket_name=settings.AWS_STATIC_STORAGE_BUCKET_NAME,
            gzip=True,
            default_acl='public-read'
        )

class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    default_acl = 'public-read'
    file_overwrite = False

class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False

private_storage = default_storage if settings.DEBUG else PrivateMediaStorage()
