from django.db import models
from accounts.models import User

class Income(models.Model):
  title = models.CharField(
    max_length=100,
  )
  description = models.TextField(
    blank=True,
    null=True,
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
  )
  date = models.DateTimeField(
    auto_now_add=True,
  )
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return f'{self.user.username}: {self.title}: ${self.amount}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    self.user.available_money += self.amount
    self.user.save()

class ExpenseCategory(models.Model):
  title = models.CharField(
    max_length=100,
  )
  description = models.TextField(
    null=True,
    blank=True,
  )
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.title

class Expense(models.Model):
  title = models.CharField(
    max_length=100,
  )
  category = models.ForeignKey(
    ExpenseCategory,
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
  )
  description = models.TextField(
    blank=True,
    null=True,
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
  )
  date = models.DateTimeField(
    auto_now_add=True,
  )
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return f'{self.user.username}: {self.title}: ${self.amount}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    self.user.available_money -= self.amount
    self.user.save()
