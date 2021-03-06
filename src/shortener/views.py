from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render
from .models import KirrURL
from .forms import SubmitURLForm
from analytics.models import ClickEvent


class HomeView(View):
    def get(self, req, *args, **kwargs):
        return render(req, 'shortener/home.html', self.get_context(SubmitURLForm()))

    def post(self, req, *args, **kwargs):
        form = SubmitURLForm(req.POST)
        template = 'shortener/home.html'
        context = self.get_context(form)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url=url)
            context = {
                'object': obj,
                'created': created,
            }
            template = 'shortener/success.html' if created else 'shortener/already-exists.html'

        return render(req, template, context)

    def get_context(self, form):
        return {
            'title': 'Kirr.co - URL shortener',
            'form': form,
        }


class URLRedirectView(View):
    def get(self, req, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
        print(obj.url)
        return HttpResponseRedirect(obj.url)
