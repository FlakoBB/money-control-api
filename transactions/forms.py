from django.forms import ModelForm
from .models import Income, Expense

class NewIncomForm(ModelForm):
  class Meta:
    model = Income
    fields = '__all__'

class NewExpenseForm(ModelForm):
  class Meta:
    model = Expense
    fields = '__all__'
