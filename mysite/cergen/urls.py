from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'get_serial_number/', views.get_serial_number, name='get_serial_number'),
]