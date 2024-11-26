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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('HomePage.urls')),
    path('profile/', include('UserProfile.urls')),
    path('recipelist', RecipePostListView.as_view(), name='recipe_list'),
    path('new/', RecipePostCreateView.as_view(), name='recipe_create'),
    path('<int:pk>/edit/', RecipePostUpdateView.as_view(), name='recipe_edit'),
    path('<int:pk>/delete/', RecipePostDeleteView.as_view(), name='recipe_delete'),
    path('cuisine/', cuisine_view, name='recipe_cuisine')
]

if settings.DEBUG:  # This ensures it only runs in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)