from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

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



