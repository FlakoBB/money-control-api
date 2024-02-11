from django.urls import path
from . import views

urlpatterns = [
  path('', views.income, name='income'),
  path('add/income/', views.add_income, name='add_income'),
]
