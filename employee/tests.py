import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Employee, Vote
from restaurants.models import Menu, Restaurant
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user_and_authenticate(api_client):
    user = User.objects.create_user(username='TestUser2', password='testpassword22')
    refresh = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return user, api_client


@pytest.mark.django_db
def test_register_employee(create_user_and_authenticate):
    user, client = create_user_and_authenticate
    url = reverse('employee:employee-register')
    data = {
        'email': 'employee1@example.com',
        'name': 'Employee One',
        'phone_number': '123456789000'
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Employee.objects.filter(email='employee1@example.com').exists()


@pytest.mark.django_db
def test_employee_vote(create_user_and_authenticate):
    user, client = create_user_and_authenticate
    restaurant = Restaurant.objects.create(restaurant_name='Test Restaurant', description='Test Description',
                                           address='Test Address', phone_number='123456789')
    menu = Menu.objects.create(restaurant=restaurant, dishes=[{"name": "Dish 1", "price": 10.99}])
    employee = Employee.objects.create(email='employee2@example.com', name='Employee TWO',
                                       phone_number='987654321000')

    url = reverse('employee:vote', kwargs={'employee_id': employee.id, 'menu_id': menu.id})
    response = client.post(url)

    assert response.status_code == status.HTTP_201_CREATED
    assert Vote.objects.filter(employee=employee, menu_item=menu).exists()


