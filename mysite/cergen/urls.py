from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'get_serial_number/', views.get_serial_number, name='get_serial_number'),
    path(r'get_test_points/', views.get_test_points, name='get_test_points'),
    path(r'get_description_procedure/', views.get_description_procedure, name='get_description_procedure'),
    path(r'get_dev_name/', views.get_dev_name, name='get_dev_name'),
    path(r'template/', views.template, name='template'),
]