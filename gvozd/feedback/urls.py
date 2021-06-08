from django.urls import path
from . import views


urlpatterns = [
    path('', views.forum),
    path('show/<int:favour_id>/', views.favour_id, name='show')
]