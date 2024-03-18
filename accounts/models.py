from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  available_money = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
  )

  def __str__(self):
    return f'{self.username}. Available money: ${self.available_money}'
