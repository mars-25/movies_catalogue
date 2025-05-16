#test_tmdb.py 
from unittest.mock import Mock
import requests, tmdb_client
import os
from dotenv import load_dotenv

load_dotenv
API_TOKEN = os.getenv("TMDB_API_TOKEN")

# Testowanie funkcji pobierania URL plakatu
def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w500'
    
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    
    assert expected_default_size in poster_url
    assert poster_url == f"https://image.tmdb.org/t/p/{expected_default_size}/{poster_api_path}"

# Pobieranie listy filmów z API TMDb
def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

# Testowanie pobierania listy filmów
def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None

# Funkcja do mockowania błędu
def some_function_to_mock():
    raise Exception("Original was called")

# Testowanie mockowania
def test_mocking(monkeypatch):
    my_mock = Mock()
    my_mock.return_value = 2
    monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
    
    result = some_function_to_mock()
    assert result == 2

# Testowanie mockowania zapytań do API TMDb
def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movies_list
    
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list

# Funkcja wywołująca API TMDb
def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

# Funkcja pobierająca listę filmów
def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


from unittest.mock import Mock
import tmdb_client

# Testowanie pobierania pojedynczego filmu
def test_get_single_movie(monkeypatch):
    mock_movie_data = {"id": 123, "title": "Test Movie", "overview": "Test description"}

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie_data

    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie = tmdb_client.get_single_movie(movie_id=123)
    assert movie == mock_movie_data
    assert movie["title"] == "Test Movie"

# Testowanie pobierania obrazów filmu
def test_get_movie_images(monkeypatch):
    mock_images_data = {"backdrops": [{"file_path": "image1.jpg"}, {"file_path": "image2.jpg"}]}

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_images_data

    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    images = tmdb_client.get_movie_images(movie_id=123)
    assert images == mock_images_data
    assert len(images["backdrops"]) == 2

# Testowanie pobierania obsady filmu
def test_get_single_movie_cast(monkeypatch):
    mock_cast_data = {"cast": [{"name": "Actor 1"}, {"name": "Actor 2"}]}

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_cast_data

    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    cast = tmdb_client.get_single_movie_cast(movie_id=123)
    assert cast == mock_cast_data["cast"]
    assert len(cast) == 2