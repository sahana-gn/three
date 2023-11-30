# movie_search/urls.py
from django.urls import path
from movies.views import search_movie

urlpatterns = [
    path('search/', search_movie, name='search_movie'),
]
