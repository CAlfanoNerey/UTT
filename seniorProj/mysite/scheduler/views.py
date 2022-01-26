from django.shortcuts import render
from .models import courseCat
# Create your views here.

def indexView(request):
    coursesView = courseCat.objects.all()

    return render(request, 'index.html', {'course':coursesView})