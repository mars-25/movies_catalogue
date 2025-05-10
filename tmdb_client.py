import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYWQ2ODkzYjAyNzc3MmNlZjkxOWMxMzk1MDA4MGRhMiIsIm5iZiI6MTc0Njc4MTA4OC41NTksInN1YiI6IjY4MWRjM2EwN2YyNGFkYzU5ODNlY2M2YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.opLOBbk-AF07wqzzR0_HGgP72lqpkpwCaSdKoBcY_zA"  # Zamień na rzeczywisty token API

def get_movies_list(list_type="popular"):
    """Pobiera listę filmów z wybranego endpointu TMDb (np. 'popular', 'top_rated', 'now_playing')."""
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # ✅ Sprawdza błędy HTTP (np. 401, 404)
        return response.json().get("results", [])  # ✅ Pobiera tylko listę filmów
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Błąd API TMDb: {e}")
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