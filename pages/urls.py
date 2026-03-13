from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('learn/', views.learn_view, name='learn'),
]
