from django.db import models
from transactions.models import Income

class Saving(models.Model):
  title = models.CharField(
    max_length=100,
  )
  description = models.TextField(
    blank=True,
    null=True,
  )
  date = models.DateTimeField(
    auto_now_add = True,
  )
  amount_saving = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    blank=True,
    null=True,
  )

  def __str__(self):
    return f'{self.title}: ${self.amount_saving}'

class SavingAllocation(models.Model):
  taken_from = models.ForeignKey(
    Income,
    on_delete=models.CASCADE,
  )
  saving = models.ForeignKey(
    Saving,
    on_delete=models.CASCADE,
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
  )
  date = models.DateTimeField(
    auto_now_add=True,
  )

  def __str__(self):
    return f'{self.saving.title}: ${self.amount}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    self.taken_from.amount_available -= self.amount
    self.taken_from.save()

    self.saving.amount_saving += self.amount
    self.saving.save()

  def delete(self, *args, **kwargs):
    if self.taken_from.amount_available is not None:
      self.taken_from.amount_available += self.amount
      self.taken_from.save()

    self.saving.amount_saving -= self.amount
    self.saving.save()

    super().delete(*args, **kwargs)

class WishList(models.Model):
  title = models.CharField(
    max_length=100,
  )
  description = models.TextField(
    null=True,
    blank=True,
  )

  def __str__(self):
    return self.title

class WishListItem(models.Model):
  name = models.CharField(
    max_length=100,
  )
  price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
  )
  wish_list = models.ForeignKey(
    WishList,
    on_delete=models.CASCADE,
  )
  date = models.DateTimeField(
    auto_now_add=True,
  )

class SavingGoal(models.Model):
  title = models.CharField(
    max_length=100,
  )
  goal = models.DecimalField(
    max_digits=10,
    decimal_places=2,
  )
  current_amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
  )
  is_achieved = models.BooleanField(
    default = False
  )

  def __str__(self):
    return f'{self.title}: ${self.current_amount}/{self.goal}'
  
class SavingGoalAllocation(models.Model):
  taken_from = models.ForeignKey(
    Income,
    on_delete=models.CASCADE,
  )
  saving_goal = models.ForeignKey(
    SavingGoal,
    on_delete=models.CASCADE,
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
  )
  date = models.DateTimeField(
    auto_now_add=True,
  )

  def __str__(self):
    return f'{self.saving_goal.title}: ${self.amount}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    self.saving_goal.current_amount += self.amount
    self.saving_goal.save()

    self.taken_from.amount_available -= self.amount
    self.taken_from.save()

    if self.saving_goal.current_amount >= self.saving_goal.goal:
      self.saving_goal.is_achieved = True
      self.saving_goal.save()
