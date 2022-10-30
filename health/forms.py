from django import forms
from .models import Blog,Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):

    email=forms.EmailField()
    name=forms.CharField()
    password = forms.PasswordInput()

    class Meta:
        model=User
        fields=["name", "password", "email"]

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        
        fields="__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        
        fields="__all__"

