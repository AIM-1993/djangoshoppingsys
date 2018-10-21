from django.urls import path, re_path
from .import views

app_name = "store"

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^product/(?:page-(?P<product_id>\d+)/)?$', views.product, name="product"),
    re_path(r'^store/$', views.store, name="store"),
    re_path(r'^checkout/?$', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
]
