from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field 

# Create your models here.

class Category(models.Model):
    """
    Represents a music genre category for live events
    """
    GENRE_CHOICES = [
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('hip-hop', 'Hip-Hop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('electronic', 'Electronic'),
        ('blues', 'Blues'),
        ('metal', 'Metal'),
        ('reggae', 'Reggae'),
        ('folk', 'Folk'),
        ('punk', 'Punk'),
        ('indie', 'Indie'),
        ('rnb', 'R&B'),
        ('country', 'Country'),
        ('soul', 'Soul'),
        ('funk', 'Funk'),
        ('latin', 'Latin'),
        ('world', 'World Music'),
        ('house', 'House'),
        ('techno', 'Techno'),
    ]
    title = models.CharField(max_length=30, choices=GENRE_CHOICES, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.get_title_display()
    
    def get_absolute_url(self):
        return f"/{self.slug}"

class Review(models.Model):
    """
    Represents music blog posts
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='media/blog')
    slug = models.SlugField(default='')
    content = CKEditor5Field('Content', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    location = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug



