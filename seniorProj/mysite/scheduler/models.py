from django.db import models
from django.forms import CharField


class courseCat(models.Model):
    classtitle = models.CharField(max_length=200)
    classTime = models.CharField(max_length=200)
    def __str__(self):
        return self.classtitle
# Create your models here.

class Classes(models.Model):
    crn = models.IntegerField()
    subj = models.CharField(max_length=50)
    courseNumb = models.IntegerField()
    title = models.CharField(max_length=200)
    max = models.IntegerField()
    seatsTaken = models.IntegerField(default=0)
    days = models.CharField(max_length=7)
    time = models.TimeField()
    duration = models.TimeField()
    instructor = models.CharField(max_length=50)
    addInfo = models.TextField(max_length=500)
    def __str__(self):
        return self.crn
