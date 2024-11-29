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
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Change post_detail to ratings_and_review
    path('post/<int:post_pk>/', ratings_and_review, name='ratings_and_review'),  # Updated path
    path('post/<int:post_pk>/add_review/', add_review, name='add_review'),
    path('review/<int:pk>/edit/', edit_review, name='edit_review'),
    path('review/<int:pk>/delete/', delete_review, name='delete_review'),
    path('', lambda request: redirect('login/', permanent=False)),  # Root URL redirect to '/home/'
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)