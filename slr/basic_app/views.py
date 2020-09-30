#from django.shortcuts import render

from django.views.generic import TemplateView

app_name = 'basic_app'


class base_view(TemplateView):
    template_name = 'basic_app/base.html'


class contact_view(TemplateView):
    template_name = 'basic_app/contact.html'


class about_view(TemplateView):
    template_name = 'basic_app/about.html'
