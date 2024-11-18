from django.shortcuts import render,redirect

# Create your views here.
from app1.models import Movie
def home1(request):
    m=Movie.objects.all()
    context={'movie':m}
    return render(request, 'home1.html',context)
def addmovie(request):
    if (request.method == "POST"):
        t = request.POST['t']
        d = request.POST['d']
        l = request.POST['l']
        y = request.POST['y']
        i = request.FILES['i']
        m = Movie.objects.create(title=t, description=d, language=l, year=y, image=i)
        m.save()
        return redirect('home1')


    return render(request, 'addmovie.html')

def details(request,p):
    m=Movie.objects.get(id=p)
    context={'Movie':m}
    return render(request, 'details.html',context)

def delete(request,p):
    k=Movie.objects.get(id=p)
    k.delete()
    return redirect('home1')

def edit(request,p):
    k=Movie.objects.get(id=p)
    if (request.method == "POST"):
        k.title = request.POST['t']
        k.language = request.POST['l']
        k.description = request.POST['d']
        k.year = request.POST['y']
        if (request.FILES.get('i') == None):
            k.save()
        else:
            k.image = request.FILES.get('i')
        k.save()
        return redirect('details',p)

    context={'Movie':k}
    return render(request,'edit.html',context)