from django.urls import path

from .views import (
    HomeView,
    ShopView,
    partners,
    project,
    about,
    menu,
    reviews,
    ProductListView,
    ProductUpdateView,
    ProductCreateView,
    ProductDeleteView
)

app_name = "coffee_shop"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/products/', ProductListView.as_view(), name="products"),
    path('shop/products/create/', ProductCreateView.as_view(), name="product_create"),
    path('shop/products/delete/<int:pk>', ProductDeleteView.as_view(), name="delete"),
    path('shop/products/<int:pk>', ProductUpdateView.as_view(), name="product_details"),
    path('partners/', partners, name='partners'),
    path('project/', project, name='project'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('reviews/', reviews, name='reviews')
]
