from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_blog, name='music_blog'),
]