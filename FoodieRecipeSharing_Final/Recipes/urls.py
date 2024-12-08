#Recipes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('cuisine/', views.cuisine_view, name='recipe_cuisine'),
    path('cuisine/<str:category>/', views.recipe_by_category, name='recipe_by_category'),
    path('bookmark/add/<int:recipe_id>/', views.add_bookmark, name='add_bookmark'),
    path('bookmark/remove/<int:recipe_id>/', views.remove_bookmark, name='remove_bookmark'),
    path('bookmarks/', views.bookmark_list, name='bookmark_list'),
    path('search/', views.search_recipes, name='recipe_search'),
    path('reviews/', views.reviews_list, name='reviews_list'),
]