from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.
class Question(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_image = models.ImageField(upload_to='question_pics', blank= True, null= True)


class Answers(models.Model):
    answer = models.TextField(max_length=1000)
    answer_time = models.DateTimeField(auto_now=True)
    question_id = models.OneToOneField(Question, on_delete=models.CASCADE, primary_key = True)
    acc_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Account.id+')

    def __str__(self):
        return self.question_id
    
    def __str__(self):
        return self.answer
  