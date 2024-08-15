from django.db import models
from restaurants.models import Menu


class Employee(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date_of_voting = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} -> menu id: {self.menu_item.pk}"
