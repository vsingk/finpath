from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('savings/', include('savings.urls')),
    path('budgets/', include('budgets.urls')),
    path('goals/', include('goals.urls')),  # NEW: Savings goals
    path('', include('pages.urls')),
]
