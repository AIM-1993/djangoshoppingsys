from django.shortcuts import render
from django.conf import settings
from .models import Product
# Create your views here.
def index(request):
    product_list = Product.objects.all()
    return render(request, "index.html", locals())


def product(request):
    product_list = Product.objects.all()
    return render(request, "product.html", locals())


def store(request):
    return render(request, "store.html")
