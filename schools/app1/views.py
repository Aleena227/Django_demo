from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from app1.models import School,Student
# Create your views here.


from django.urls import reverse_lazy
from app1.forms import SchoolForm,StudentForm,RegisterForm




class home(TemplateView):
    template_name='home.html'


class addschool(CreateView):
    model=School
    form_class = SchoolForm
    template_name = 'addschool.html'
    success_url = reverse_lazy('home')

class addstudent(CreateView):
    model=Student
    form_class = StudentForm
    template_name = 'addstudent.html'
    success_url = reverse_lazy('home')

class schoollist(ListView):
    model=School
    context_object_name = 'school'
    template_name = 'schoollist.html'

class schooldetail(DetailView):
    model=School
    context_object_name = 'school'
    template_name = 'detail.html'


class register(CreateView):
    model=User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form): #in CreateView after validation it will call form_valid() function to save the data
        f=form.save(commit=False) #in our class we redefine the form_valid. so after validation it will form_valid inside our function
        password=form.cleaned_data['password'] #here we access the password from the cleaned_data
        f.set_password(password) #To change into encrypted format we use set_password
        f.save() #then it will save the form object into table User
        return super().form_valid(form) #inorder to redirect into home page we call super().form_valid()

class Userlogin(LoginView):
    template_name = 'login.html'

class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('home')