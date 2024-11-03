from django.contrib import admin
from .models import Post, Review  # Import the Review model

# Register your models here
admin.site.register(Post)
admin.site.register(Review)  # Register the Review model
