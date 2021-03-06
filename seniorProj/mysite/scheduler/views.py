from multiprocessing import context
from operator import itemgetter
from django.shortcuts import render, redirect


from .forms import SignUpForm, ChooseSubjForm, ChooseNumbForm
from .models import CourseNumb, Subject, courseCat, Classes, StudChoice, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your views here.

def indexView(request):
    coursesView = courseCat.objects.all()

    return render(request, 'index.html', {'course':coursesView})

def signUpView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        uID = form.cleaned_data.get('uID')
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
    crnChosen = StudChoice.objects.all()
    classes = crnChosen.filter(uID=current_user.id)

   
    
    context= {
        # 'stuchoice': stuchoice,
        'classes' : classes,
        'crn': crnChosen,
        'student' : student,

    }


    return render(request, 'addCourse.html', context)

def courseNumbDropdown(request):
    subj = request.GET.get('subj')
    print("HERE " +subj)
    form = CourseNumb.objects.filter(subj__id = subj)
    print(form)
    context = {
        'form' : form
    }
    return render(request, "partials/courseNumb.html", context)

