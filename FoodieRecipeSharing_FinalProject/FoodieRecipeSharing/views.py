from django.urls import reverse_lazy  # type: ignore
from django.views.generic import ListView, CreateView  # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin  # type: ignore # Add this import
from .models import RecipePost
from .forms import RecipePostForm

class RecipePostListView(ListView):
    model = RecipePost
    template_name = 'recipes/recipePost_list.html'
    context_object_name = 'posts'

class RecipePostCreateView(CreateView):  # Add LoginRequiredMixin
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'recipes/recipePost_create.html'
    success_url = reverse_lazy('recipe_list')
