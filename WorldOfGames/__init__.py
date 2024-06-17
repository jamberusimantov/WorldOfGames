from flask import Flask
from .MainScore import MainScore
from sys import exit
from .Utils import SCORES_FILE

app = Flask(__name__)

@app.route('/')
def score_page():
    return MainScore.score_server()


@app.route('/score')
def score():
    try:
        with open(SCORES_FILE, "a+") as f:
            f.seek(0, 0)
            return f.readline() or '0'
    except BaseException as e:
        print(f"An error occurred: {e}")
        return '0'


if __name__ == '__main__':
   app.run()
