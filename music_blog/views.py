from django.shortcuts import render
from .models import Review, Category
from django.core.paginator import Paginator

# Create your views here.

def music_blog(request):
    all_posts = Review.objects.all().order_by('-created_at')
    featured_post = all_posts.first()
    paginator = Paginator(all_posts[1:],6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'music_blog/blog.html',{'posts':posts, 'featured_post':featured_post})
