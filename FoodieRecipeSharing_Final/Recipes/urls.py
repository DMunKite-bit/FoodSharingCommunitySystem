#Recipes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('cuisine/', views.cuisine_view, name='recipe_cuisine'),
    path('cuisine/<str:category>/', views.recipe_by_category, name='recipe_by_category'),
]