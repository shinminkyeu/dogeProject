from django.urls import path

from . import views

app_name = 'dog'
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('info/', views.info, name = 'info'),
]