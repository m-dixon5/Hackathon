from django.urls import path, include
from . import views
from user.views import create_post, edit_post, delete_post

urlpatterns = [
    path('', views.music_blog, name='music_blog'),
    path('create_post/', create_post, name='create_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('<slug:category_slug>/<slug:slug>/', views.details, name='details'),
    path('<slug:category_slug>/<slug:slug>/comment/',
         views.comment, name='comment'),
    path('<slug:category_slug>/<slug:slug>/delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('<slug:slug>/', views.Category, name='category'),
    path('summernote/', include('django_summernote.urls')),
]
