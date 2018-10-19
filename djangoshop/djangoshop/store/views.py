from django.shortcuts import render
from django.conf import settings
from .models import Product, Category
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger 
# Create your views here.


def get_page(request, product_list):
    paginator = Paginator(product_list, 2)
    try:
        page = int(request.GET.get('page', 1))
        product_list = paginator.page(page)
    except (EmptyPage, PageNotAnInteger, InvalidPage):
        product_list = paginator.page(1)
    return product_list


def index(request):
    categories_list = Category.objects.all()
    product_list = Product.objects.all()
    new_product_list = Product.new_product.all()
    hot_product_list = Product.hot_product.all()
    return render(request, "index.html", locals())


def product(request):
    product_list = Product.objects.all()
    return render(request, "product.html", locals())


def store(request):
    categories_list = Category.objects.all()
    product_list = Product.objects.all()
    new_product_list = Product.new_product.all()
    hot_product_list = Product.hot_product.all()
    return render(request, "store.html", locals())


def about(request):
    return render(request, "about.html")




def search(request):
    categories = Category.objects.filter(parent=None)
    if request.method == "POST":
        keyword = request.POST.get('keyword', '')
        col_list = Product.objects.filter(name__contains=keyword)
        col_list = get_page(request, col_list)
        return render(request, "store.html", locals())


