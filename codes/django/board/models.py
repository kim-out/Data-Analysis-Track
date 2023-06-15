from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 모델 변경 시: makemigrations와 migrate를 통해 데이터베이스 변경
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(null=True, blank=True)

    
    