from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from .models import Post, Review

def ratings_and_review(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    reviews = Review.objects.filter(post=post)
    return render(request, 'RatingsAndReview.html', {'reviews': reviews, 'post': post})

def add_review(request, post_pk):
    post = Post.objects.get(pk=post_pk)  
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post  
            review.user = request.user  
            review.save()
            return redirect('ratings_and_review', post_pk=post.pk)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'post': post})

@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully.")
            return redirect('ratings_and_review', post_pk=review.post.pk)
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
        return redirect('ratings_and_review', post_pk=post_pk)
    return render(request, 'delete_review.html', {'review': review})