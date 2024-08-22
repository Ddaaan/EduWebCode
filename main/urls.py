from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main_index),
    path('post/', views.post, name='post'),
    path('about1/', views.about1, name='about1'),
    path('about2/', views.about2, name='about2'),
    path('file/', views.file, name='file'),
    path('admin/', views.admin, name='admin'),
]