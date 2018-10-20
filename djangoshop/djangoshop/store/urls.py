from django.urls import path
from .import views

app_name = "store"

urlpatterns = [
    path('', views.index, name="index"),
    path('product/', views.product, name="product"),
    path('store/', views.store, name="store"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
]
