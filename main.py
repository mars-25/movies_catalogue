from flask import Flask, render_template
import tmdb_client  # Import funkcji do pobierania filmów z TMDb

app = Flask(__name__)

@app.route('/')
def homepage():
    try:
        # ✅ Pobranie rzeczywistych popularnych filmów z API TMDb
        movies_data = tmdb_client.get_popular_movies()

        # 📌 Przetwarzanie danych — wyciągnięcie tytułu i plakatu
        movies = [{"title": movie.get("title", "Brak tytułu"), 
                   "image": tmdb_client.get_poster_url(movie.get("poster_path", ""), "w500")}
                  for movie in movies_data]

    except Exception as e:
        print(f"⚠️ Błąd pobierania danych: {e}")  # 🔍 Wyświetlanie błędu w konsoli
        movies = []  # 📌 Jeśli coś pójdzie nie tak, strona nie zawiesi się!

    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)