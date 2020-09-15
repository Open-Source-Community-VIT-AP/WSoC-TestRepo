from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'updated_app'

class AboutView(TemplateView):
    template_name = 'updated_app/about.html'
