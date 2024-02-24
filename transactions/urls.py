from django.urls import path
from . import views

urlpatterns = [
  path('', views.income, name='income'),
  path('income/add/', views.add_income, name='add_income'),
  path('expense/list/', views.expense_list, name='expense_list'),
  path('expense/add/', views.add_expense, name='add_expense'),
]
