import pytest

from .factories import product

pytestmark = pytest.mark.django_db


def test_product__str__(product: product):
    assert product.__str__() == f'Product: {product.name}'
    assert str(product) == f'Product: {product.name}'
