
from django.db import models
from django.forms import CharField
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser



class fullClass (models.Model):
    crn = models.IntegerField()
    subj = models.CharField(max_length=50)
    courseNumb = models.IntegerField()
    section = models.IntegerField()
    title = models.CharField(max_length=200)
    max = models.IntegerField()
    seatsTaken = models.IntegerField(default=0)
    days = models.CharField(max_length=7, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True)
    instructor = models.CharField(max_length=50)
    addInfo = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return str(self.crn)



class User(AbstractUser):
    uID = models.CharField(max_length=50)
    def __str__(self):
        return str(self.uID)


class StudChoice(models.Model):
    section = models.ForeignKey(fullClass, on_delete=models.CASCADE, related_name="crnLookOf")
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



