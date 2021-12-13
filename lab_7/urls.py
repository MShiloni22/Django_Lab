from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_7, name='lab_7'),
    path('input_processor', views.input_processor, name='input_processor')
]
