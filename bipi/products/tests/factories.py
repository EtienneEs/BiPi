import pytest

from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Product


@pytest.fixture
def product():
    return ProductFactory()


class ProductFactory(DjangoModelFactory):
    name = Faker('sentence', nb_words=3)

    class Meta:
        model = Product
