from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.blogpage, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
]