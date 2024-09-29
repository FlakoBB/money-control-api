from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Income, Expense
from .serializers import IncomeSerializer, ExpenseSerializer

class RegisterIncomeView(generics.CreateAPIView):
  queryset = Income.objects.all()
  serializer_class = IncomeSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class IncomeListView(generics.ListAPIView):
  serializer_class = IncomeSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return Income.objects.filter(user=user)
  
class ResgisterExpenseView(generics.CreateAPIView):
  queryset = Expense.objects.all()
  serializer_class = ExpenseSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class ExpenseListView(generics.ListAPIView):
  serializer_class = ExpenseSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    user = self.request.user
    return Expense.objects.filter(user=user)
