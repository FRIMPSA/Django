from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[

    path('Login/', views.LogInPage, name='Login'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('createRoom/', views.createRoom, name='roomForm'),
    path('updateRoom/<str:pk>/', views.updateRoom, name='update'),
    path('deleteRoom/<str:pk>/', views.deleteRoom, name='delete'),


]