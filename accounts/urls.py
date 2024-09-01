from django.urls import path
from . import views

urlpatterns = [
  # path('login/', views.login_view, name='login'),
  # path('logout/', views.logout_view, name='logout'),
  # path('register/', views.register_view, name='register'),
  # * API URLS
  path('register/', views.RegisterView.as_view(), name='register'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('logout/', views.LogoutView.as_view(), name='logout'),
]
