from django.urls import path
from . import views

urlpatterns = [
    path('', views.goals_overview, name='goals_overview'),
    path('create/', views.create_goal, name='create_goal'),
    path('<int:pk>/', views.goal_detail, name='goal_detail'),
    path('<int:pk>/edit/', views.edit_goal, name='edit_goal'),
    path('<int:pk>/delete/', views.delete_goal, name='delete_goal'),
    path('contribution/<int:pk>/delete/', views.delete_contribution, name='delete_contribution'),
    path('allocate/', views.allocate_budget, name='allocate_budget'),
    path('history/', views.allocation_history, name='allocation_history'),
]
