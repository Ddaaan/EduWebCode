from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main_index),
    path('post/', views.post, name='post'),
]