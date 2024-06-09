from django.urls import path
from . import views

urlpatterns = [
  # * SAVING URLS
  path('all/', views.saving_list, name='savings'),
  path('create/', views.create_saving, name='create_saving'),
  path('details/<int:saving_id>/', views.saving_details, name='saving_details'),
  path('<int:saving_id>/add/', views.add_saving_funds, name='add_saving_funds'),
  path('<int:saving_id>/withdraw/', views.withdraw_from_saving, name='withdraw_from_saving'),
  # * SAVING GOALS URLS
  path('saving-goals/', views.saving_goal_list, name='saving_goal_list'),
  path('saving-goals/create/', views.create_saving_goal, name='create_saving_goal'),
  path('saving-goals/details/<int:saving_goal_id>/', views.saving_goal_details, name='saving_goal_details'),
  path('saving-goals/<int:saving_goal_id>/add/', views.add_saving_goal_funds, name='add_saving_goal_funds'),
  path('saving-goals/<int:saving_goal_id>/withdraw/', views.withdraw_from_saving_goal, name='withdraw_from_saving_goal'),
]
