from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form=AuthenticationForm()
        return render(request, "users/login.html", {"form":form})
    
def logout_view(request):
    if request.method=="POST":
        logout(request)
    return redirect("home")

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'users/profile.html', context)

@login_required
def profile_edit(request, username):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile_edit.html', {'form': form})