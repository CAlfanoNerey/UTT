from ast import Sub
from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(Classes)
admin.site.register(Subject)
admin.site.register(CourseNumb)
admin.site.register(Section)
admin.site.register(User)
admin.site.register(StudChoice)