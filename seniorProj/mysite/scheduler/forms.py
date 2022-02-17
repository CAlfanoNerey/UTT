
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from .models import User, Classes, Subject, CourseNumb, StudChoice



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1','password2', 'uID')

class ChooseSubjForm(forms.Form):
    # subj = forms.ModelChoiceField(queryset=Subject.objects.all().order_by('subj'))
    class Meta:
        model = Subject
        fields = "subj"

class StudChoiceForm(forms.Form):
    class Meta:
        model = StudChoice
        fields = ['section', 'uID']
class ChooseNumbForm(forms.Form):
    # crn = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('crn'))
    # subj = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('subj'))
    courseNumb = forms.ModelChoiceField(queryset=CourseNumb.objects.all().order_by('courseNumb'))

    class Meta:
        model = Classes
        fields = 'courseNumb'