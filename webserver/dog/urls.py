from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.findMyDog),
    path('register/', views.register),
]