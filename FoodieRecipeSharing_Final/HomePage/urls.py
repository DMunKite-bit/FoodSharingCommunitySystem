from django.urls import path
from . import views

app_name = 'HomePage'

urlpatterns = [
    path('', views.index, name='index'),  # Root URL points to the index view
]
