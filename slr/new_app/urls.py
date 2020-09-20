from django.urls import path
from new_app import views
app_name = 'new_app'
urlpatterns=[
    path('',views.home.as_view(),name='home')
]