from flask import Flask, render_template, request
import tmdb_client  # Import funkcji do pobierania filmów z TMDb

app = Flask(__name__)

@app.context_processor
def utility_processor():
    """Dodaje funkcję `tmdb_image_url` do dostępnych funkcji w szablonie."""
    def tmdb_image_url(path, size="w500"):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    # Lista dozwolonych typów list filmów
    movie_categories = ["popular", "top_rated", "now_playing", "upcoming"]
    
    # Pobieramy wartość list_type z parametru URL
    list_type = request.args.get("list_type", "popular")
    
    # 🚀 Walidacja: jeśli użytkownik poda błędną kategorię, ustawiamy "popular"
    if list_type not in movie_categories:
        list_type = "popular"

    try:
        movies_data = tmdb_client.get_movies(12, list_type)  # ✅ Pobiera filmy zgodnie z wybraną kategorią

    except Exception as e:
        print(f"⚠️ Błąd pobierania danych: {e}")
        movies_data = []

    return render_template("homepage.html", movies=movies_data, list_type=list_type, movie_categories=movie_categories)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    try:
        details = tmdb_client.get_single_movie(movie_id)
        cast = tmdb_client.get_single_movie_cast(movie_id)
    except Exception as e:
        print(f"⚠️ Błąd pobierania szczegółów filmu: {e}")
        details, cast = None, []

    return render_template("movie_details.html", movie=details, cast=cast)

if __name__ == '__main__':
    app.run(debug=True)
