from django.shortcuts import render
from .models import *


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request, pk):
    product = Product.objects.get(pk=pk)
    images = Image.objects.filter(product=product)
    return render(request, 'about.html', {'product': product, 'images': images})
