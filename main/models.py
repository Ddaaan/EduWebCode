from django.db import models

# Create your models here.
class Response(models.Model):
    question_id = models.IntegerField()
    text_ans = models.TextField(blank=True, null=True)
    score_ans = models.IntegerField(blank=True, null=False)
    
    def __str__(self):
        return f"질문에 답변하세요 {self.question_id}"
    
    
class School(models.Model):
    education_office = models.CharField(max_length=100) #시도교육청
    school_level = models.CharField(max_length=100) #학교급
    establishment_type = models.CharField(max_length=100) #설립구분
    school_name = models.CharField(max_length=255) #학교명
    district = models.CharField(max_length=100) #자치구
    postal_code = models.CharField(max_length=10) #우편번호
    address = models.CharField(max_length=255) #학교주소
    
    def __str__(self):
        return self.school_name