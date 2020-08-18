from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'restaurant/main.html')


def menu(request):
    products = Product.objects
    return render(request, 'restaurant/menu.html', {'products': products})


def reservations(request):
    return render(request, 'restaurant/reservations.html')


def contact(request):
    return render(request, 'restaurant/contact.html')
