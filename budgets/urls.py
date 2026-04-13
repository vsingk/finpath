from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_overview, name='budget_overview'),
    path('setup/', views.budget_setup, name='budget_setup'),
    path('delete-expense/<int:pk>/', views.delete_expense, name='budget_delete_expense'),
    path('projected-budget/<str:n>/<str:i>/<str:a>/', views.projected_Budget, name='projected_budget'),
    path('monthly-deposit-project/<str:monthlyDeposit>/<str:goalAmount>/<str:interestRate>/', views.monthlyDepositProject, name='monthlyDepositProject')


]
