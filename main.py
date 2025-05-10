from flask import Flask, render_template
import tmdb_client  # Import funkcji do pobierania filmów z TMDb

app = Flask(__name__)

@app.context_processor
def utility_processor():
    """Dodaje funkcję `tmdb_image_url` do dostępnych funkcji w szablonie."""
    def tmdb_image_url(path, size="w500"):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}  # ✅ Dzięki temu można używać tej funkcji w HTML

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=13)
    return render_template("homepage.html", movies=movies)

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    return render_template("movie_details.html", movie=details)

if __name__ == '__main__':
    app.run(debug=True)
