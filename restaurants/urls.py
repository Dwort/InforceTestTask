from django.urls import path
from .views import (
    AddRestaurantView,
    AddMenuView,
    RestaurantAllView,
    RestaurantEditView,
    MenuAllView,
    MenuEditView,
    GetCurrentDayMenu,
    GetBestDayMenu,
)

app_name = 'restaurants'

urlpatterns = [
    path('rest/add/restaurant/', AddRestaurantView.as_view(), name='add-restaurant'),
    path('rest/add/menu/', AddMenuView.as_view(), name='add-menu'),
    path('rest/all/restaurant/', RestaurantAllView.as_view(), name='restaurant-all'),
    path('rest/restaurant/<int:rest_id>/', RestaurantEditView.as_view(), name='restaurant-edit'),
    path('rest/all/menu/', MenuAllView.as_view(), name='menu-all'),
    path('rest/menu/<int:menu_id>/', MenuEditView.as_view(), name='menu-edit'),
    path('rest/menu/today/', GetCurrentDayMenu.as_view(), name='menu-today'),
    path('rest/menu/today/count/', GetBestDayMenu.as_view(), name='menu-current-day-count'),

]
