from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from apps.post.models import Post

def login_req(request):
    return render(request, 'login_required.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def _login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect('main')
            else:
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def profile(request, id=None):
    user = request.user
    if not user.is_authenticated:
        return login_req(request)
    posts = Post.objects.filter(author=user)
    if id is not None:
        user = get_object_or_404(User, id=id)
        posts = Post.objects.filter(author=user).order_by('-created_date')
    return render(request, 'profile.html', {'posts': posts, 'user': user, 'id': id, 'post_count': len(posts)})

@login_required
def _logout(request):
    logout(request=request)
    return redirect('main')