from django.shortcuts import render
from transactions.models import Income, Expense

def index(request):
  transactions = []

  incomes = Income.objects.values('amount', 'date')[:5]
  for income in incomes:
    transaction = {
      'type': 'Income',
      'amount': income['amount'],
      'date': income['date'],
    }
    transactions.append(transaction)

  expenses = Expense.objects.values('amount', 'date')[:5]
  for expense in expenses:
    transaction = {
      'type': 'Expense',
      'amount': expense['amount'],
      'date': expense['date'],
    }
    transactions.append(transaction)

  last_transactions = sorted(transactions, key=lambda transaction: transaction['date'], reverse=True)

  context = {
    'last_transactions': last_transactions,
  }

  return render(request, 'core/index.html', context)
