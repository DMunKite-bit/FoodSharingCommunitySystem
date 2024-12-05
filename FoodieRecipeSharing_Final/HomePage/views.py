from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from Recipes.models import RecipePost  # Import the Recipe model

def index(request):
    return render(request, 'index.html')

def go_to_profile(request):
    return redirect('user_profile:profile_list')

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(RecipePost, id=recipe_id)
    return render(request, 'recipe_details.html', {'recipe': recipe})

def index(request):
    recipes = RecipePost.objects.all()[:8]  # Fetch the first six recipes
    return render(request, 'index.html', {'recipes': recipes})

# Create your views here.
