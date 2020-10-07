from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'temp'


class IndexView(TemplateView):
    template_name = 'temp/index.html'

