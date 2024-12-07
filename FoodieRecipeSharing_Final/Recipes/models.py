#Recipes/Models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator # type: ignore
from django.conf import settings

from django.conf import settings # type: ignore
# Create your models here.
class RecipePost(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True) #User, on_delete=models.CASCADE
    difficulty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Restrict to 1-5
    description = models.TextField(default='')
    category = models.CharField(max_length=50, default='Uncategorized')
    ingredients = models.TextField()
    directions = models.TextField(default='')
    image = models.ImageField(upload_to='recipe/images/', blank=True, null=True)  # Optional image field
    created_at = models.DateTimeField(auto_now=True)
    # Define category choices
    CATEGORY_CHOICES = [
        ('Comfort Food', 'Comfort Food'),
        ('International Eats', 'International Eats'),
        ('Breakfast & Brunch', 'Breakfast & Brunch'),
        ('Community Picks', 'Community Picks'),
    ]
    title = models.CharField(max_length=200)  # Recipe title
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )  # Associated user, nullable and optional
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  # Difficulty level (1-5)
    description = models.TextField(default='')  # Brief description of the recipe
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='Uncategorized'
    )  # Recipe category with predefined choices
    ingredients = models.TextField()  # Ingredients list
    directions = models.TextField(default='')  # Step-by-step directions
    image = models.ImageField(
        upload_to='recipe/images/', 
        blank=True, 
        null=True
    )  # Optional recipe image
    created_at = models.DateTimeField(auto_now=True)  # Timestamp of creation

    def __str__(self):
        return self.title  # String representation of the model
    def difficulty_stars(self):
        return '★' * self.difficulty + '☆' * (5 - self.difficulty)
    
class Review(models.Model):
    recipe = models.ForeignKey(RecipePost, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'Review by {self.user.username} on {self.recipe.title}'
    
class Bookmark(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipe_bookmarks'  # Ensure uniqueness here
    )
    recipe = models.ForeignKey(
        RecipePost,
        on_delete=models.CASCADE,
        related_name='bookmarks'  # Change this to avoid conflict with 'bookmarked_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        unique_together = ('user', 'recipe')  # Prevent duplicate bookmarks
 
    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}" 