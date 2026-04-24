"""
Django admin configuration for the app.
Registers models and configures admin interface.
"""

from django.contrib import admin
from .models import Movie, Trailer, News, Slider


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin interface for Movie model."""
    list_display = ('title', 'genre', 'release_date', 'rating', 'director')
    list_filter = ('genre', 'release_date', 'rating')
    search_fields = ('title', 'director', 'cast')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'genre', 'release_date')
        }),
        ('Media', {
            'fields': ('cover_image',)
        }),
        ('Details', {
            'fields': ('rating', 'duration', 'director', 'cast')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    """Admin interface for Trailer model."""
    list_display = ('title', 'movie', 'uploaded_date')
    list_filter = ('movie', 'uploaded_date')
    search_fields = ('title', 'movie__title')
    readonly_fields = ('uploaded_date',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """Admin interface for News model."""
    list_display = ('title', 'author', 'is_featured', 'published_date')
    list_filter = ('is_featured', 'published_date', 'author')
    search_fields = ('title', 'content', 'author')
    readonly_fields = ('published_date', 'updated_date')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'content', 'image')
        }),
        ('Settings', {
            'fields': ('author', 'is_featured')
        }),
        ('Dates', {
            'fields': ('published_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    """Admin interface for Slider model."""
    list_display = ('title', 'order', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
    ordering = ('order',)


# Customize admin site
admin.site.site_header = "Movie Portal Admin"
admin.site.site_title = "Movie Portal"
admin.site.index_title = "Welcome to Movie Portal Administration"
