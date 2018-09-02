from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404
from .models import KirrURL


def kirr_redirect_view(req, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)


class KirrCBView(View):
    def get(self, req, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect('Hello {sc}!'.format(sc=obj.url))
