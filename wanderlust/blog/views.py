from django.shortcuts import render,redirect,get_object_or_404 
from .forms import PostForm
from django.http import HttpResponse
from blog.models import Posts
from .models import Post # Make sure Post is imported
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 

def blog_index(request):
    return render(request=request, template_name="blog_index.html")
def get_post(request):
    all_posts = Posts.objects.all()
    return render(request=request,template_name='posts.html',context={'posts':all_posts})
def create_post(request):
    print("Test",dir(request))
    title=request.POST.get('title')
    content=request.POST.get('content')
    return render(request=request, template_name='new_post.html')
def home(request):
    posts = Post.objects.all().order_by('-created_at') # Get all posts, newest first
    return render(request, 'home.html', {'posts': posts})
# Create your views here.
@login_required
def content_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Create a post object but DON'T save it to the database yet
            post = form.save(commit=False)
            
            # Assign the current logged-in user to the author field
            post.author = request.user
            
            # Now, save the post to the database with the author included
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