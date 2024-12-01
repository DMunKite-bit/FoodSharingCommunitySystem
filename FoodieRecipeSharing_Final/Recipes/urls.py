from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
]