from django.contrib import admin

from .models import Classes, courseCat, User
# Register your models here.


admin.site.register(courseCat)
admin.site.register(Classes)
admin.site.register(User)