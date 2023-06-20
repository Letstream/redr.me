from django.http import HttpRequest
from rest_framework import serializers

from .models import Link

class PublicURLMixin:

    def get_public_url(self, obj):
        if not self.context.get('request'):
            return None
        
        request: HttpRequest = self.context['request']

        return "https://%s/%s/" % (
            request.get_host(),
            obj.code
        )

class LinkSerializer(serializers.ModelSerializer, PublicURLMixin):

    public_url = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = [
            'code', 'target_url', 'token', 'user_email',
            'created_on', 'modified_on', 'hits', 'public_url'
        ]
        read_only_fields = [
            'created_on', 'modified_on', 'code', 'hits', 
            'token'
        ]
    
class LinkPublicSerializer(serializers.ModelSerializer, PublicURLMixin):

    public_url = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = [
            'target_url', 'hits', 'public_url'
        ]
        read_only_fields = [
            'target_url', 'hits'
        ]

class LinkEditSerializer(serializers.ModelSerializer, PublicURLMixin):

    public_url = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = [
            'target_url',
            'code',
            'hits',
            'created_on', 
            'public_url'
        ]
        read_only_fields = [
            'code',
            'hits',
            'created_on', 
            'public_url'
        ]
