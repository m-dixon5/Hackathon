from django.shortcuts import render, get_object_or_404, redirect
from .models import Review, Category, Comment
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.

def music_blog(request):
    all_posts = Review.objects.all().order_by('-created_at')
    featured_post = all_posts.first()
    paginator = Paginator(all_posts[1:], 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'music_blog/blog.html', {'posts': posts, 'featured_post': featured_post})

def details(request, category_slug, slug):
    post = get_object_or_404(Review, slug=slug, category__slug=category_slug)
    comments = post.comments.all()
    form = CommentForm()
    return render(request, 'music_blog/details.html', {'post': post, 'comments': comments, 'form': form})

def comment(request, category_slug, slug):
    post = get_object_or_404(Review, slug=slug, category__slug=category_slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('details', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()
    comments = post.comments.all()
    return render(request, 'music_blog/details.html', {'post': post, 'comments': comments, 'form': form})

def delete_comment(request, category_slug, comment_id, slug):
    comment = get_object_or_404(Comment, id=comment_id, post__slug=slug, post__category__slug=category_slug)
    if request.method == 'POST' and comment.user == request.user:
        comment.delete()
        return redirect('details', category_slug=category_slug, slug=slug)