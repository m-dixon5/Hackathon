from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

@login_required
def view_profile(request):
    profile,created = Profile.objects.get_or_create(user=request.user)
    posts = Post.objects.filter(author=request.user)
    paginator = Paginator(posts,6)
    page_number = request.GET.get('page')
    user_posts = paginator.get_page(page_number)

    return render(request, 'user/profile.html', {'profile':profile, 'user_posts':user_posts})
