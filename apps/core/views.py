from django.shortcuts import get_object_or_404, redirect
from django.views import View, generic

from .models import Link

class HomeView(generic.TemplateView):
    
    template_name = "core/index.html"


class RedirectCodeView(View):

    def get(self, *args, **kwargs):

        instance = get_object_or_404(Link, code=self.kwargs['code'])
        instance.add_hit()

        return redirect(instance.target_url, permanent=False)
