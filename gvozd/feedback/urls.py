from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum),
    path('show',views.show)
]