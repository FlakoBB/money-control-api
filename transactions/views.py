from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import NewIncomForm, NewExpenseForm

def income_list(request):
  income = Income.objects.all()

  context = {
    'incomes': income,
  }

  return render(request, 'transactions/income_list.html', context)

def add_income(request):
  if request.method == 'POST':
    form = NewIncomForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('income_list')
  
  else:
    form = NewIncomForm()

  context = {
    'form': form,
  }
  
  return render(request, 'transactions/add_income.html', context)

def expense_list(request):
  expenses = Expense.objects.all()

  context = {
    'expenses': expenses,
  }

  return render(request, 'transactions/expense_list.html', context)

def add_expense(request):
  if request.method == 'POST':
    form = NewExpenseForm(request.POST)

    if form.is_valid():
      form.save()

      return redirect('expense_list')
  
  else:
    form = NewExpenseForm()

  context = {
    'form': form,
  }

  return render(request, 'transactions/add_expense.html', context)