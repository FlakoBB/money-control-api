from django.urls import path
from .views import RegisterIncomeView, IncomeListView, ResgisterExpenseView, ExpenseListView

urlpatterns = [
  path('income/register/', RegisterIncomeView.as_view(), name='income_register'),
  path('income/list/', IncomeListView.as_view(), name='income_list'),
  path('expense/register/', ResgisterExpenseView.as_view(), name='expense_register'),
  path('expense/list/', ExpenseListView.as_view(), name='expense_list'),
]