import pytest

from .factories import stock

pytestmark = pytest.mark.django_db


def test_stock__str__(stock: stock):
    string = f'Stock: {stock.product.name}'
    assert stock.__str__() == string
    assert str(stock) == string


def test_stock_get_absolute_url(stock: stock):
    assert stock.get_absolute_url() == f'/inventories/{stock.id}/'
