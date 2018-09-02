from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View


def kirr_redirect_view(req, *args, **kwargs):
    return HttpResponse('Hello world!')


class KirrCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world from class')
