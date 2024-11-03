from django.urls import path
from .views import login_view, signup_view, post_review, update_review, delete_review

urlpatterns = [
    path('login/',login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('reviews/',post_review, name='reviews'),
    path('reviews/update/<int:pk>/',update_review, name='update_review'),
    path('reviews/delete/<int:pk>/',delete_review, name='delete_review'),
]

