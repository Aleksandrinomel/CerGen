from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'get_serial_number/', views.get_serial_number, name='get_serial_number'),
    path(r'get_test_points/', views.get_test_points, name='get_test_points'),
    path(r'template/', views.template, name='template'),
]