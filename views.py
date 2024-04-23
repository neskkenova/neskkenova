from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from coffee_shop.forms import OrderCreateForm
from coffee_shop.models import Product, Order


class HomeView(View):

    def get(self, request: HttpRequest):
        return render(request, "coffee_shop/home.html")


class ShopView(View):

    def get(self, request: HttpRequest):

        if request.user.is_authenticated:
            user = request.user
            context = {
                "goods": Product.objects.all(),
                "form": OrderCreateForm(user=user),
                "orders": Order.objects.filter(user=user)
            }
        else:
            context = {}
        return render(request, "coffee_shop/shop.html", context)

    def post(self, request: HttpRequest):
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        return render(request, "coffee_shop/shop.html", {"form": form})


class ProductListView(ListView):
    model = Product
    context_object_name = "products"


class ProductUpdateView(UpdateView):
    model = Product
    context_object_name = "product"
    fields = "name", "category", "description", "price", "discount", "archived"
    success_url = reverse_lazy("coffee_shop:products")


class ProductCreateView(CreateView):
    model = Product
    fields = "name", "category", "description", "price", "discount", "archived"
    success_url = reverse_lazy("coffee_shop:products")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("coffee_shop:products")


def partners(request):
    return render(request, "coffee_shop/partners.html")


def project(request):
    return render(request, "coffee_shop/project.html")


def about(request):
    return render(request, "coffee_shop/about.html")


def menu(request):
    context = {
        "form": OrderCreateForm()
    }
    return render(request, "coffee_shop/menu.html", context)


def reviews(request):
    return render(request, "coffee_shop/reviews.html")
