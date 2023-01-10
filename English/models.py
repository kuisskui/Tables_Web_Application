from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    word = models.CharField(max_length=50)
    word_class = models.CharField(max_length=50)