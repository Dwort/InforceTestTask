from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'


class MenuVoteCountSerializer(serializers.Serializer):
    menu_id = serializers.IntegerField()
    vote_count = serializers.IntegerField()
