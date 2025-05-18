from unittest.mock import Mock
from main import app
import tmdb_client
import pytest

@pytest.mark.parametrize("list_type", ["popular", "top_rated", "now_playing", "upcoming"])
def test_homepage(monkeypatch, list_type):
    # Mockowanie funkcji get_movies
    api_mock = Mock(return_value=[])  # Zwraca pustą listę filmów
    monkeypatch.setattr(tmdb_client, "get_movies", api_mock)  # Podmieniamy get_movies

    with app.test_client() as client:
        # Tworzymy zapytanie, uwzględniając list_type w parametrze URL
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200  # Sprawdzamy, czy odpowiedź jest poprawna
        api_mock.assert_called_once_with(12, list_type)  # Sprawdzamy, czy mock został wywołany z odpowiednim parametrem
