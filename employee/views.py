from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Vote
from restaurants.models import Menu
from .serializers import EmployeeSerializer, VoteSerializer


# Create Employee
class EmployeeRegisterView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EmployeeSerializer


# Show all employees in DB
class EmployeeAllView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CRUD operations for employee (get specific employee; edit data - put; delete employee - delete)
class EmployeeEditView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        employee = Employee.objects.get(id=user_id)
        serialized_employee = EmployeeSerializer(employee)
        return Response(serialized_employee.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        employee = Employee.objects.get(id=user_id)
        if employee is None:
            serializer = EmployeeSerializer(instance=employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        employee = Employee.objects.get(id=user_id)
        if employee is not None:
            employee.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)


# Voting implementation class
class VoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, employee_id, menu_id):
        try:
            employee = Employee.objects.get(pk=employee_id)
            menu = Menu.objects.get(pk=menu_id)

        except (Employee.DoesNotExist, Menu.DoesNotExist):
            return Response({'error': 'Employee or Menu not found'}, status=status.HTTP_404_NOT_FOUND)

        existing_vote = Vote.objects.filter(employee=employee, menu_item=menu, date_of_voting=menu.date).first()

        if existing_vote:
            return Response({'error': 'Employee has already voted for this menu today'},
                            status=status.HTTP_400_BAD_REQUEST)

        vote_data = {'employee': employee.id, 'menu_item': menu.id}
        serializer = VoteSerializer(data=vote_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
