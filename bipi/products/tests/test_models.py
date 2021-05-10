import pytest

from .factories import product, price

pytestmark = pytest.mark.django_db


def test_product__str__(product: product):
    assert product.__str__() == f'Product: {product.name}'
    assert str(product) == f'Product: {product.name}'


def test_product_get_absolute_url(product: product):
    assert product.get_absolute_url() == f'/products/{product.id}/'


def test_price__str__(price: price):
    assert price.__str__() == f'{price.organization} - {price.product} {price.price}'
    assert str(price) == f'{price.organization} - {price.product} {price.price}'


def test_price_get_absolute_url(price: price):
    assert price.get_absolute_url() == f'/products/prices/{price.id}/'
