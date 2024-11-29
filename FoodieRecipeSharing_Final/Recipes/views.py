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

class RecipePostCreateView(CreateView):  # Add LoginRequiredMixin
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'recipes/recipePost_create.html'
    success_url = reverse_lazy('recipe_list')

class RecipePostUpdateView(UpdateView):
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'recipes/recipePost_update.html'
    success_url = reverse_lazy('recipe_list')

class RecipePostDeleteView(DeleteView):
    model = RecipePost
    template_name = 'recipes/recipePost_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')

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
