from django.shortcuts import render, redirect
from .models import Income, Expense, ExpenseCategory
from .forms import NewExpenseForm

def income_list(request):
  user = request.user
  income = Income.objects.filter(user=user).order_by('-date')

  context = {
    'incomes': income,
  }

  return render(request, 'transactions/income_list.html', context)

def add_income(request):
  user = request.user

  context = {}
  
  if request.method == 'POST':
    form = request.POST

    if form['title'] != '' and form['amount'] != '':
      title = form['title']
      amount = int(form['amount'])
      description = form['description']

      Income.objects.create(user=user, title=title, amount=amount, description=description)

      return redirect('income_list')
    
    else:
      if form['title'] == '':
        title_error = 'El titulo es obligatorio.'
        
        context['title_error'] = title_error
      
      if form['amount'] == '':
        amount_error = 'Debes proporcionar una cantidad.'

        context['amount_error'] = amount_error

      return render(request, 'transactions/add_income.html', context)

  return render(request, 'transactions/add_income.html')

def expense_list(request):
  user = request.user
  expenses = Expense.objects.filter(user=user).order_by('-date')

  context = {
    'expenses': expenses,
  }

  return render(request, 'transactions/expense_list.html', context)

def add_expense(request):
  user = request.user

  categories = ExpenseCategory.objects.filter(user=user).values('id', 'title')

  context = {
    'categories': categories
  }
  
  if request.method == 'POST':
    form = request.POST

    if form['title'] != '' and form['amount'] != '':
      title = form['title']
      amount = int(form['amount'])
      category = int(form['category']) if form['category'] != '' else ''
      description = form['description']

      if category != '':
        expense_category = ExpenseCategory.objects.get(id=category)
        Expense.objects.create(user=user, title=title, amount=amount, description=description, category=expense_category)
      else:
        Expense.objects.create(user=user, title=title, amount=amount, description=description)
      return redirect('expense_list')
    
    else:
      if form['title'] == '':
        title_error = 'El titulo es obligatorio.'
        
        context['title_error'] = title_error
      
      if form['amount'] == '':
        amount_error = 'Debes proporcionar una cantidad.'

        context['amount_error'] = amount_error

      return render(request, 'transactions/add_expense.html', context)

  return render(request, 'transactions/add_expense.html', context)