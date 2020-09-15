from submission_app import views
from django.urls import path

app_name = 'submission_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
