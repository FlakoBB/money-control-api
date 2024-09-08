from django.urls import path
from .views import RegisterIncomeView, IncomeListView

urlpatterns = [
  path('income/register/', RegisterIncomeView.as_view(), name='income_register'),
  path('income/list/', IncomeListView.as_view(), name='income_list'),
]