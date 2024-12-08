from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserUpdateForm
from .models import UserProfile
from Recipes.models import RecipePost
 
def user_recipes(request):
    # Get the recipes posted by the logged-in user
    user_recipes = RecipePost.objects.filter(user=request.user)

    return render(request, 'recipes/user_recipes.html', {
        'user_recipes': user_recipes,
    })
 
@login_required
def profile(request):
    # Fetch the user's profile (create if it doesn't exist)
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Fetch recipes added by the logged-in user
    user_recipes = RecipePost.objects.filter(user=request.user)

    return render(request, 'profile.html', {
        'profile': profile,
        'user_recipes': user_recipes  # Pass the recipes to the template
    })
 
@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'editprofile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,  # Pass the profile for the current image
    })