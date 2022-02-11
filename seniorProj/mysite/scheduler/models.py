
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
    crn = models.IntegerField
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


class User(AbstractUser):
    uID = models.CharField(max_length=50)


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


# class StudChoice(models.Model):
    # crn = models.ForeignKey(Classes, on_delete=models.CASCADE)
    # uID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
