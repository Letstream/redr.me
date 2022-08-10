import uuid
import random
import string

from django.db import models
from django.db.models import F

class TimestampModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class HitsMixin(models.Model):
    
    hits = models.BigIntegerField(default=0)

    class Meta:
        abstract = True
    
    def add_hit(self):
        self.hits = F('hits') + 1
        self.save(update_fields=['hits', ])

class Link(TimestampModel, HitsMixin):

    DEFAULT_CODE_LENGTH = 6
    
    id = models.BigAutoField(primary_key=True)

    code = models.CharField(max_length=10, unique=True, db_index=True)
    target_url = models.URLField(max_length=2000)

    user_email = models.EmailField(null=True)
    token = models.UUIDField(default=uuid.uuid4)
    
    def save(self, *args, **kwargs):

        if not self.code:
            self.generate_code(save=False)

        super().save(*args, **kwargs)
    
    def generate_code(self, save=True):
        code = None
        while code == None:
            code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(self.DEFAULT_CODE_LENGTH))
            if self.__class__.objects.filter(code=code).exists():
                code = None
        
        self.code = code
        if save:
            self.save(update_fields=['code', ])
        