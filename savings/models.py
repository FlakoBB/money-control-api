from django.db import models
from django.core.exceptions import ValidationError
from transactions.models import Income
from accounts.models import User

class Saving(models.Model):
  title = models.CharField(
    max_length=100,
  )
  description = models.TextField(
    blank=True,
    null=True,
  )
  amount_saving = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0,
    blank=True,
    null=True,
  )
  creation_date = models.DateTimeField(
    auto_now_add = True,
  )
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return f'{self.user.username}: {self.title}: ${self.amount_saving}'
  
  def delete(self, *args, **kwargs):
    if self.amount_saving > 0:
      self.user.available_money += self.amount_saving
      self.user.save()

    super().delete(*args, **kwargs)

class SavingAllocation(models.Model):
  user = models.ForeignKey(
    User,
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

    if self.user.available_money >= self.amount:
      self.user.available_money -= self.amount
      self.user.save()
    else:
      raise ValidationError("The amount exceeds the user's available money.")

    self.saving.amount_saving += self.amount
    self.saving.save()

class SavingWithdrawal(models.Model):
  user = models.ForeignKey(
    User,
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
    return f'{self.amount}'

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.saving.amount_saving >= self.amount:
      self.user.available_money += self.amount
      self.user.save()

      self.saving.amount_saving -= self.amount
      self.saving.save()
    else:
      raise ValidationError('The amount exceeds the saving total amount.')

class SavingGoal(models.Model):
  title = models.CharField(
    max_length=100,
  )
  description = models.TextField(
    blank=True,
    null=True,
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
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return f'{self.title}: ${self.current_amount}/{self.goal}'
  
  def delete(self, *args, **kwargs):
    if self.current_amount > 0:
      self.user.available_money += self.current_amount
      self.user.save()

    super().delete(*args, **kwargs)
  
class SavingGoalAllocation(models.Model):
  user = models.ForeignKey(
    User,
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
    return f'{self.user.username}: {self.saving_goal.title}: ${self.amount}'
  
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.user.available_money >= self.amount:
      self.user.available_money -= self.amount
      self.user.save()
      
      self.saving_goal.current_amount += self.amount
      if self.saving_goal.current_amount >= self.saving_goal.goal:
        self.saving_goal.is_achieved = True
      self.saving_goal.save()
    else:
      raise ValidationError("The amount exceeds the user's available money.")

class SavingGoalWithdrawal(models.Model):
  user = models.ForeignKey(
    User,
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
    return f'{self.amount}'

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.saving_goal.current_amount >= self.amount:
      self.user.available_money += self.amount
      self.user.save()

      self.saving_goal.current_amount -= self.amount
      if self.saving_goal.current_amount < self.saving_goal.goal:
        self.saving_goal.is_achieved = False
      self.saving_goal.save()
    else:
      raise ValidationError('The amount exceeds the saving goal current amount.')

class WishList(models.Model):
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
    return f'{self.user.username}: {self.title}'

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

  def __str__(self):
    return f'{self.wish_list.title}: {self.name}'
