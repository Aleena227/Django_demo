"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart import views
from django.conf.urls.static import static
from django.conf import settings

app_name='cart'
urlpatterns = [
    path('addtocart/<int:i>',views.addtocart,name='addtocart'),
    path('cartview',views.cartview,name='cartview'),
    path('cartremove/<int:i>',views.cartremove,name='cartremove'),
    path('addtowishlist/<int:i>',views.addtowishlist,name='addtowishlist'),
    path('wishlistview',views.wishlistview,name='wishlistview'),
    path('wishlistremove/<int:i>',views.wishlistremove,name='wishlistremove'),
    path('cartdelete/<int:i>',views.cartdelete,name='cartdelete'),
    path('orderform',views.orderform,name='orderform'),
    path('payment_status/<u>',views.payment_status,name='payment_status'),
    path('orderview',views.orderview,name='orderview'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)