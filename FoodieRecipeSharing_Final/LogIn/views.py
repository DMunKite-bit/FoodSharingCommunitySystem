from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm 
from .models import Post
from LogIn.forms import UserRegistrationForm

def signup_view(request):
    """View for user signup."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserRegistrationForm()
    
    return render(request, 'Signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to ratings_and_review page after login
            # Replace '1' with the actual post ID or fetch the post dynamically if needed
            return redirect('HomePage:home')  # Or replace '1' with dynamic post ID
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'Login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


