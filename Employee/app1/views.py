from django.shortcuts import render,redirect
from app1.models import employee
# Create your views here.
def home(request):
    return render(request, 'home.html')

def viewemployee(request):
    k = employee.objects.all()
    context = {'employee': k}
    return render(request, 'viewemployee.html', context)
def addemployee(request):
    if (request.method == "POST"):
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        g = request.POST['g']
        p = request.POST['p']
        d = request.POST['d']
        i = request.FILES['i']
        k = employee.objects.create(empid=e, name=n, age=a, gender=g, place=p,designation=d,image=i)
        k.save()
        return viewemployee(request)

    return render(request, 'addemployee.html')

def details(request,p):
    k=employee.objects.get(id=p)
    context={'employee':k}
    return render(request, 'details.html',context)

def delete(request,p):
    k=employee.objects.get(id=p)
    k.delete()
    return redirect('viewemployee')


def editemployee(request,p):
    k=employee.objects.get(id=p)
    if (request.method == "POST"):
        k.empid = request.POST['e']
        k.name = request.POST['n']
        k.age = request.POST['a']
        k.gender = request.POST['g']
        k.place = request.POST['p']
        k.designation = request.POST['d']
        if (request.FILES.get('i') == None):
            k.save()
        else:
            k.image = request.FILES.get('i')
        k.save()
        return redirect('viewemployee')

    context={'employee':k}
    return render(request,'editemployee.html',context)