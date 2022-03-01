
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from .models import User, StudChoice
from django.core.exceptions import ValidationError
import re 
EMAIL_REGEX = r'\w+@usf\.edu'

def email_valid(value):
    if value and not re.match(EMAIL_REGEX, value):
        raise forms.ValidationError("Must use .usf.edu email")
    return value

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, validators=[email_valid])
    class Meta:
        model = User
        fields = ('username', 'password1','password2', 'uID', 'email')

class StudChoiceForm(forms.Form):
    class Meta:
        model = StudChoice
        fields = ['section', 'uID']