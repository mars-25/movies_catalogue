Opis projektu:
Aplikacja webowa stworzona w Flask, umożliwiająca przeglądanie filmów i ich szczegółowych informacji. Projekt wykorzystuje Bootstrap do estetycznego wyglądu i dynamicznego interfejsu. Dane o filmach pobierane są z The Movie Database (TMDb).


Wymagania
- Python 3.10+
- Flask
- Konto na TMDb, rejestracja: https://www.themoviedb.org/account/signup
- Klucz API TMDb, umieszczony w pliku .env 

Instalacja
1. Sklonuj repozytorium:
    git clone https://github.com/mars-25/movies_catalogue 
    cd movies_project 

2. Utwórz wirtualne środowisko.
    python -m venv movies_env
    source movies_env/bin/activate

3. Zainstaluj wymagane zależności:
    pip install -r requirements.txt

4. Utwórze plik .env i dodaj swój klucz API TMDb:
    TMDB_API_TOKEN=Twoj_Klucz_API

5. Uruchom aplikację:
    flask run
    Aplikacja uruchoma się na http://127.0.0.1:5000 

5. Testowanie:
    pytest test_tmdb.py -v


Autor: Marek Swachta 