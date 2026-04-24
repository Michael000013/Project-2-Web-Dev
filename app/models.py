"""
Models for the movie application.
Defines Movie, Trailer, News, and Slider models.
"""

from django.db import models
from django.core.validators import URLValidator

class Movie(models.Model):
    """Movie database model for storing movie information."""
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='movies/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    duration = models.IntegerField(help_text="Duration in minutes")
    director = models.CharField(max_length=200)
    cast = models.TextField(help_text="Comma-separated list of actors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-release_date']
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title


class Trailer(models.Model):
    """Trailer model for storing movie trailers linked to movies."""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='trailers')
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='trailers/', blank=True, null=True)
    duration = models.IntegerField(help_text="Duration in seconds", default=0)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_date']

    def __str__(self):
        return f"{self.movie.title} - {self.title}"


class News(models.Model):
    """News model for storing entertainment news and updates."""
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    author = models.CharField(max_length=200, default='Admin')
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Slider(models.Model):
    """Slider model for managing hero/banner slider images."""
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='slider/')
    link_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Order of appearance in slider")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Slide {self.id}"
