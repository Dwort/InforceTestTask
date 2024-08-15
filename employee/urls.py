from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from employee.views import (
    EmployeeRegisterView,
    EmployeeAllView,
    EmployeeEditView,
    VoteView,
)

app_name = 'employee'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user/register/', EmployeeRegisterView.as_view(), name='employee-register'),
    path('user/all/', EmployeeAllView.as_view(), name='employee-all'),
    path('user/<int:user_id>/', EmployeeEditView.as_view(), name='employee-edit'),
    path('user/vote/<int:employee_id>/<int:menu_id>/', VoteView.as_view(), name='vote'),
]
