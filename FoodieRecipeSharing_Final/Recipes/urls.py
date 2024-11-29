from django.urls import path
from . import views

urlpatterns = [
    path('<str:category>/', views.category_recipes, name='category_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]