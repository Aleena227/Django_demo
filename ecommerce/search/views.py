from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.

def search(request):
    if(request.method=="POST"):
        query=request.POST['q']
        if query:
            p = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
            context = {'pro': p, 'query': query}
    return render(request,'search.html',context)

