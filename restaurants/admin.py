from django.contrib import admin
from .models import Menu, Restaurant

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu)