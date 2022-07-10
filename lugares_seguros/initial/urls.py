from django.urls import path, re_path

from initial import views

urlpatterns = [
    path('', views.HelloDrf.as_view(), name='index')
]