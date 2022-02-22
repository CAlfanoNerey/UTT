from ast import Sub
from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(StudChoice)
admin.site.register(fullClass)