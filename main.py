from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [{"title": f"Film {i}", "image": f"film_{i}.jpg"} for i in range(1, 24)]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)