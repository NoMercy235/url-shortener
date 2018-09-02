from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render
from .models import KirrURL
from .forms import SubmitURLForm


class HomeView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'shortener/home.html', self.get_context(SubmitURLForm()))

    def post(self, req, *args, **kwargs):
        form = SubmitURLForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(req, 'shortener/home.html', self.get_context(form))

    def get_context(self, form):
        return {
            'title': 'Hello world!',
            'form': form,
        }


class KirrCBView(View):
    def get(self, req, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect('Hello {sc}!'.format(sc=obj.url))
