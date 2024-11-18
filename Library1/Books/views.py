from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'home.html')

from Books.models import Book

@login_required
def viewbooks(request):
    #k=con.execute('select * from Book')
    #k=modelname.objects.all()
    k=Book.objects.all()
    context={'Book':k}
    return render(request, 'viewbooks.html',context)

@login_required
def addbooks(request):
    if(request.method=="POST"):
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        pa = request.POST['pa']
        l = request.POST['l']
        c = request.FILES['c']
        pd = request.FILES['pd']
        b=Book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=c,pdf=pd)
        b.save()
        return viewbooks(request)

    return render(request, 'addbooks.html')

@login_required
def viewdetails(request,p):
    k=Book.objects.get(id=p)
    context={'book':k}
    return render(request, 'viewdetails.html',context)


@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return redirect('Books:viewbooks')


@login_required
def edit(request,p):
    k=Book.objects.get(id=p)
    if (request.method == "POST"):
        k.title = request.POST['t']
        k.author = request.POST['a']
        k.price = request.POST['p']
        k.pages = request.POST['pa']
        k.language = request.POST['l']
        if (request.FILES.get('c') == None):
            k.save()
        else:
            k.cover = request.FILES.get('c')
        if (request.FILES.get('pd') == None):
            k.save()
        else:
            k.pdf = request.FILES.get('pd')
        k.save()
        return redirect('Books:viewbooks')

    context={'book':k}
    return render(request,'edit.html',context)