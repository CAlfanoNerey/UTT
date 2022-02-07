from django.shortcuts import render, redirect
from .models import courseCat
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def indexView(request):
    coursesView = courseCat.objects.all()

    return render(request, 'index.html', {'course':coursesView})

def signUpView(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', {'form': form})

    