import pytest

from django.urls import reverse, resolve

from .factories import stock

pytestmark = pytest.mark.django_db


def test_list_reverse():
    assert reverse('inventories:stock_list') == '/inventories/'


def test_list_resolve():
    assert resolve('/inventories/').view_name == 'inventories:stock_list'


def test_create_reverse():
    assert reverse('inventories:stock_create') == '/inventories/create/'


def test_create_resolve():
    assert resolve('/inventories/create/').view_name == 'inventories:stock_create'


def test_detail_reverse(stock: stock):
    url = reverse('inventories:stock_detail', kwargs={'pk': stock.pk})
    assert url == f'/inventories/{stock.pk}/'


def test_detail_resolve(stock: stock):
    url = f'/inventories/{stock.pk}/'
    assert resolve(url).view_name == 'inventories:stock_detail'


def test_update_reverse(stock: stock):
    url = reverse('inventories:stock_update', kwargs={'pk': stock.pk})
    assert url == f'/inventories/{stock.pk}/update/'


def test_update_resolve(stock: stock):
    url = f'/inventories/{stock.pk}/update/'
    assert resolve(url).view_name == 'inventories:stock_update'
