import os
import requests                                                                                                                                                                                                                                                                                     #feito por messias
from flask import Flask, render_template, request
from dotenv import load_dotenv
                                                                                                                                                                                                                                                                                                                       #feito por messias
load_dotenv()                                                                                                                                                                                                                                                                                                                             #feito por messias                                                                                                                                                                                                                                                                                                                  #feito por messias

app = Flask(__name__)
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return render_template('index.html', movies=None)
    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}'
    response = requests.get(url)
    data = response.json()
    movies = data.get('results', [])
    return render_template('index.html', movies=movies, query=query)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'
    response = requests.get(url)
    movie = response.json()
    return render_template('detail.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
