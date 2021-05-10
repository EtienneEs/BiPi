import pytest

from djmoney.money import Money

from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from ..models import Product, Price
from ...accounts.tests.factories import OrganizationFactory


@pytest.fixture
def product():
    return ProductFactory()


@pytest.fixture
def price():
    return PriceFactory()


class ProductFactory(DjangoModelFactory):
    name = Faker('sentence', nb_words=3)

    class Meta:
        model = Product


class PriceFactory(DjangoModelFactory):
    product = SubFactory(ProductFactory)
    organization = SubFactory(OrganizationFactory)
    price = Money(22.2, "EUR")

    class Meta:
        model = Price
