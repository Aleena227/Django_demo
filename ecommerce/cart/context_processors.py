from cart.models import Cart,Wishlist
def count_items(request):
    u=request.user
    count = 0
    try:
        if request.user.is_authenticated:
            c = Cart.objects.filter(user=u)
            for i in c:
                count += i.quantity
    except:
        count=0

    return {'c':count}

def count_wishlist_items(request):
    u=request.user
    count = 0
    try:
        if request.user.is_authenticated:
            b = Wishlist.objects.filter(user=u)
            for i in b:
                count += i.quantity
    except:
        count=0

    return {'b':count}
