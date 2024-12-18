from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Profile
from .forms import UserProfileForm
from music_blog.forms import PostForm
from music_blog.models import Review  
from music_blog.views import music_blog


# Create your views here.

@login_required
def view_profile(request):
    profile,created = Profile.objects.get_or_create(user=request.user)
    posts = Review.objects.filter(author=request.user)
    paginator = Paginator(posts,6)
    page_number = request.GET.get('page')
    user_posts = paginator.get_page(page_number)

    return render(request, 'user/profile.html', {'profile':profile, 'user_posts':user_posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
        
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():

            form.save()
            return redirect('details', category_slug=post.category.slug, slug=post.slug)
        
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete() 
        return redirect('blog')
    
    return render(request, 'blog/delete_post.html', {'post': post})
