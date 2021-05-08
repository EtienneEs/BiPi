from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView
)

from .models import Product
from .forms import ProductForm


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'products/product_list.html'
    queryset = Product.objects.all()


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'products/product_detail.html'
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'products/product_create.html'
    model = Product
    form_class = ProductForm
    action = 'Update'


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'products/product_create.html'
    model = Product
    form_class = ProductForm
