from django.contrib import admin
from django.urls import path
from . import views


# url path to the home page
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('logout', views.logoutUser, name='logout'),

    path('', views.loginPage, name='login'),
    path('home', views.home, name='home'),
    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('create-room/', views.createRoom, name="create-room"),
    path('create-topic', views.createTopic, name="create-topic"),

    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    
    path('update-user/<str:pk>/', views.updateUser, name="update-user"),
]
