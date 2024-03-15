from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from apps.post.models import Post, Comment
from apps.post.forms import CreateForm, PostSearchForm, CommentForm

from apps.user.views import login_req

def index(request):
    posts = Post.objects.filter(created_date__lte = timezone.now()).order_by('-created_date')
    search_form = PostSearchForm()
    if 'post_id' in request.GET:
        search_form = PostSearchForm(request.GET)
        if search_form.is_valid():
            return redirect('detail', id=search_form.data['post_id'])
    return render(request, 'index.html', {'posts': posts, 'search_form': search_form})

def detail(request, id):
    user = request.user
    if not user.is_authenticated:
        return login_req(request)
    
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post).order_by('-created_date')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Comment.objects.create(text=text, post=post, author=user, created_date=timezone.now())
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'post': post,
    'comments': comments, 'form': form, 'comments_count': len(comments)})

def search(request):
    user = request.user
    if not user.is_authenticated:
        return login_req(request)
    
    form = PostSearchForm()
    if 'post_id' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            return redirect('detail', id=form.data['post_id'])
    return render(request, 'search.html', {'form': form})

def create(request):
    user = request.user
    if not user.is_authenticated:
        return login_req(request)
    
    if not user.is_staff:
        return redirect('main')

    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('detail', id=post.id)
    else:
        form = CreateForm()
    return render(request, 'create.html', {'form': form})