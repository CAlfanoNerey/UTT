from django.shortcuts import render, redirect
from .models import courseCat
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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

def loginView(request):
    if request.method == "POST":

        context = {}
        form = AuthenticationForm(None, request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            ...
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form}, )