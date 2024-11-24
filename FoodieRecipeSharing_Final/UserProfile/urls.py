# user_profile/urls.py
from django.urls import path
from .views import profile_list, profile_detail, profile_create, profile_update, profile_delete
from . import views

app_name = 'UserProfile'
urlpatterns = [
    path('profiles/', views.profile_list, name='profile_list'),
    path('profile/<str:username>/', profile_detail, name='profile_detail'),
    path('create/', profile_create, name='profile_create'),
    path('edit/<str:username>/', profile_update, name='profile_update'),
    path('delete/<str:username>/', profile_delete, name='profile_delete'),
]
