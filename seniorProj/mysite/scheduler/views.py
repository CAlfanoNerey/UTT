from enum import unique
from multiprocessing import context
from operator import itemgetter
from django.shortcuts import render, redirect


from .forms import SignUpForm
from .models import  StudChoice, User, fullClass
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



def indexView(request):
    context={

    }

    return render(request, 'index.html', {'course':context})

def signUpView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        uID = form.cleaned_data.get('uID')
        email = form.cleaned_data.get('email')
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

def fkView(request):
    current_user = request.user
    student = User.objects.get(id=current_user.id) 
    #Filtering by the classes chosen by UID of user
    crnChosen = StudChoice.objects.all()
    classes = crnChosen.filter(uID=current_user.id)


    if request.method == "POST":
        crn= request.POST['flag']
        sectionChoice = fullClass.objects.get(crn = crn)
        ret = StudChoice.objects.create(section=sectionChoice, uID=request.user )
        
 
    # Loads all available courses
    courses = fullClass.objects.order_by().values('subj').distinct()
      

    context= {
        'classes' : classes,
        'student' : student,
        'courseList':courses
    }


    return render(request, 'addCourse.html', context)

def courseNumbDropdown(request):
    subj = request.GET.get('subj')
    form = fullClass.objects.filter(subj = subj)
    context = {
        'form' : form
    }
    return render(request, "partials/courseNumb.html", context)

def courseDisplay(request):
    coursenum = request.GET.get('section')
    print(coursenum)
    form = fullClass.objects.filter(courseNumb = coursenum)

    context = {
        'form' : form,

    }
    return render(request, 'partials/courseDisplay.html', context)