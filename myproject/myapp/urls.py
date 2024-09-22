# myapp/urls.py
# myapp/urls.py

from django.urls import path
from .views import bfhl

urlpatterns = [
    path('bfhl/', bfhl, name='bfhl'),
]
