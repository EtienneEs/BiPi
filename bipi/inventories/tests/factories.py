import pytest

from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from ..models import Inventory
from ...products.tests.factories import ProductFactory


@pytest.fixture
def inventory():
    return InventoryFactory()


class InventoryFactory(DjangoModelFactory):
    product = SubFactory(ProductFactory)
    quantity = Faker('pyint')

    class Meta:
        model = Inventory
        django_get_or_create = ('product',)
