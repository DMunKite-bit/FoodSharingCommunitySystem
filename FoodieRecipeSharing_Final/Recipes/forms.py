from django import forms # type: ignore
from .models import RecipePost

class RecipePostForm(forms.ModelForm):
    class Meta:
        model = RecipePost
        fields = ['title', 'description', 'category', 'ingredients', 'directions', 'image']