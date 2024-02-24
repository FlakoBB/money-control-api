from django.shortcuts import render
from transactions.models import Income, Expense

def index(request):
  incomes = Income.objects.values_list('amount', flat=True)

  total_income = 0
  for amount in incomes:
    total_income += amount

  expenses = Expense.objects.values_list('amount', flat=True)

  total_expense = 0
  for amount in expenses:
    total_expense += amount

  available = total_income - total_expense

  context = {
    'total_income': total_income,
    'total_expense': total_expense,
    'available': available,
  }

  return render(request, 'core/index.html', context)
