from django.db import models


class Problem(models.Model):
    question = models.TextField()
    solution = models.TextField()
