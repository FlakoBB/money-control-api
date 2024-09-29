from rest_framework import serializers
from ..models import Income, Expense

class IncomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Income
    fields = ['id', 'title', 'description', 'amount', 'date']

class ExpenseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Expense
    fields = ['id', 'title', 'description', 'amount', 'category', 'date']
