import requests
import os 
from dotenv import load_dotenv 
load_dotenv() #Wczytuje zmienne z pliku .env

API_TOKEN = os.getenv("TMDB_API_TOKEN")

def get_movies_list(list_type="popular"):
    """Pobiera listę filmów z TMDb."""
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        data = response.json()  # Pobranie danych z API

        # 🔹 Sprawdź, czy `data` jest słownikiem, jeśli tak, pobierz 'results'
        if isinstance(data, dict) and "results" in data:
            return data["results"]
        
        return data  # Jeśli nie ma 'results', zwróć oryginalną wartość

    except requests.exceptions.RequestException as e:
        print(f"Błąd pobierania danych z TMDb: {e}")
        return []

def get_movies(how_many, list_type="popular"):
    """Zwraca określoną liczbę filmów z wybranej listy."""
    data = get_movies_list(list_type)  # ✅ Pobiera dane z wybranego endpointu TMDb
    return data[:how_many]  # ✅ Zwraca tylko pierwsze `how_many` filmów

def get_single_movie(movie_id):
    """Pobiera szczegóły pojedynczego filmu z TMDb API."""
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()  # ✅ Zwraca szczegóły filmu jako słownik
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Błąd API TMDb: {e}")
        return None

def get_single_movie_cast(movie_id):
    """Pobiera obsadę pojedynczego filmu."""
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("cast", [])  # ✅ Pobiera tylko listę aktorów
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Błąd API TMDb: {e}")
        return []

def get_poster_url(poster_api_path, size="w500"):
    """Generuje pełny URL plakatu filmowego na podstawie 'poster_path' z TMDb API."""
    if not poster_api_path:
        return "https://via.placeholder.com/500x750?text=Brak+plakatu"  # 🔍 Domyślny placeholder

    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path.lstrip('/')}"  # ✅ Usunięcie zbędnego ukośnika

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()