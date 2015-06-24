from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length = 500)

class Answer(models.Model):


