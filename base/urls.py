from django.contrib import admin
from django.urls import path
from . import views


# url path to the home page
urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('home', views.home, name='home'),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]
