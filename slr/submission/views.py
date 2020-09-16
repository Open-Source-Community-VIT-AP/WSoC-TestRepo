from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'submission'
class home(TemplateView):
    template_name = 'submission/home.html'