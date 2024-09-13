from django.db import models
from django.utils import timezone

# Create your models here.
 
class School(models.Model):
    education_office = models.CharField(max_length=100) #시도교육청
    school_level = models.CharField(max_length=100) #학교급
    establishment_type = models.CharField(max_length=100) #설립구분
    school_name = models.CharField(max_length=255) #학교명
    district = models.CharField(max_length=100) #자치구
    postal_code = models.CharField(max_length=10) #우편번호
    address = models.CharField(max_length=255) #학교주소
    school_id = models.CharField(max_length=100) #각 학교별 아이디
    school_pw = models.CharField(max_length=100) #각 학교별 비밀번호
    
    ROLE_CHOICES = [
        ('본청', '본청 관리자'),
        ('지역청', '지역청 관리자'),
        ('학교', '학교 관리자'),
        ('user', '일반 사용자')  # 일반 사용자 추가
    ]
    
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='user')  # 기본값을 일반 사용자로 설정
    
    def __str__(self):
        return self.school_name

class Post(models.Model):
    title = models.CharField(max_length=200) #제목
    content = models.TextField() #내용
    created_at = models.DateTimeField(default=timezone.now) #작성일
    views = models.IntegerField(default=0) #조회수
    file = models.FileField(upload_to='uploads/', blank=True, null=True) #첨부파일
    
    def __str__(self):
        return self.titile
    
class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    viewed_at = models.DateTimeField(auto_now_add=True)