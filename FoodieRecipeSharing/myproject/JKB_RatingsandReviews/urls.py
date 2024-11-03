from django.urls import path
from JKB_RatingsandReviews.views import login_view, signup_view, post_detail, add_review, edit_review, delete_review

urlpatterns = [
    path('', login_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/add_review/', add_review, name='add_review'),
    path('review/<int:pk>/edit/', edit_review, name='edit_review'),
    path('review/<int:pk>/delete/', delete_review, name='delete_review'),
]
