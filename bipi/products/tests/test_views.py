import pytest
import factory
from pytest_django.asserts import (
    assertContains,
    assertTemplateUsed
)
from django.urls import reverse

from .factories import ProductFactory, product
from ..models import Product
from ..views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView
)

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


class TestProductDetailView:

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
