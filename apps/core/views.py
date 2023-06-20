from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.conf import settings

from .models import Link

class HomeView(View):

    def get(self, *args, **kwargs):
        return redirect(settings.FRONTEND_URL, permanent=False)

class RedirectCodeView(View):

    def get(self, *args, **kwargs):

        instance = get_object_or_404(Link, code=self.kwargs['code'])
        instance.add_hit()

        return redirect(instance.target_url, permanent=False)
