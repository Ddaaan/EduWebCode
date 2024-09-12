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
    #학교별 통계
    path('statistics-student-form/', views.school_student_statistics, name='statistics_student_form'),  # 학생용 통계 결과 페이지
    path('statistics-parents-form/', views.school_parents_statistics, name='statistics_parents_form'),   # 학부모용 통계 결과 페이지
    path('statistics-teacher-form/', views.school_teacher_statistics, name='statistics_teacher_form'),  # 교사용 통계 결과 페이지
    path('statistics-admin/eachSchool/', views.statistics_admin_page, name='statistics_admin_page'), #전체 관리자 정보 선택 페이지 (최종)
    
    #지역별 통계
    path('statistics-region-student-form/', views.region_student_statistics, name='statistics_region_student_form'),  # 학생용 통계 결과 페이지
    path('statistics-region-parents-form/', views.region_parents_statistics, name='statistics_region_parents_form'),   # 학부모용 통계 결과 페이지
    path('statistics-region-teacher-form/', views.region_teacher_statistics, name='statistics_region_teacher_form'),  # 교사용 통계 결과 페이지
    path('statistics-admin/region/', views.statistics_admin_region_page, name='statistics_admin_region_page'), #지역별 통계 페이지 (최종)
    
    #학교급별 통계
    path('statistics-total-student-form/', views.total_student_statistics, name='statistics_total_student_form'),  # 학생용 통계 결과 페이지
    path('statistics-total-parents-form/', views.total_parents_statistics, name='statistics_total_parents_form'),   # 학부모용 통계 결과 페이지
    path('statistics-total-teacher-form/', views.total_teacher_statistics, name='statistics_total_teacher_form'),  # 교사용 통계 결과 페이지
    path('statistics-admin/total/', views.statistics_admin_total_page, name='statistics_admin_total_page'), #지역별 통계 페이지 (최종)

]

#미디어 파일 다운로드
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)