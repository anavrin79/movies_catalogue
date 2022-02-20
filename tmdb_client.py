import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYWYwZDM3NWIyZWRkMmJmZWQ1NTFlYTgxZGJiY2MyYiIsInN1YiI6IjYyMGY1MTU1Mzk2ZTk3MDAxYmI2ZWVjNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zJ1a4YSYBLNqCrfcAmnzVclWXP6y2t99vdzHiHLdlpo"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/top_rated"
    api_token = API_TOKEN
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

#def get_movie_details(id):
#    endpoint = "https://api.themoviedb.org/3/movie/{id}"
#    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYWYwZDM3NWIyZWRkMmJmZWQ1NTFlYTgxZGJiY2MyYiIsInN1YiI6IjYyMGY1MTU1Mzk2ZTk3MDAxYmI2ZWVjNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zJ1a4YSYBLNqCrfcAmnzVclWXP6y2t99vdzHiHLdlpo"
#    headers = {
#        "Authorization": f"Bearer {api_token}"
#    }
#    response = requests.get(endpoint, headers=headers)
#    return response.json()

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()
    
