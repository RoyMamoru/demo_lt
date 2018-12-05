from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('input', views.input, name='input'),
    path('input_form', views.input_form, name='input_form'),
    path('result', views.result, name='result')
]
