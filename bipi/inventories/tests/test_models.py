import pytest

from .factories import inventory

pytestmark = pytest.mark.django_db


def test_inventory__str__(inventory: inventory):
    string = f'Inventory: [{inventory.id}] {inventory.product} {inventory.quantity}'
    assert inventory.__str__() == string
    assert str(inventory) == string
