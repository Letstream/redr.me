from django.core.cache import cache
from django.db.models import Count, Sum
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Link
from .serializers import (
    LinkSerializer,
    LinkPublicSerializer,
    LinkEditSerializer
)

class HttpRequestContextMixin:

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

class LinkCreateAPIView(generics.CreateAPIView, HttpRequestContextMixin):

    model = Link
    serializer_class = LinkSerializer
    permission_classes = [AllowAny, ]

class LinkRetrieveAPIView(generics.RetrieveAPIView, HttpRequestContextMixin):

    model = Link
    serializer_class = LinkPublicSerializer
    queryset = model.objects.all()
    permission_classes = [AllowAny, ]

    def get_object(self):
        try:
            self.get_queryset().get(code=self.kwargs['code'])
        except self.model.DoesNotExist:
            raise NotFound()

class LinkRetrieveEditAPIView(generics.RetrieveUpdateAPIView):

    model = Link
    queryset = model.objects.all()
    serializer_class = LinkEditSerializer
    lookup_field = 'token'
    permission_classes = [AllowAny, ]

class StatsView(APIView):
    
    permission_classes = [AllowAny, ]

    def get(self, *args, **kwargs):

        stats = cache.get('stats')

        if not stats:
            stats = Link.objects.aggregate(total_redirects=Sum('hits'), total_urls=Count('id'))

            # Cache stats for an hour
            cache.set('stats', stats, timeout=3600)
        
        return Response(stats)
