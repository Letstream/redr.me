from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View, generic

from .models import Link

class HomeView(generic.TemplateView):
    
    template_name = "core/index.html"


class RedirectCodeView(View):

    def get(self, *args, **kwargs):

        instance = get_object_or_404(Link, code=self.kwargs['code'])
        instance.add_hit()

        return redirect(instance.target_url, permanent=False)


class DashboardView(generic.TemplateView):

    template_name = "core/dashboard.html"

    def get(self, request, token, *args):
        try:
            instance = Link.objects.filter(token=token)
            print(instance)
        except:
            return HttpResponseNotFound('<h1>Token not found</h1>')
        else:
            context = {'data': instance}
            return render(self.request, self.template_name, context)