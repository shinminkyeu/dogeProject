from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.verify, name = 'verify'),
    path('update/', views.update, name = 'update'),
    path('join/', views.join, name = 'join'),
    path('logout/', views.logout, name = 'logout'),
    path('<user_addr>/', views.info, name = 'info')
]