from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, NewUserForm

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request, request.POST)

    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        
        return redirect('home')
      
      else:
        return render(request, 'accounts/login.html', {'form': form, 'error_msj': 'Usuario o contraseña incorrectos'})
    
  else:
    form = LoginForm()
    
  return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('login')

def register_view(request):
  if request.method == 'POST':
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('login')
  
  else:
    form = NewUserForm()
  
  return render(request, 'accounts/register.html', {'form': form})
