from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class RecipePost(models.Model):
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
