
from django.db import models
from django.forms import CharField
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser


class courseCat(models.Model):
    classtitle = models.CharField(max_length=200)
    classTime = models.CharField(max_length=200)
    def __str__(self):
        return self.classtitle
# Create your models here.

# class CRN(model.Model):
#     crn = models.IntegerField()
#     def __str__(self):
#         return self.crn


class Classes(models.Model):
    crn = models.IntegerField()
    def __str__(self):
        return str(self.crn)

class Subject (models.Model):
    crn = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subj = models.CharField(max_length=50)
    def __str__(self):
        return str(self.subj)

class CourseNumb (models.Model):
    subj = models.ForeignKey(Subject, on_delete=models.CASCADE)
    courseNumb = models.IntegerField()
    def __str__(self):
        return str(str(self.subj) + " " +str(self.courseNumb))

class Section (models.Model):
    courseNumb = models.ForeignKey(CourseNumb, on_delete=models.CASCADE)
    section = models.IntegerField()
    title = models.CharField(max_length=200)
    max = models.IntegerField()
    seatsTaken = models.IntegerField(default=0)
    days = models.CharField(max_length=7)
    time = models.TimeField()
    duration = models.TimeField()
    instructor = models.CharField(max_length=50)
    addInfo = models.TextField(max_length=500)
    def __str__(self):
        return str(self.courseNumb)

    

class User(AbstractUser):
    uID = models.CharField(max_length=50)
    def __str__(self):
        return str(self.uID)


class StudChoice(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="crnLookOf")
    uID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     uID= models.CharField(max_length=200, default='')
#     firstName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)

#     def __str__(self):
#         return self.uID

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# class Student(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)



