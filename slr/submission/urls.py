from submission import views
from django.urls import path

app_name = 'submission'

urlpatterns = [
    path('',views.home.as_view(),name='home'),
]