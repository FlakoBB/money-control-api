from django.shortcuts import render, redirect, get_object_or_404
from .models import Saving, SavingAllocation, SavingWithdrawal, SavingGoal, SavingGoalAllocation, SavingGoalWithdrawal, WishList, WishListItem

# * SAVING VIEWS
def saving_list(request):
  user = request.user

  savings = Saving.objects.filter(user=user)

  context = {
    'savings': savings,
  }

  return render(request, 'savings/all_savings.html', context)

def create_saving(request):
  user = request.user

  if request.method == 'POST':
    form = request.POST

    title = form['title']
    description = form['description']

    if title != '':
      if description != '':
        Saving.objects.create(title=title, description=description, user=user)
      else:
        Saving.objects.create(title=title, user=user)

      return redirect('savings')
    else:
      context = {
        'title_error': 'Debes definir un titulo.'
      }

      return render(request, 'savings/create_saving.html', context)
  
  return render(request, 'savings/create_saving.html')

def saving_details(request, saving_id):
  saving = Saving.objects.get(id=saving_id)

  context = {
    'saving': saving
  }

  return render(request, 'savings/saving_details.html', context)

def add_saving_funds(request, saving_id):
  user = request.user
  saving = Saving.objects.get(id=saving_id)

  context = {
    'saving_title': saving.title,
  }

  if request.method == 'POST':
    form = request.POST

    amount = int(form['amount']) if form['amount'] != '' else ''

    if amount != '':
      SavingAllocation.objects.create(user=user, saving=saving, amount=amount)
      return redirect('saving_details', saving_id)

    else:
      context['amount_error'] = 'Introduzca una cantidad valida.'

      return render(request, 'savings/add_saving_fund.html', context)
  
  return render(request, 'savings/add_saving_fund.html', context)

def withdraw_from_saving(request, saving_id):
  user = request.user
  saving = Saving.objects.get(id=saving_id)

  context = {
    'saving_title': saving.title,
  }

  if request.method == 'POST':
    form = request.POST

    amount = int(form['amount']) if form['amount'] != '' else ''

    if amount != '':
      SavingWithdrawal.objects.create(user=user, saving=saving, amount=amount)
      return redirect('saving_details', saving_id)

    else:
      context['amount_error'] = 'Introduzca una cantidad valida.'

      return render(request, 'savings/withdraw_from_saving.html', context)
  
  return render(request, 'savings/withdraw_from_saving.html', context)

# * SAVING GOALS VIEWS
def saving_goal_list(request):
  user = request.user

  saving_goals = SavingGoal.objects.filter(user=user)

  context = {
    'saving_goals': saving_goals,
  }

  return render(request, 'savings/saving_goals.html', context)

def create_saving_goal(request):
  user = request.user

  if request.method == 'POST':
    form = request.POST

    title = form['title']
    description = form['description']
    goal = int(form.get('goal') or 0)

    if goal != 0:
      if title != '':
        if description != '':
          SavingGoal.objects.create(title=title, goal=goal, description=description, user=user)
        else:
          SavingGoal.objects.create(title=title, goal=goal, user=user)

          return redirect('saving_goal_list')
      else:
        context = {
          'title_error': 'Debes definir un titulo.'
        }

        return render(request, 'savings/create_saving_goal.html', context)
      
    else:
      context = {
        'goal_error': 'Debes definir una meta.'
      }

      return render(request, 'savings/create_saving_goal.html', context)
  
  return render(request, 'savings/create_saving_goal.html')

def saving_goal_details(request, saving_goal_id):
  saving_goal = SavingGoal.objects.get(id=saving_goal_id)

  context = {
    'saving_goal': saving_goal
  }

  return render(request, 'savings/saving_goal_details.html', context)

def add_saving_goal_funds(request, saving_goal_id):
  user = request.user
  saving_goal = SavingGoal.objects.get(id=saving_goal_id)

  context = {
    'saving_title': saving_goal.title,
  }

  if request.method == 'POST':
    form = request.POST

    amount = int(form['amount']) if form['amount'] != '' else ''

    if amount != '':
      SavingGoalAllocation.objects.create(user=user, saving_goal=saving_goal, amount=amount)
      return redirect('saving_goal_details', saving_goal_id)

    else:
      context['amount_error'] = 'Introduzca una cantidad valida.'

      return render(request, 'savings/add_saving_goal_fund.html', context)
  
  return render(request, 'savings/add_saving_goal_fund.html', context)

def withdraw_from_saving_goal(request, saving_goal_id):
  user = request.user
  saving_goal = SavingGoal.objects.get(id=saving_goal_id)

  context = {
    'saving_title': saving_goal.title,
  }

  if request.method == 'POST':
    form = request.POST

    amount = int(form['amount']) if form['amount'] != '' else ''

    if amount != '':
      SavingGoalWithdrawal.objects.create(user=user, saving_goal=saving_goal, amount=amount)
      return redirect('saving_goal_details', saving_goal_id)

    else:
      context['amount_error'] = 'Introduzca una cantidad valida.'

      return render(request, 'savings/withdraw_from_saving_goal.html', context)
  
  return render(request, 'savings/withdraw_from_saving_goal.html', context)

def all_wish_list(request):
  user = request.user

  wish_lists = WishList.objects.filter(user=user)

  context = {
    'wish_lists': wish_lists
  }

  return render(request, 'savings/wish_lists.html', context)

def create_wish_list(request):
  user = request.user

  if request.method == 'POST':
    form = request.POST

    title = form['title']
    description = form['description']

    if title != '':
      if description != '':
        WishList.objects.create(title=title, description=description, user=user)
      else:
        WishList.objects.create(title=title, user=user)

      return redirect('all_wish_list')
    else:
      context = {
        'title_error': 'Debes definir un titulo.'
      }

      return render(request, 'savings/create_wish_list.html', context)
  
  return render(request, 'savings/create_wish_list.html')

def wish_list_details(request, wish_list_id):
  wish_list = WishList.objects.get(id=wish_list_id)

  items = WishListItem.objects.filter(wish_list=wish_list)

  context = {
    'wish_list': wish_list,
    'items': items
  }

  return render(request, 'savings/wish_list_details.html', context)

def add_item(request, wish_list_id):
  wish_list = WishList.objects.get(id=wish_list_id)

  context = {
    'wish_list': wish_list
  }

  if request.method == 'POST':
    form =  request.POST

    name = form['name']
    price = int(form.get('price') or 0)

    if name != '' and price != 0:
      WishListItem.objects.create(name=name, price=price, wish_list=wish_list)

      return redirect('wish_list_details', wish_list_id)
    
    else:
      if name == '':
        context['name_error'] = 'Debes asignar un nombre'
      
      if price == 0:
        context['price_error'] = 'Debes proporcionar un precio'

      return render(request, 'savings/add_item.html', context)
  
  return render(request, 'savings/add_item.html', context)

def delete_item(request, wish_list_id, item_id):
  item = get_object_or_404(WishListItem, id=item_id)

  item.delete()

  return redirect('wish_list_details', wish_list_id)
