from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def go_to_profile(request):
    return redirect('user_profile:profile_list')

# Create your views here.
