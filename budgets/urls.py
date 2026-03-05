from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_overview, name='budget_overview'),
    path('setup/', views.budget_setup, name='budget_setup'),
    path('delete-expense/<int:pk>/', views.delete_expense, name='budget_delete_expense'),
]
