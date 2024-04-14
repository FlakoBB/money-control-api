from django.shortcuts import render, redirect
from .models import Saving

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
