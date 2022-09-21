from django.db import models


class Problem(models.Model):
    title = models.CharField(150)
    question = models.TextField()
    solution = models.TextField()
    author = models.CharField(200)
    
