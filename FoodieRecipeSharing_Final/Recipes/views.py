from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin  # type: ignore # Add this import
from .models import RecipePost
from .forms import RecipePostForm
from django.shortcuts import render

class RecipePostListView(ListView):
    model = RecipePost
    template_name = 'recipes/recipePost_list.html'
    context_object_name = 'posts'

class RecipePostCreateView(LoginRequiredMixin, CreateView):  # Add LoginRequiredMixin
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'recipes/recipePost_create.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class RecipePostUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'recipes/recipePost_update.html'
    success_url = reverse_lazy('recipe_list')

    def get_queryset(self):
        # Restrict updates to recipes owned by the logged-in user
        return self.model.objects.filter(user=self.request.user)

class RecipePostDeleteView(LoginRequiredMixin, DeleteView):
    model = RecipePost
    template_name = 'recipes/recipePost_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')

    def get_queryset(self):
        # Restrict deletions to recipes owned by the logged-in user
        return self.model.objects.filter(user=self.request.user)

def cuisine_view(request):
    # Get all unique categories from the RecipePost model
    categories = RecipePost.objects.values_list('category', flat=True).distinct()
    
    # Get the selected category from the GET request
    selected_category = request.GET.get('category', None)
    
    # Filter recipes by the selected category, or display all recipes if no category is selected
    if selected_category:
        recipes = RecipePost.objects.filter(category=selected_category)
    else:
        recipes = RecipePost.objects.all()
    
    context = {
        'categories': categories,
        'recipes': recipes,
        'selected_category': selected_category,
    }
    return render(request, 'recipePost_cuisine.html', context)

    # Recipe list view for a specific category
def category_recipes(request, category):
    recipes = RecipePost.objects.filter(category=category)
    context = {
        'recipes': recipes,
        'category': category,
    }
    return render(request, 'recipes/category_recipes.html', context)

    # Recipe detail view
def recipe_detail(request, recipe_id):
    recipe = RecipePost.objects.get(id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)

def recipes_by_category(request, category):
    recipes = RecipePost.objects.filter(category=category)
    return render(request, 'Recipes/category_recipes.html', {'recipes': recipes, 'category': category})
