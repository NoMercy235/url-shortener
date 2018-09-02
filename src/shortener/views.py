from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render
from .models import KirrURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})


class KirrCBView(View):
    def get(self, req, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect('Hello {sc}!'.format(sc=obj.url))
