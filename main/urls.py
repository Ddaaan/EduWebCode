from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main_index),
    path('post/', views.post, name='post'),
    path('about1/', views.about1, name='about1'),
    path('about2/', views.about2, name='about2'),
    path('file/', views.file, name='file'),
    path('admin/', views.admin, name='admin'),
    path('select-info/', views.info_page, name='select-info'),
    path('get-school-names/', views.get_school_names, name='get_school_names'),
    
    path('ele-student-survey/', views.ele_stuSur_question, name='ele-student-s'),
    path('mid-student-survey/', views.midHigh_stuSur_question, name='mid-student-s'),
    path('high-student-survey/', views.midHigh_stuSur_question, name='high-student-s'),
    path('kinder-parents-survey/', views.kinder_parSur_question, name='kinder-parents-s'),
    path('school-parents-survey/', views.school_parSur_question, name='school-parents-s'), 
    path('kinder-teacher-survey/', views.kinder_teaSur_question, name='kinder-teacher-s'),
    path('school-teacher-survey/', views.school_teaSur_question, name='school-teacher-s'),  
]