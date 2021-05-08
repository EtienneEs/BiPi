import pytest

from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from ..models import Stock
from ...products.tests.factories import ProductFactory


@pytest.fixture
def stock():
    return StockFactory()


class StockFactory(DjangoModelFactory):
    product = SubFactory(ProductFactory)
    quantity = Faker('pyint')

    class Meta:
        model = Stock
        django_get_or_create = ('product',)
