from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store_app/base_generic.html', context)

def home(request):
    return render(request, 'store_app/home.html')

def checkout(request):
    if request.customer.is_authenticated:
        customer = request.user
        order, date = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    
    context = {'items': items, 'order': order}
    return render(request, 'store_app/checkout.html', context)

def cart(request):
    if request.customer.is_authenticated:
        customer = request.user
        order, date = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    
    context = {'items': items, 'order': order}
    return render(request, 'store_app/cart.html', context)