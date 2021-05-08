import pytest

from django.urls import reverse, resolve

from .factories import product

pytestmark = pytest.mark.django_db


def test_list_reverse():
    assert reverse('products:product_list') == '/products/'


def test_list_resolve():
    assert resolve('/products/').view_name == 'products:product_list'


def test_create_reverse():
    assert reverse('products:product_create') == '/products/create/'


def test_create_resolve():
    assert resolve('/products/create/').view_name == 'products:product_create'


def test_detail_reverse(product: product):
    url = reverse('products:product_detail', kwargs={'pk': product.pk})
    assert url == f'/products/{product.pk}/'


def test_detail_resolve(product: product):
    url = f'/products/{product.pk}/'
    assert resolve(url).view_name == 'products:product_detail'


def test_update_reverse(product: product):
    url = reverse('products:product_update', kwargs={'pk': product.pk})
    assert url == f'/products/{product.pk}/update/'


def test_update_resolve(product: product):
    url = f'/products/{product.pk}/update/'
    assert resolve(url).view_name == 'products:product_update'
