from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'submission_app'

class Index(TemplateView):
    template_name = 'submission_app/index.html'

