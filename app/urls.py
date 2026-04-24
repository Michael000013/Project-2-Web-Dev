"""
URL configuration for the app.
"""

from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # Home page
    path('', views.HomeView.as_view(), name='home'),

    # Movies
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),

    # Trailers
    path('trailers/', views.TrailerView.as_view(), name='trailers'),

    # News
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
]
