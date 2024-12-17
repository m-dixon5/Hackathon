from django.shortcuts import render
from .models import Review
from .forms import CommentForm
from django.core.paginator import Paginator

# Create your views here.

def blog(request):
    all_posts = Post.objects.all().order_by('-created_at')
    featured_post = all_posts.first()
    paginator = Paginator(all_posts[1:],6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/blog.html',{'posts':posts, 'featured_post':featured_post})