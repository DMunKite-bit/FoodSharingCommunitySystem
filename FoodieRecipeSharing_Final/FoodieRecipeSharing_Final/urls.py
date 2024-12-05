"""
URL configuration for FoodieRecipeSharing_Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Recipes.views import RecipePostCreateView, RecipePostListView, RecipePostUpdateView, RecipePostDeleteView, cuisine_view
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from LogIn.views import signup_view, login_view, logout_view
from RatingsAndReview.views import ratings_and_review, add_review, edit_review, delete_review  # Import correct views

urlpatterns = [
    # The other paths
    path('admin/', admin.site.urls),
    path('home/', include('HomePage.urls')),  # Homepage path (should be '/home/')
    path('ratings/', include('RatingsAndReview.urls')),
    path('recipelist', RecipePostListView.as_view(), name='recipe_list'),
    path('new/', RecipePostCreateView.as_view(), name='recipe_create'),
    path('<int:pk>/edit/', RecipePostUpdateView.as_view(), name='recipe_edit'),
    path('<int:pk>/delete/', RecipePostDeleteView.as_view(), name='recipe_delete'),
    path('cuisine/', cuisine_view, name='recipe_cuisine'),
    path('signup/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Change post_detail to ratings_and_review
    path('post/<int:post_pk>/', ratings_and_review, name='ratings_and_review'),  # Updated path
    path('post/<int:post_pk>/add_review/', add_review, name='add_review'),
    path('review/<int:pk>/edit/', edit_review, name='edit_review'),
    path('review/<int:pk>/delete/', delete_review, name='delete_review'),
    path('recipes/', include('Recipes.urls')),
     path('popular/', include('popular.urls')),
    path('', lambda request: redirect('login/', permanent=False)),  # Root URL redirect to '/home/'
]


if settings.DEBUG:  # This ensures it only runs in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)