from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Product, Category
from .forms import CheckoutForm

# Create your views here.


def get_page(request, product_all_list):
    paginator = Paginator(product_all_list, 3)

    page_num = request.GET.get('page', 1)
    page_of_products = paginator.get_page(page_num)
    current_page_num = page_of_products.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(range(current_page_num, min(current_page_num + 2, paginator.num_pages + 1)))
    if page_range[0] - 1 >= 2:
        page_range.insert(0, "...")
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append("...")
    if page_range[0] != 1:
        page_range.insert(0, 1)
    context = {}
    context['products'] = page_of_products.object_list
    context['page_of_products'] = page_of_products
    context['page_range'] = page_range

    return context


def index(request):
    categories_list = Category.objects.all()
    product_list = Product.objects.all()
    new_product_list = Product.new_product.all()
    hot_product_list = Product.hot_product.all()

    return render(request, "index.html", locals())


def product(request, id=4):
    product_list = Product.objects.get(pk=id)
    return render(request, "product.html", locals())


def store(request):
    product_all_list = Product.objects.all()
    product_page = get_page(request, product_all_list)
    categories_list = Category.objects.all()

    return render(request, "store.html", locals())


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/product/')
    else:
        form = CheckoutForm()
    return render(request, "checkout.html", locals())


def about(request):
    return render(request, "about.html")


def search(request):
    categories = Category.objects.filter(parent=None)
    if request.method == "POST":
        keyword = request.POST.get('keyword', '')
        col_list = Product.objects.filter(name__contains=keyword)
        col_list = get_page(request, col_list)
        return render(request, "store.html", locals())
