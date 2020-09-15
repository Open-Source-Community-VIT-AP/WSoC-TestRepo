from updated_app import views
from django.urls import path

app_name = 'updated_app'

urlpatterns = [
    path('about/',views.AboutView.as_view(), name = 'about'),
]
