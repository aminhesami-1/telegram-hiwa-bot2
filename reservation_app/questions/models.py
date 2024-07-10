from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    answer = models.TextField()
    active = models.BooleanField(default=False)
