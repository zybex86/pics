import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


@pytest.mark.django_db
def test_create_valid_user_success(api_client):
    data = {
        'email': 'test@mail.com',
        'password': 'testpass',
        'name': 'Test'
    }
    response = api_client.post(CREATE_USER_URL, data)

    assert response.status == status.HTTP_201_CREATED
    user = get_user_model().objects.get(**response.data)
    assert user.check_password(data['password'])
    assert data['password'] not in response.data


@pytest.mark.django_db
def test_user_exists(api_client):
    data = {
        'email': 'basic@mail.com',
        'password': 'testpass',
        'name': 'Test'
    }
    response = api_client.post(CREATE_USER_URL, data)

    assert response.status == status.HTTP_400_BAD_REQUEST
