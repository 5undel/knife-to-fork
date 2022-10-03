from django.contrib import admin
from django.urls import path
from . import views


# url path to the home page
urlpatterns = [
    path('', views.index, name='startpage'),
    path('home', views.home, name='home'),
    path('room/<str:pk>/', views.room, name="room"),
]
