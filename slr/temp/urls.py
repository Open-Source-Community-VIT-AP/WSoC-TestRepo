from django.urls import path

from . import views
from django.urls import path

app_name = 'temp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

]
'''
    path('frontend/', views.FrontEndView.as_view(), name='frontend'),
    path('backend/', views.BackEndView.as_view(), name='backend'),
    path('frontendsubmission/', views.FrontEndSubmissionView.as_view(), name='frontend_submission'),
    '''