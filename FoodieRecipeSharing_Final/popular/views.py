# popular/views.py

from django.shortcuts import render
from Recipes.models import RecipePost   # Adjust to import from the correct model

def popular(request):
    # Assuming you want to display the recipes with the highest difficulty
    recipes = RecipePost.objects.order_by('-difficulty')[:5]
    return render(request, 'recipes/popular_recipes.html', {'recipes': recipes})