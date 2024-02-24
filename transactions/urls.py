from django.urls import path
from . import views

urlpatterns = [
  path('income/list/', views.income_list, name='income_list'),
  path('income/add/', views.add_income, name='add_income'),
  path('expense/list/', views.expense_list, name='expense_list'),
  path('expense/add/', views.add_expense, name='add_expense'),
]
