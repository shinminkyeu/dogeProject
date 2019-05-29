from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.info, name = 'info'),
    path('update', views.update, name = 'update'),
    path('join', views.join, name = 'join'),
    path('logout', views.logout, name = 'logout')
]