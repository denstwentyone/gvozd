from django.urls import path
from . import views


urlpatterns = [
    path('', views.getform),
    path('showorders', views.apps_info)
]