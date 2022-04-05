from enum import unique
from multiprocessing import context
from operator import itemgetter
from secrets import choice
from django.shortcuts import render, redirect


from .forms import SignUpForm
from .models import  StudChoice, User, fullClass
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import itertools 
from itertools import chain


def indexView(request):
    if request.user.is_authenticated:
        return redirect('choice')
    else:    
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
        if 'selectMult' in request.POST:
            crn= request.POST.getlist('selectMult')
            for x in crn:
                sectionChoice = fullClass.objects.get(crn = x)
                courseNumbSubj = (str(sectionChoice.subj) + " " + str(sectionChoice.courseNumb))
                ret = StudChoice.objects.create(section=sectionChoice,courseSubjNum=courseNumbSubj, uID=request.user )

        
        if 'flag' in request.POST:
            crn= request.POST['flag']
            sectionChoice = fullClass.objects.get(crn = crn)
            ret = StudChoice.objects.create(section=sectionChoice, uID=request.user )
        
        if 'crnAdded' in request.POST:
            delChoice = request.POST.getlist('crnAdded')
            for x in delChoice:
                delChoiceObj = fullClass.objects.get(crn = x)
                print(str(delChoice) + " " + str(student.uID))
            # print(str(StudChoice.objects.get(section = delChoiceObj, uID = request.user)))
                delObj = StudChoice.objects.filter(section = delChoiceObj, uID = request.user).delete()
        if 'gensched' in request.POST:
             #Algorithm

            coursenumDict = {}
            crnlist = []
            dist = classes.order_by().values('courseSubjNum').distinct()
            print("distinct" + str(dist))



            for courseandnum in dist:
                courseval= courseandnum.get('courseSubjNum')
                split = courseval.split(' ')
                # print("subj " + str(subj[0]) + " numb " + str(subj[1]))
                subject = split[0]
                classnum = int(split[1]) 
                # print("subj " + subj + " numb " + classnum)
                classfilter = fullClass.objects.filter(subj=subject, courseNumb=classnum)
                coursenumDict[courseval]= None
            
                for y in classfilter:
                    crnlist.append(y.crn)
                
                coursenumDict[courseval]=crnlist
                crnlist = []
                # print(str(classfilter.crn))
                # print(x.get('courseSubjNum'))

            print(coursenumDict)

            # print("******ClassLIst******")
            # print(classlist)
            #cartesian product of dictionaries
            keys = coursenumDict.keys()
            values = coursenumDict.values()

            daydict = {}
            conflictdays = {}
            noconflict={}
            finalschedule={}
            schedulecount = 0
            for instance in itertools.product(*values):
                # Instance = Cartesian product ^^
                print(dict(zip(keys, instance)))
                print(instance)
                for crn in instance:
                    currclass = fullClass.objects.get(crn= crn)
                    daydict[currclass.crn] = currclass.days + str(currclass.time) + " "+ str(currclass.duration)
                print("daydict "+str(daydict))
                
                # merges if conflict
                for key, value in daydict.items():
                    if value not in conflictdays:
                        conflictdays[value] = [key]
                    else:
                        conflictdays[value].append(key)

                for key in conflictdays:
                    value = conflictdays[key]
                    #if more conflict in key
                   
                    if (len(value) > 1):
                        
                        noconflict[str(value)] = 'conflict' 
                    else:
                        noconflict[str(value)] =key

                for key in noconflict:
                    value = noconflict[key]
                    if noconflict[key] == "conflict" :
                        noconflict.clear()
                        break

                finalschedule[schedulecount] = []
                for key in noconflict:
                    #get data and clean it
                    key = str(key)
                    key = key.replace("'","")
                    key = key.replace("[","")
                    key = key.replace("]","")
                    value = key
                    
                    #append to the final schedule with no conflicts
                    finalschedule[schedulecount].append(value)

                schedulecount += 1

                print("THIS IS IT" + str(noconflict))
                print("final schedule no conflict " + str(finalschedule))
                print()
                
                daydict.clear()
                conflictdays.clear()
                noconflict.clear()
                
                
            
        

    # Loads all available courses distinct
    courses = fullClass.objects.order_by().values('subj').distinct()
    
    #loads all available courses not distinct
    fullList = fullClass.objects.all()


    context= {
        'classes' : classes,
        'student' : student,
        'courseList':courses,
        'fullList': fullList
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