from django.contrib import admin

from .models import Classes, courseCat 
# Register your models here.
admin.site.register(courseCat)
admin.site.register(Classes)