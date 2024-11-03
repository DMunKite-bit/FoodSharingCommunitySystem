from django.db import models # type: ignore
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings

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

    def __str__(self):
        return self.title