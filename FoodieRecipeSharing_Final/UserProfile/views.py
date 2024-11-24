from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm

def home(request):
    return render(request, 'home/home.html')

def create_hardcoded_users_and_profiles():
    # Hardcoded user profiles (we will create user instances)
    users = [
        User(username='Alice', first_name='Alice', last_name='Smith', email='alice@example.com'),
        User(username='Bob', first_name='Bob', last_name='Brown', email='bob@example.com'),
        User(username='Charlie', first_name='Charlie', last_name='Johnson', email='charlie@example.com'),
    ]

    # Create users in the database if not already present
    for user in users:
        user, created = User.objects.get_or_create(username=user.username, defaults={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })

        # Create profiles for the hardcoded users if they don't already exist
        if created or not Profile.objects.filter(user=user).exists():
            Profile.objects.get_or_create(user=user, defaults={
                'bio': 'Food lover',
                'location': 'New York',
                'birth_date': '1990-01-01'
            })

def profile_list(request):
    # Call the function to create hardcoded users and profiles only if needed
    if not User.objects.filter(username='Alice').exists():  # Check if users already exist
        create_hardcoded_users_and_profiles()

    profiles = Profile.objects.all()  # Query the database for profiles
    return render(request, 'user_profile/profile_list.html', {'profiles': profiles})

def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'user_profile/profile_detail.html', {'profile': profile})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # Create a new user and profile
            new_user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email']
            )
            new_user.set_password(form.cleaned_data['password'])  # Set password
            new_user.save()
            new_profile = Profile(
                user=new_user,
                bio=form.cleaned_data['bio'],
                location=form.cleaned_data['location'],
                birth_date=form.cleaned_data['birth_date']
            )
            new_profile.save()  # Save the new profile
            return redirect('profile_list')  # Redirect to the profile list
    else:
        form = ProfileForm()  # Create a new form instance

    return render(request, 'user_profile/profile_create.html', {'form': form})  # Render the form
def profile_update(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # Save the updated profile
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'user_profile/profile_edit.html', {'form': form, 'profile': profile})

def profile_delete(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    profile.delete()  # Delete the profile
    return redirect('profile_list')
