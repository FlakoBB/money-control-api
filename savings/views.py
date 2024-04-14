from django.shortcuts import render, redirect
from .models import Saving, SavingAllocation, SavingWithdrawal

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
