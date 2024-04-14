from django.urls import path
from . import views

urlpatterns = [
  path('all/', views.saving_list, name='savings'),
  path('create/', views.create_saving, name='create_saving'),
  path('details/<int:saving_id>', views.saving_details, name='saving_details'),
]