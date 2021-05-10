import pytest

from django.urls import reverse, resolve

from .factories import product, price

pytestmark = pytest.mark.django_db


def test_products_list_reverse():
    assert reverse('products:product_list') == '/products/'


def test_products_list_resolve():
    assert resolve('/products/').view_name == 'products:product_list'


def test_products_create_reverse():
    assert reverse('products:product_create') == '/products/create/'


def test_products_create_resolve():
    assert resolve('/products/create/').view_name == 'products:product_create'


def test_products_detail_reverse(product: product):
    url = reverse('products:product_detail', kwargs={'pk': product.pk})
    assert url == f'/products/{product.pk}/'


def test_products_detail_resolve(product: product):
    url = f'/products/{product.pk}/'
    assert resolve(url).view_name == 'products:product_detail'


def test_products_update_reverse(product: product):
    url = reverse('products:product_update', kwargs={'pk': product.pk})
    assert url == f'/products/{product.pk}/update/'


def test_products_update_resolve(product: product):
    url = f'/products/{product.pk}/update/'
    assert resolve(url).view_name == 'products:product_update'


def test_prices_list_reverse():
    assert reverse('products:price_list') == '/products/prices/'


def test_prices_list_resolve():
    assert resolve('/products/prices/').view_name == 'products:price_list'


def test_prices_create_reverse():
    assert reverse('products:price_create') == '/products/prices/create/'


def test_prices_create_resolve():
    assert resolve('/products/prices/create/').view_name == 'products:price_create'


def test_prices_detail_reverse(price: price):
    url = reverse('products:price_detail', kwargs={'pk': price.pk})
    assert url == f'/products/prices/{price.pk}/'


def test_prices_detail_resolve(price: price):
    url = f'/products/prices/{price.pk}/'
    assert resolve(url).view_name == 'products:price_detail'


def test_prices_update_reverse(price: price):
    url = reverse('products:price_update', kwargs={'pk': price.pk})
    assert url == f'/products/prices/{price.pk}/update/'


def test_prices_update_resolve(price: price):
    url = f'/products/prices/{price.pk}/update/'
    assert resolve(url).view_name == 'products:price_update'
