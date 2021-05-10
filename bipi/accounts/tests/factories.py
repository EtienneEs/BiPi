import pytest

from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from ..models import Organization, Account

@pytest.fixture
def organization():
    return OrganizationFactory()


@pytest.fixture
def account():
    return AccountFactory()


class OrganizationFactory(DjangoModelFactory):
    name = Faker('company',)

    class Meta:
        model = Organization
        django_get_or_create = ('name',)


class AccountFactory(DjangoModelFactory):
    name = Faker('company', )
    address = Faker('address')
    organization = SubFactory(OrganizationFactory)

    class Meta:
        model = Account
        django_get_or_create = ('name',)
