from django import forms
from app1.models import School,Student
from django.contrib.auth.models import User


class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields="__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']