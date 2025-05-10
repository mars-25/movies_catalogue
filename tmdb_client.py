import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYWQ2ODkzYjAyNzc3MmNlZjkxOWMxMzk1MDA4MGRhMiIsIm5iZiI6MTc0Njc4MTA4OC41NTksInN1YiI6IjY4MWRjM2EwN2YyNGFkYzU5ODNlY2M2YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.opLOBbk-AF07wqzzR0_HGgP72lqpkpwCaSdKoBcY_zA"  # Zamień na rzeczywisty token API

def get_popular_movies():
    """Pobiera listę popularnych filmów z TMDb API."""
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # 🚀 Sprawdzanie błędów HTTP (np. 401, 404)

        data = response.json()
        return data.get("results", [])  # 📌 Pobiera tylko listę filmów
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Błąd API TMDb: {e}")
        return []

def get_poster_url(poster_api_path, size="w500"):
    """Generuje pełny URL plakatu filmowego na podstawie 'poster_path' z TMDb API."""
    if not poster_api_path:
        return "https://via.placeholder.com/500x750?text=Brak+plakatu"  # 🔍 Domyślny placeholder

    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path.lstrip('/')}"  # ✅ Usunięcie zbędnego ukośnika
