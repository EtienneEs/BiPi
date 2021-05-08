from django.urls import path

from .views import (
    StockListView,
    StockCreateView,
    StockDetailView,
    StockUpdateView
)


app_name = 'inventories'
urlpatterns = [
    path('', StockListView.as_view(), name='stock_list'),
    path('create/', StockCreateView.as_view(), name='stock_create'),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('<int:pk>/update/', StockUpdateView.as_view(), name='stock_update'),
]
