from django.contrib import admin

from .models import Classes, StudChoice, courseCat, User
# Register your models here.


admin.site.register(courseCat)
admin.site.register(Classes)
admin.site.register(User)
admin.site.register(StudChoice)