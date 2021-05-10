import pytest

from .factories import organization, account

pytestmark = pytest.mark.django_db


def test_organization__str__(organization: organization):
    assert organization.__str__() == f'Organization: {organization.name}'
    assert str(organization) == f'Organization: {organization.name}'


def test_account__str__(account: account):
    assert account.__str__() == f'Account: {account.name} ({account.organization})'
