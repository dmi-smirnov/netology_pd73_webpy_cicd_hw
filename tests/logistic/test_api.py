import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from rest_framework import status

from logistic.models import Product


@pytest.mark.django_db
def test_get_products():
    # Arrange
    products_amt = 10
    products = baker.make(Product, _quantity=products_amt)

    api_base_route = '/api/v1/'
    products_route = f'{api_base_route}products/'
    api_client = APIClient()

    # Act
    resp = api_client.get(products_route)

    # Assert
    assert resp.status_code == status.HTTP_200_OK
    assert resp.data['count'] == len(products)

