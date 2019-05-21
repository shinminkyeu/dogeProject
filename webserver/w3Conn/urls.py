from django.urls import path

from . import views

app_name = 'w3Conn'
urlpatterns = [
    path('', views.index, name = 'test')
]
