from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import HomePage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",HomePage.as_view(), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)