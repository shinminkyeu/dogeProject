from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.show_img),
    path('register/', views.register),
]