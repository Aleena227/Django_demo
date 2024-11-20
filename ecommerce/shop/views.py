from django.shortcuts import render,redirect
# Create your views here.
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def categories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'categories.html',context)

def products(request,p):
    c = Category.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context = {'cat': c,'product':p}
    return render(request, 'products.html', context)


def details(request,p):
    pro=Product.objects.get(id=p)
    context={'product':pro}
    return render(request,'details.html',context)

def register(request):
    if(request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('shop:login')
        else:
            return HttpResponse("Passwords are not same")
    return render(request, 'register.html')


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:categories')

@login_required
def addcat(request):
    if (request.method == "POST"):
        n = request.POST['n']
        d = request.POST['d']
        i = request.FILES['i']
        m = Category.objects.create(name=n, description=d,image=i)
        m.save()
        return redirect('shop:categories')
    return render(request, 'addcat.html')

@login_required
def addpro(request):
    if (request.method == "POST"):
        n = request.POST['n']
        d = request.POST['d']
        i = request.FILES['i']
        p = request.POST['p']
        s = request.POST['s']
        c = request.POST['c']
        cat=Category.objects.get(name=c)
        m = Product.objects.create(name=n, desc=d,image=i,price=p,stock=s,category=cat)
        m.save()
        return redirect('shop:categories')
    return render(request, 'addpro.html')

def addstock(request,i):
    k = Product.objects.get(id=i)
    if(request.method == "POST"):
        k.stock = request.POST['s']
        k.save()
        return redirect('shop:details',i)

    context = {'product': k}
    return render(request, 'addstock.html',context)


