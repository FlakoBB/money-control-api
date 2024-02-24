from django.forms import ModelForm
from .models import Income

class NewIncomForm(ModelForm):
  class Meta:
    model = Income
    fields = '__all__'
