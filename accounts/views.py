from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, NewUserForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer

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

# * API VIEWS
class RegisterView(APIView):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response({
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'available_money': user.available_money,
      }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class LoginView(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
  
class LogoutView(APIView):
  def post(self, request):
    try:
      token = request.auth
      token.delete()
      return Response(status=status.HTTP_200_OK)
    except AttributeError:
      return Response(status=status.HTTP_400_BAD_REQUEST)
