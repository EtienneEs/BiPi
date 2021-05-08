from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView
)


app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]