import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Restaurant, Menu
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user_and_authenticate(api_client):
    user = User.objects.create_user(username='TestUser3', password='testpassword33')
    refresh = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return user, api_client


@pytest.mark.django_db
def test_add_restaurant(create_user_and_authenticate):
    user, client = create_user_and_authenticate
    url = reverse('restaurants:add-restaurant')
    data = {
        'restaurant_name': 'New Restaurant',
        'description': 'A fine dining place',
        'address': '123 Fancy St.',
        'phone_number': '555-5555'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.filter(restaurant_name='New Restaurant').exists()


@pytest.mark.django_db
def test_get_today_menu(create_user_and_authenticate):
    user, client = create_user_and_authenticate
    restaurant = Restaurant.objects.create(restaurant_name='Test Restaurant', description='Test Description',
                                           address='Test Address', phone_number='000123456789')
    menu = Menu.objects.create(restaurant=restaurant, dishes=[{"name": "Dish 1", "price": 10.99}])

    url = reverse('restaurants:menu-today')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert str(menu.pk) in str(response.content)
