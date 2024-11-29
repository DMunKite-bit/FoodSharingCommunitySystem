from django.urls import path
from . import views

app_name = 'RatingsAndReview'

urlpatterns = [
    path('post/<int:post_pk>/reviews/', views.ratings_and_review, name='ratings_and_review'),
    path('post/<int:post_pk>/add_review/', views.add_review, name='add_review'),
    path('review/<int:pk>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:pk>/delete/', views.delete_review, name='delete_review'),
]
