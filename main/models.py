from django.db import models

# Create your models here.
class Response(models.Model):
    question_id = models.IntegerField()
    text_ans = models.TextField(blank=True, null=True)
    score_ans = models.IntegerField(blank=True, null=False)
    
    def __str__(self):
        return f"질문에 답변하세요 {self.question_id}"