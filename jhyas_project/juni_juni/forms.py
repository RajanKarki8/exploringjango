from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Poet
from django.forms import ModelForm
class UserCanAddmoreField(UserCreationForm):
    email = forms.EmailField(required=True)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
    
class UpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']
        

        