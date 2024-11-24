# admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

# Unregister the default User admin
admin.site.unregister(User)

# Create a custom User admin
class UserAdmin(BaseUserAdmin):
    # You can customize the fields displayed in the admin
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')

# Register the customized User admin
admin.site.register(User, UserAdmin)

# Register your Profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date')
    search_fields = ('user__username', 'bio')
