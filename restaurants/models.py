from django.db import models


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.restaurant_name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    date = models.DateField(auto_now_add=True)
    dishes = models.JSONField(default=list)

    def __str__(self):
        return f"{self.restaurant.restaurant_name} -> {self.pk}"
