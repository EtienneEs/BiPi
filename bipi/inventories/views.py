from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView
)

from .models import Stock


class StockListView(LoginRequiredMixin, ListView):
    template_name = 'inventories/stock_list.html'
    queryset = Stock.objects.all()


class StockDetailView(LoginRequiredMixin, DetailView):
    template_name = 'inventories/stock_detail.html'
    model = Stock


class StockUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'inventories/stock_create.html'
    model = Stock
    fields = ['quantity']
    action = 'Update'


class StockCreateView(LoginRequiredMixin, CreateView):
    template_name = 'inventories/stock_create.html'
    model = Stock
    fields = ['product', 'quantity']
