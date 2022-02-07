from django.db import models
from django.forms import CharField


class courseCat(models.Model):
    classtitle = models.CharField(max_length=200)
    classTime = models.CharField(max_length=200)
    def __str__(self):
        return self.place
# Create your models here.
