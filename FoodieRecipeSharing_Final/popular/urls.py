# popular/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.popular, name='popular'),  # The popular page
]
