#Recipes/views.py
from django.urls import reverse_lazy  # type: ignore
from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin  # type: ignore # Add this import
from .models import RecipePost, Review , Bookmark
from .forms import RecipePostForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
import json
 

@csrf_exempt
def add_review(request, post_id):
    if request.method == "POST" and request.user.is_authenticated:
        try:
            data = json.loads(request.body)
            recipe = get_object_or_404(RecipePost, id=post_id)
            review_text = data.get("text", "").strip()
           
            if not review_text:
                return JsonResponse({"success": False, "error": "Review text cannot be empty."}, status=400)
 
            review = Review.objects.create(recipe=recipe, user=request.user, text=review_text)
            return JsonResponse({
                "success": True,
                "username": review.user.username,
                "review": review.text,
            })
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)
    return JsonResponse({"success": False, "error": "Invalid request."}, status=400)

class RecipePostListView(ListView):
    model = RecipePost
    template_name = 'recipes/recipePost_list.html'
    context_object_name = 'posts'
    paginate_by = 12
    
    def get_queryset(self):
        return RecipePost.objects.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            bookmarked_recipes = Bookmark.objects.filter(user=user).values_list('recipe_id', flat=True)
            context['bookmarked_recipes'] = set(bookmarked_recipes)
        else:
            context['bookmarked_recipes'] = set()
        return context

class RecipePostCreateView(LoginRequiredMixin, CreateView):
    model = RecipePost
    form_class = RecipePostForm
    template_name = 'recipes/recipePost_create.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
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
        'show_dropdown': True,  # Show dropdown for general browsing
    }
    return render(request, 'recipePost_cuisine.html', context)

def recipe_detail(request, pk):
    recipe = get_object_or_404(RecipePost, pk=pk)
    is_bookmarked = False
    if request.user.is_authenticated:
        is_bookmarked = Bookmark.objects.filter(user=request.user, recipe=recipe).exists()
    return render(request, 'recipes/recipe_details.html', {
        'recipe': recipe, 
        'is_bookmarked': is_bookmarked
    })

def recipe_by_category(request, category):
    recipes = RecipePost.objects.filter(category=category)
    context = {
        'recipes': recipes,
        'selected_category': category,
        'show_dropdown': False,  # Hide dropdown for "Explore More"
    }
    return render(request, 'recipePost_cuisine.html', context)
def recipe_list(request):
    posts = RecipePost.objects.all()  # or whatever your queryset is
    for post in posts:
        if post.difficulty is None:
            post.difficulty = 0  # You can set a default value if no difficulty is provided
    return render(request, 'recipe_list.html', {'posts': posts})
 
@csrf_exempt
def add_review(request, post_id):
    if request.method == "POST" and request.user.is_authenticated:
        try:
            data = json.loads(request.body)
            recipe = get_object_or_404(RecipePost, id=post_id)
            review_text = data.get("text", "").strip()
           
            if not review_text:
                return JsonResponse({"success": False, "error": "Review text cannot be empty."}, status=400)
 
            review = Review.objects.create(recipe=recipe, user=request.user, text=review_text)
            return JsonResponse({
                "success": True,
                "username": review.user.username,
                "review": review.text,
            })
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)
    return JsonResponse({"success": False, "error": "Invalid request."}, status=400)
 
@login_required
def add_bookmark(request, recipe_id):
    recipe = get_object_or_404(RecipePost, id=recipe_id)
    try:
        bookmark, created = Bookmark.objects.get_or_create(user=request.user, recipe=recipe)
        return JsonResponse({
            'success': True, 
            'message': 'Bookmark added successfully',
            'is_bookmarked': True
        })
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': str(e)
        }, status=400)

@login_required
def remove_bookmark(request, recipe_id):
    recipe = get_object_or_404(RecipePost, id=recipe_id)
    try:
        bookmark = Bookmark.objects.filter(user=request.user, recipe=recipe)
        if bookmark.exists():
            bookmark.delete()
            return JsonResponse({
                'success': True, 
                'message': 'Bookmark removed successfully',
                'is_bookmarked': False
            })
        return JsonResponse({
            'success': False, 
            'message': 'Bookmark not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False, 
            'message': str(e)
        }, status=400)

@login_required
def bookmark_list(request):
    """
    View to display a list of bookmarked recipes for the logged-in user
    """
    bookmarks = Bookmark.objects.filter(user=request.user)
    
    context = {
        'bookmarks': bookmarks,
    }
    
    return render(request, 'recipes/bookmark_list.html', context)
 
def search_recipes(request):
    # Display some initial recipes before search
    initial_recipes = RecipePost.objects.all()[:6]  # First 6 recipes
    
    # Check if there's a search query
    query = request.GET.get('q', '').strip()
    
    if query:
        # Search across multiple fields
        recipes = RecipePost.objects.filter(
            Q(title__icontains=query) |  # Search in title
            Q(ingredients__icontains=query) |  # Search in ingredients
            Q(description__icontains=query) |  # Search in description
            Q(category__icontains=query)  # Search in category
        )
    else:
        recipes = initial_recipes
    
    context = {
        'recipes': recipes,
        'query': query,
        'show_initial_results': not bool(query)  # Flag to show initial recipes
    }
    
    return render(request, 'recipes/search_recipes.html', context)