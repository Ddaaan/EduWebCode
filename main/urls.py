from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', views.main_index),
    path('about1/', views.about1, name='about1'),
    path('about2/', views.about2, name='about2'),
    path('file/', views.file, name='file'),
    path('admin/', views.admin, name='admin'),
    path('select-info/', views.info_page, name='select-info'),
    path('get-school-names/', views.get_school_names, name='get_school_names'),
    
    #설문조사 페이지 이동 url
    path('ele-student-survey/', views.ele_stuSur_question, name='ele-student-s'),
    path('midhigh-student-survey/', views.midHigh_stuSur_question, name='midhigh-student-s'),
    path('kinder-parents-survey/', views.kinder_parSur_question, name='kinder-parents-s'),
    path('school-parents-survey/', views.school_parSur_question, name='school-parents-s'), 
    path('kinder-teacher-survey/', views.kinder_teaSur_question, name='kinder-teacher-s'),
    path('school-teacher-survey/', views.school_teaSur_question, name='school-teacher-s'),  
    path('survey-complete/', views.survey_complete, name='survey_complete'),
    path('submit-survey/', views.handle_survey_response, name='handle_survey_response'), #조사 제출
    
    #공지사항 url
    path('post/', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'), 
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    
    #설문조사 결과 url
    path('statistics-admin/', views.school_statistics, name='statistics_admin'), #전체 관리자 정보 선택 페이지
    path('statistics-admin-temp/', views.school_statistics, name='statistics_admin_temp'), #전체 관리자 결과페이지
]

#미디어 파일 다운로드
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)