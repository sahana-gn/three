#from django.shortcuts import render

# Create your views here.
# movies/views.py
from django.shortcuts import render
import requests

def search_movie(request):
    if request.method == 'POST':
        api_key = 'b14609ba'  # Get your API key from http://www.omdbapi.com/apikey.aspx
        search_query = request.POST.get('search_query')
        url = f'http://www.omdbapi.com/?apikey={api_key}&t={search_query}'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data['Response'] == 'True':
            movie_data = {
                'title': data['Title'],
                'year': data['Year'],
                'plot': data['Plot'],
                'poster': data['Poster'],
                'imdb_id': data['imdbID'],
            }
            return render(request, 'movies/movie_detail.html', {'movie': movie_data})
        else:
            error_message = 'Movie not found'
            return render(request, 'movies/movie_search.html', {'error_message': error_message})

    return render(request, 'movies/movie_search.html')
