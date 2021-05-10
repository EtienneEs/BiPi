import pytest
from pytest_django.asserts import (
    assertContains,
    assertTemplateUsed
)
import factory

from django.urls import reverse

from djmoney.money import Money

from .factories import (
    ProductFactory,
    product,
    PriceFactory,
    price
)
from ..models import Product, Price
from ..views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    PriceCreateView,
    PriceListView,
    PriceDetailView,
    PriceUpdateView
)
from ...accounts.tests.factories import organization

pytestmark = pytest.mark.django_db


class TestProductListView:

    def test_status(self, rf, admin_user, product: product):
        url = reverse('products:product_list')
        request = rf.get(url)
        request.user = admin_user
        response = ProductListView.as_view()(request)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client):
        url = reverse('products:product_list')
        response = admin_client.get(url)
        assertTemplateUsed(response, 'products/product_list.html')

    def test_list_contains_2_products(self, admin_client, product: product):
        url = reverse('products:product_list')
        product1 = product
        product2 = ProductFactory()
        response = admin_client.get(url)
        assertContains(response, product1.name)
        assertContains(response, product2.name)


class TestProductDetailView:

    def test_status(self, rf, admin_user, product):
        url = reverse('products:product_detail', kwargs={'pk': product.pk})
        request = rf.get(url)
        request.user = admin_user
        response = ProductDetailView.as_view()(request, pk=product.pk)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client, product):
        url = reverse('products:product_detail', kwargs={'pk': product.pk})
        response = admin_client.get(url)
        assertTemplateUsed(response, 'products/product_detail.html')


class TestProductCreateView:

    def test_status(self, rf, admin_user):
        url = reverse('products:product_create')
        request = rf.get(url)
        request.user = admin_user
        response = ProductCreateView.as_view()(request)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client):
        url = reverse('products:product_create')
        response = admin_client.get(url)
        assertTemplateUsed(response, 'products/product_create.html')

    def test_creates_product(self, admin_client):
        url = reverse('products:product_create')
        form_data = factory.build(dict, FACTORY_CLASS=ProductFactory)
        response = admin_client.post(url, form_data)
        assert response.status_code == 302
        new_product = Product.objects.first()
        assert new_product.name == form_data['name']


class TestProductUpdateView:

    def test_status(self, rf, admin_user, product):
        url = reverse('products:product_update', kwargs={'pk': product.pk})
        request = rf.get(url)
        request.user = admin_user
        response = ProductUpdateView.as_view()(request, pk=product.pk)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client, product):
        url = reverse('products:product_update', kwargs={'pk': product.pk})
        response = admin_client.get(url)
        assertTemplateUsed(response, 'products/product_create.html')

    def test_update_form_valid(self, admin_client, product):
        original_product = product
        url = reverse('products:product_update', kwargs={'pk': original_product.pk})
        form_data = factory.build(dict, FACTORY_CLASS=ProductFactory)
        response = admin_client.post(url, form_data)
        assert response.status_code == 302
        updated_product = Product.objects.get(pk=original_product.pk)
        assert updated_product.name == form_data['name']


class TestPriceListView:

    def test_status(self, rf, admin_user, price: price):
        url = reverse('products:price_list')
        request = rf.get(url)
        request.user = admin_user
        response = PriceListView.as_view()(request)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client):
        url = reverse('products:price_list')
        response = admin_client.get(url)
        assertTemplateUsed(response, 'products/price_list.html')

    def test_list_contains_2_products(self, admin_client, price: price):
        url = reverse('products:price_list')
        price1 = price
        price2 = PriceFactory()
        response = admin_client.get(url)
        assertContains(response, price1.price)
        assertContains(response, price2.price)


class TestPriceDetailView:

    def test_status(self, rf, admin_user, price):
        url = reverse('products:price_detail', kwargs={'pk': price.pk})
        request = rf.get(url)
        request.user = admin_user
        response = PriceDetailView.as_view()(request, pk=price.pk)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client, price):
        url = reverse('products:price_detail', kwargs={'pk': price.pk})
        response = admin_client.get(url)
        assertTemplateUsed(response, 'products/price_detail.html')


class TestPriceCreateView:

    def test_status(self, rf, admin_user):
        url = reverse('products:price_create')
        request = rf.get(url)
        request.user = admin_user
        response = PriceCreateView.as_view()(request)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client):
        url = reverse('products:price_create')
        response = admin_client.get(url)
        assertTemplateUsed(response, 'products/price_create.html')

    def test_creates_price(self, admin_client, product, organization):
        url = reverse('products:price_create')
        price_money = Money(42.0, 'EUR')
        form_data = {
            'product': product.pk,
            'organization': organization.pk,
            'price_0': price_money.amount,
            'price_1': price_money.currency
        }
        response = admin_client.post(url, form_data)
        assert response.status_code == 302
        new_price = Price.objects.first()
        assert new_price.product.pk == product.pk
        assert new_price.organization == organization
        assert new_price.price == price_money


class TestPriceUpdateView:

    def test_status(self, rf, admin_user, price):
        url = reverse('products:price_update', kwargs={'pk': price.pk})
        request = rf.get(url)
        request.user = admin_user
        response = PriceUpdateView.as_view()(request, pk=price.pk)
        assert response.status_code == 200

    def test_uses_correct_template(self, admin_client, price):
        url = reverse('products:price_update', kwargs={'pk': price.pk})
        response = admin_client.get(url)
        assertTemplateUsed(response, 'products/price_create.html')

    def test_update_form_valid(self, admin_client, price):
        original_price = price
        url = reverse('products:price_update', kwargs={'pk': original_price.pk})
        new_price = Money(100.1, "CHF")
        form_data = {
            'price_0': new_price.amount,
            'price_1': new_price.currency

        }
        response = admin_client.post(url, form_data)
        assert response.status_code == 302
        updated_price = Price.objects.get(pk=original_price.pk)
        assert updated_price.price == new_price
