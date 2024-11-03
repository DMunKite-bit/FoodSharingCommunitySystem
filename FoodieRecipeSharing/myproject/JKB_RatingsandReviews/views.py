from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm  # Make sure this is the correct import
from django.contrib import messages
from .models import Post, Review
from .forms import ReviewForm

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
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the specific Ratings and Comments page, adjust pk as needed
            return redirect('post_detail', pk=1)  # Use pk=1 or any default pk you want for the first login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    reviews = post.reviews.all()
    return render(request, 'RatingandCommenting.html', {
        'post': post,
        'reviews': reviews,
    })

@login_required
def add_review(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.user = request.user
            review.save()
            messages.success(request, "Review added successfully.")
            return redirect('post_detail', pk=post.pk)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    print("Review's Post ID:", review.post.pk)  # Debugging line to check if post.pk exists

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully.")
            return redirect('post_detail', pk=review.post.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form, 'review': review})



@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        post_pk = review.post.pk
        review.delete()
        messages.success(request, "Review deleted successfully.")
        return redirect('post_detail', pk=post_pk)
    return render(request, 'delete_review.html', {'review': review})

