from django.shortcuts import render


def home(request):
    return render(request, 'restaurant/main.html')


def reservations(request):
    return render(request, 'restaurant/reservations.html')


def contact(request):
    return render(request, 'restaurant/contact.html')
