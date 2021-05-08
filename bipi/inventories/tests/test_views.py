import pytest
import factory
from pytest_django.asserts import (
    assertContains,
    assertTemplateUsed
)
from django.urls import reverse

from .factories import StockFactory, stock
from ..models import Stock
from ..views import (
    StockCreateView,
    StockListView,
    StockDetailView,
    StockUpdateView
)
from ...products.tests.factories import product

pytestmark = pytest.mark.django_db


class TestStockListView:

    def test_status(self, rf, admin_user, stock: stock):
        url = reverse('inventories:stock_list')
        request = rf.get(url)
        request.user = admin_user
        response = StockListView.as_view()(request)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client):
        url = reverse('inventories:stock_list')
        response = admin_client.get(url)
        assertTemplateUsed(response, 'inventories/stock_list.html')

    def test_list_contains_2_inventories(self, admin_client, stock: stock):
        url = reverse('inventories:stock_list')
        stock1 = stock
        stock2 = StockFactory()
        response = admin_client.get(url)
        assertContains(response, stock1.quantity)
        assertContains(response, stock2.quantity)


class TestStockDetailView:

    def test_status(self, rf, admin_user, stock: stock):
        url = reverse('inventories:stock_detail', kwargs={'pk': stock.pk})
        request = rf.get(url)
        request.user = admin_user
        response = StockDetailView.as_view()(request, pk=stock.pk)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client, stock: stock):
        url = reverse('inventories:stock_detail', kwargs={'pk': stock.pk})
        response = admin_client.get(url)
        assertTemplateUsed(response, 'inventories/stock_detail.html')


class TestStockCreateView:

    def test_status(self, rf, admin_user):
        url = reverse('inventories:stock_create')
        request = rf.get(url)
        request.user = admin_user
        response = StockCreateView.as_view()(request)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client):
        url = reverse('inventories:stock_create')
        response = admin_client.get(url)
        assertTemplateUsed(response, 'inventories/stock_create.html')

    def test_creates_stock(self, admin_client, product: product):
        url = reverse('inventories:stock_create')
        form_data = factory.build(dict, FACTORY_CLASS=StockFactory)
        form_data.update({'product': product.pk, })
        response = admin_client.post(url, form_data)
        assert response.status_code == 302
        new_stock = Stock.objects.first()
        assert new_stock.quantity == form_data['quantity']


class TestStockUpdateView:

    def test_status(self, rf, admin_user, stock):
        url = reverse('inventories:stock_update', kwargs={'pk': stock.pk})
        request = rf.get(url)
        request.user = admin_user
        response = StockDetailView.as_view()(request, pk=stock.pk)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client, stock):
        url = reverse('inventories:stock_update', kwargs={'pk': stock.pk})
        response = admin_client.get(url)
        assertTemplateUsed(response, 'inventories/stock_create.html')

    def test_update_form_valid(self, admin_client, stock):
        original_stock = stock
        url = reverse('inventories:stock_update', kwargs={'pk': original_stock.pk})
        form_data = factory.build(dict, FACTORY_CLASS=StockFactory)
        form_data.update({'product': stock.product.pk, })
        response = admin_client.post(url, form_data)
        assert response.status_code == 302
        updated_stock = Stock.objects.get(pk=original_stock.pk)
        assert updated_stock.quantity == form_data['quantity']
