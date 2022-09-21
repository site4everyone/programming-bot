from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=150)
    question = models.TextField()
    solution = models.TextField()
    author = models.CharField(max_length=200)
    
