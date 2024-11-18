from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Users.models import CustomUser

def userregister(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,phone=n,address=a,is_user=True)
            u.save()
            return redirect('Books:home')
        else:
            return HttpResponse("Passwords are not same")
    return render(request, 'userregister.html')


def adminregister(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,phone=n,address=a,is_superuser=True)
            u.save()
            return redirect('Books:home')
        else:
            return HttpResponse("Passwords are not same")
    return render(request, 'adminregister.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user and user.is_superuser==True:
            login(request,user)
            return redirect('Books:home')
        elif user and user.is_user==True:
            login(request,user)
            return redirect('Books:home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('Users:login')




