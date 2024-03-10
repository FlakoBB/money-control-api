from typing import Any
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
  amount_available = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    blank=True,
    null=True,
  )

  def __str__(self):
    return f'{self.title}: ${self.amount_available}/{self.amount}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    self.amount_available = self.amount

    super().save(*args, **kwargs)

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
    Income,
    on_delete=models.CASCADE,
  )
  is_necessary = models.BooleanField(
    default=False,
  )
  category = models.ForeignKey(
    ExpenseCategory,
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
  )

  def __str__(self):
    return f'{self.title}: ${self.amount}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    self.taken_from.amount_available -= self.amount
    self.taken_from.save()
  
  def delete(self, *args, **kwargs):
    if self.taken_from.amount_available is not None:
      self.taken_from.amount_available += self.amount
      self.taken_from.save()

    super().delete(*args, **kwargs)
