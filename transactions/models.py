from django.db import models

class Income(models.Model):
  title = models.CharField(
    max_length=100,
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
  )
  date = models.DateTimeField(
    auto_now_add=True,
  )

  def __str__(self):
    return f'{self.title}: ${self.amount}'

class ExpenseCategory(models.Model):
  title = models.CharField(
    max_length=100,
  )
  description = models.TextField(
    null=True,
    blank=True,
  )

  def __str__(self):
    return self.title

class Expense(models.Model):
  title = models.CharField(
    max_length=100,
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
  )
  date = models.DateTimeField(
    auto_now_add=True,
  )
  taken_from = models.ForeignKey(
    'Income',
    on_delete=models.CASCADE,
  )
  is_necessary = models.BooleanField(
    default=False,
  )
  category = models.ForeignKey(
    'ExpenseCategory',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
  )

  def __str__(self):
    return f'{self.title}: ${self.amount}'
