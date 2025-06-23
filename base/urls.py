# base/urls.py
from django.urls import path
from . import views

app_name = 'base' 

urlpatterns = [
    path('', views.base, name='index'), 
    path('messages/', views.message_list, name='message_list'),
    path('admin-links/', views.admin-links, name='admin_links'),
    path('about_us/', views.about_us, name='about_us'),
]