from django.shortcuts import render, redirect
from .models import Income
from .forms import NewIncomForm

def income(request):
  income = Income.objects.all()
  return render(request, 'transactions/index.html', {'incomes': income})

def add_income(request):
  if request.method == 'POST':
    form = NewIncomForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('income')
  
  else:
    form = NewIncomForm()
  
  return render(request, 'transactions/add_income.html', {'form': form})
