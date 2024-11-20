from django.shortcuts import render,redirect
from shop.models import Product
from cart.models import Cart,Payment,Order_details
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt

@login_required
def addtocart(request,i):
    p=Product.objects.get(id=i)
    u=request.user
    try:
        c=Cart.objects.get(product=p,user=u)
        if(p.stock>0):
            c.quantity += 1
            c.save()
            p.stock -= 1
            p.save()
    except:
        if(p.stock>0):
            c = Cart.objects.create(product=p, user=u, quantity=1)
            c.save()
            p.stock -= 1
            p.save()
    return redirect('cart:cartview')

@login_required
def cartremove(request,i):
    p=Product.objects.get(id=i)
    u=request.user
    try:
        c=Cart.objects.get(product=p,user=u)
        if(c.quantity>1):
            c.quantity -= 1
            c.save()
            p.stock += 1
            p.save()
        else:
            c.delete()
            p.stock+=1
            p.save()
    except:
        pass
    return redirect('cart:cartview')

@login_required
def cartdelete(request,i):
    p=Product.objects.get(id=i)
    u=request.user
    try:
        c = Cart.objects.get(product=p, user=u)
        newstock=c.quantity
        c.delete()
        p.stock += newstock
        p.save()
    except:
        pass
    return redirect('cart:cartview')

@login_required
def cartview(request):
    u=request.user
    c = Cart.objects.filter(user=u)
    total = 0
    for i in c:
        total += i.quantity * i.product.price
    context={'cart':c,'total':total}
    return render(request,'cartview.html',context)


def orderform(request):
    if(request.method=='POST'):
        address=request.POST['a']
        phone=request.POST['p']
        pin=request.POST['pi']
        u=request.user
        c=Cart.objects.filter(user=u)
        total=0
        for i in c:
            total += i.quantity * i.product.price
        total1=int(total*100)
        print(total)

        client=razorpay.Client(auth=('rzp_test_SXJ3hxAczZVSCV','ylZeA9wb1HXpNHtoc6HiPBEg'))
        response_payment=client.order.create(dict(amount=total1,currency='INR'))
        print(response_payment)
        order_id=response_payment['id']
        status=response_payment['status']
        if(status=='created'):
            p=Payment.objects.create(name=u.username,amount=total,order_id=order_id)
            p.save()
            for i in c:
               o=Order_details.objects.create(product=i.product, user=u, no_of_items=i.quantity,address=address,phone_no=phone,pin=pin,order_id=order_id)
               o.save()
               c.delete()
               response_payment['name']=u.username
               context={'payment':response_payment}
        return render(request,'payment.html',context)
    return render(request, 'orderform.html')


@csrf_exempt
def payment_status(request,u):
    print(u)
    usr = User.objects.get(username=u)
    if not request.user.is_authenticated:
        login(request, usr)
    if(request.method=='POST'):
        response=request.POST
        print(response)

        param_dict={
            'razorpay_order_id':response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']

        }

        client = razorpay.Client(auth=('rzp_test_SXJ3hxAczZVSCV','ylZeA9wb1HXpNHtoc6HiPBEg'))
        try:
            status = client.utility.verify_payment_signature(param_dict)
            print(status)

            #to retrieve a particular record dfrom payment table matching with razorpay response order id
            p=Payment.objects.get(order_id=response['razorpay_order_id'])
            p.razorpay_payment_id=response['razorpay_payment_id']
            p.paid=True
            p.save()
            o=Order_details.objects.filter(order_id=response['razorpay_order_id'])
            for i in o:
                i.payment_status="completed"
                i.save()

            c=Cart.objects.filter(user=usr)
            c.delete()

        except:
            pass


    return render(request,'payment_status.html',{'status':status})


@login_required
def orderview(request):
    u=request.user
    o=Order_details.objects.filter(user=u)
    print(o)
    context={'orders':o}
    return render(request,'orderview.html',context)

@login_required
def addtowishlist(request,i):
    p=Product.objects.get(id=i)
    u=request.user
    try:
        c=Cart.objects.get(product=p,user=u)
        if(p.stock>0):
            c.quantity += 1
            c.save()
            p.stock -= 1
            p.save()
    except:
        if(p.stock>0):
            c = Cart.objects.create(product=p, user=u, quantity=1)
            c.save()
            p.stock -= 1
            p.save()
    return redirect('cart:cartview')

@login_required
def wishlistremove(request,i):
    p=Product.objects.get(id=i)
    u=request.user
    try:
        c=Cart.objects.get(product=p,user=u)
        if(c.quantity>1):
            c.quantity -= 1
            c.save()
            p.stock += 1
            p.save()
        else:
            c.delete()
            p.stock+=1
            p.save()
    except:
        pass
    return redirect('cart:cartview')


@login_required
def wishlistview(request):
    u=request.user
    c = Cart.objects.filter(user=u)
    context={'cart':c}
    return render(request,'wishlistview.html',context)


