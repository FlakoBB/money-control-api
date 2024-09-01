from rest_framework import serializers
from .models import User
from .forms import NewUserForm

class UserSerializer(serializers.ModelSerializer):
  password1 = serializers.CharField(write_only=True)
  password2 = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

  def validate(self, data):
    if data['password1'] != data['password2']:
      raise serializers.ValidationError('Las contraseñas no coinciden')
    return data
  
  def create(self, validated_data):
    form = NewUserForm({
      'username': validated_data['username'],
      'first_name': validated_data['first_name'],
      'last_name': validated_data['last_name'],
      'email': validated_data['email'],
      'password1': validated_data['password1'],
      'password2': validated_data['password2'],
    })

    if form.is_valid():
      user = form.save(commit=False)
      user.available_money = validated_data.get('available_money', 0)
      user.save()
      return user
    else:
      raise serializers.ValidationError(form.errors)
