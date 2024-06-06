from flask import Flask
from MainScore import MainScore

app = Flask(__name__)

@app.route('/')
def score_page():
    return MainScore().score_server()


if __name__ == '__main__':
   app.run()
