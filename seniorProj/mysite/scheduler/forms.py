
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from .models import User, StudChoice



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1','password2', 'uID')


class StudChoiceForm(forms.Form):
    class Meta:
        model = StudChoice
        fields = ['section', 'uID']