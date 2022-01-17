from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.practice,{}),
    path('1.html', views.first_practice,{}),
    path('2.html', views.second_practice,{}),
    path('3.html', views.third_practice,{}),
]
