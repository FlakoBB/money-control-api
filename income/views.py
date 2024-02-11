from django.shortcuts import render
from .models import Income

def income(request):
  income = Income.objects.all()
  return render(request, 'income/index.html', {'incomes': income})
