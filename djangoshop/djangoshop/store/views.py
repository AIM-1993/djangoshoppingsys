from django.shortcuts import render
from django.conf import settings
from .models import Product, Category
# Create your views here.
def index(request):
    product_list = Product.objects.all()
    new_product_list = Product.new_product.all()
    hot_product_list = Product.hot_product.all()
    return render(request, "index.html", locals())


def product(request):
    product_list = Product.objects.all()
    return render(request, "product.html", locals())


def store(request):
    product_list = Product.objects.all()
    new_product_list = Product.new_product.all()
    hot_product_list = Product.hot_product.all()
    return render(request, "store.html", locals())


def search(request):
    categories = Category.objects.filter(parent=None)
    if request.method == "POST":
        keyword = request.POST.get('keyword', '')
        col_list = Product.objects.filter(name__contains=keyword)
        col_list = get_page(request, col_list)
        return render(request, "store.html", locals())

