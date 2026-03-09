from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from blog.models import Posts
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import logout

def blog_landing(request):
    return render(request=request, template_name="blog_index.html")

def list_posts(request):
    posts = Posts.objects.all()
    return render(request=request, template_name='posts.html', context={'posts': posts})

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})



@login_required
def post_update(request, pk):
    """
    View to handle editing an existing post.
    """
    post = get_object_or_404(Post, pk=pk) # Get the specific post or show a 404 error
    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to edit this post.Only author can perform action")
    if request.method == 'POST':
        # Populate the form with submitted data AND the existing post instance
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home') # Redirect to the homepage after saving
    else:
        # Populate the form with the existing post's data
        form = PostForm(instance=post)
    
    # Pass the form to a template
    return render(request, 'post_update.html', {'form': form})

@login_required
def post_delete(request, pk):
    """
    View to handle deleting a post.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to delete this post.Only author can perform action")
    if request.method == 'POST': # Only process if the form was submitted
        post.delete()
        return redirect('home')
    # If it's a GET request, you might show a confirmation page,
    # but we'll handle confirmation in the template for simplicity.
    return redirect('home') # Or render a confirmation template

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')

