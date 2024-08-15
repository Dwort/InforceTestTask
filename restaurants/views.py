from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from employee.models import Vote
from restaurants.models import Menu, Restaurant
from .serializers import RestaurantSerializer, MenuSerializer, MenuVoteCountSerializer
from datetime import date


# Create a new restaurant
class AddRestaurantView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RestaurantSerializer


# Create a new menu
class AddMenuView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MenuSerializer


# Show all restaurants from DB
class RestaurantAllView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CRUD operations for restaurant (get specific restaurant; edit data - put; delete restaurant - delete)
class RestaurantEditView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, rest_id):
        restaurant = Restaurant.objects.get(id=rest_id)
        serialized_restaurant = RestaurantSerializer(restaurant)
        return Response(serialized_restaurant.data, status=status.HTTP_200_OK)

    def put(self, request, rest_id):
        restaurant = Restaurant.objects.get(id=rest_id)
        if restaurant is None:
            serializer = RestaurantSerializer(instance=restaurant, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rest_id):
        restaurant = Restaurant.objects.get(id=rest_id)
        if restaurant is not None:
            restaurant.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)


# Show all menus from DB
class MenuAllView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CRUD operations for menu (get specific menu; edit data - put; delete menu - delete)
class MenuEditView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        serializer = MenuSerializer(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        if menu is None:
            serializer = MenuSerializer(instance=menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, menu_id):
        menu = Menu.objects.get(id=menu_id)
        if menu is not None:
            menu.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)


# Class to get the current menus for the day
class GetCurrentDayMenu(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        menus = Menu.objects.filter(date=today)
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Class to get today's menus by vote
class GetBestDayMenu(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        menus = Menu.objects.filter(date=today)

        result = []
        for menu in menus:
            vote_count = Vote.objects.filter(menu_item=menu).count()
            result.append({"menu_id": menu.id, "vote_count": vote_count})

        serializer = MenuVoteCountSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

