from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    status_choices = [("in process","в процесі"),("completed","виконано"),("delayed","відкладено")]
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=status_choices,default="in progress")
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title