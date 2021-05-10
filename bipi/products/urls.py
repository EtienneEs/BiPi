from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    PriceListView,
    PriceCreateView,
    PriceDetailView,
    PriceUpdateView
)


app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('prices/', PriceListView.as_view(), name='price_list'),
    path('prices/create/', PriceCreateView.as_view(), name='price_create'),
    path('prices/<int:pk>/', PriceDetailView.as_view(), name='price_detail'),
    path('prices/<int:pk>/update/', PriceUpdateView.as_view(), name='price_update'),
]
