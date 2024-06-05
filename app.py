from flask import Flask
from MainScores import MainScores

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to WorldOfGames"

@app.route('/scores')
def scores():
    return MainScores.score_server()
