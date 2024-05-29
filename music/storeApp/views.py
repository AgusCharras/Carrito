from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from .cart import Cart

def store(request):
    products = Product.objects.all()
    return render(request, "store.html", {"products": products})

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)  # Corregido aquí
    cart.add(product)
    return redirect('store')

def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)  # Corregido aquí
    cart.delete(product)
    return redirect('store')

def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(pk=product_id)  # Corregido aquí
    cart.remove(product)
    return redirect('store')

def clean_cart(request):
    cart = Cart(request)
    cart.clean()
    return redirect('store')
