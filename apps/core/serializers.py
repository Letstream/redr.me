from rest_framework import serializers

from .models import Link

class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = [
            'code', 'target_url', 'token', 'user_email',
            'created_on', 'modified_on', 'hits'
        ]
        read_only_fields = [
            'created_on', 'modified_on', 'code', 'hits', 
            'token'
        ]
    
class LinkPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = [
            'target_url', 'hits'
        ]
        read_only_fields = [
            'target_url', 'hits'
        ]