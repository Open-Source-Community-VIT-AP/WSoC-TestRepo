from django.shortcuts import render
from django.views.generic import TemplateView
app_name='new_app'
class home(TemplateView):
    # render(request,'home.html')
    template_name='new_app/home.html'
# Create your views here.
