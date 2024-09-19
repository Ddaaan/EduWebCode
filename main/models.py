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
    
    def __str__(self):
        return self.school_name

#공지사항 데이터베이스
class Post(models.Model):
    title = models.CharField(max_length=200) #제목
    content = models.TextField() #내용
    created_at = models.DateTimeField(default=timezone.now) #작성일
    views = models.IntegerField(default=0) #조회수
    file = models.FileField(upload_to='uploads/', blank=True, null=True) #첨부파일
    
    def __str__(self):
        return self.title
    
class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    viewed_at = models.DateTimeField(auto_now_add=True)
    
#자료실 데이터베이스
class File(models.Model):
    title = models.CharField(max_length=200) #제목
    content = models.TextField() #내용
    created_at = models.DateTimeField(default=timezone.now) #작성일
    views = models.IntegerField(default=0) #조회수
    file = models.FileField(upload_to='uploads/', blank=True, null=True) #첨부파일
    
    def __str__(self):
        return self.title
    
class FileView(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)  # File 모델과 연결
    ip_address = models.GenericIPAddressField()  # IP 주소 필드
    viewed_at = models.DateTimeField(auto_now_add=True)  # 조회 시각