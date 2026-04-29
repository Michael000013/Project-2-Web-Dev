"""
Views for the movie application.
Handles rendering of movies, trailers, news, and sliders.
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Movie, Trailer, News, Slider


class HomeView(TemplateView):
    """Home page view displaying featured sliders, news, and movies."""
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['featured_news'] = News.objects.filter(is_featured=True)[:3]
        context['recent_movies'] = Movie.objects.all()[:6]
        context['latest_news'] = News.objects.all()[:5]
        return context
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        if email:
            print(f"New subscriber: {email}")
        return self.get(request, *args, **kwargs)


class MovieListView(ListView):
    """Display list of all movies."""
    model = Movie
    template_name = 'app/movielist.html'
    context_object_name = 'movies'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Movies'
        return context


class MovieDetailView(DetailView):
    """Display details of a single movie with its trailers."""
    model = Movie
    template_name = 'app/moviedetail.html'
    context_object_name = 'movie'
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trailers'] = self.object.trailers.all()
        context['related_movies'] = Movie.objects.exclude(pk=self.object.pk)[:4]
        return context


class TrailerView(TemplateView):
    """Display page with all trailers organized by movie."""
    template_name = 'app/trailers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_with_trailers'] = Movie.objects.filter(
            trailers__isnull=False
        ).distinct()
        return context


class NewsListView(ListView):
    """Display list of all news articles."""
    model = News
    template_name = 'app/news.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_news'] = News.objects.filter(is_featured=True)
        return context


class NewsDetailView(DetailView):
    """Display details of a single news article."""
    model = News
    template_name = 'app/newsdetail.html'
    context_object_name = 'article'
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_news'] = News.objects.exclude(pk=self.object.pk)[:3]
        return context
