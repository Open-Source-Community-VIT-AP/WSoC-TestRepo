from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('', views.base_view.as_view(), name='base'),
    path('contact/',views.contact_view.as_view(),name='contact'),
    path('about/',views.about_view.as_view(),name='about'),
]
