from django.urls import path
from . import views

urlpatterns = [
    path('', views.savings_progress, name='savings_progress'),
    path('delete/<int:pk>/', views.delete_entry, name='savings_delete'),
    path('edit/<int:pk>/', views.edit_entry, name='savings_edit'),
]
