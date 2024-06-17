from .Utils import SCORES_FILE, SCORES_HTML
from flask import render_template

# serve the user’s score currently in the scores.txt file over HTTP with HTML.
# This will be done by using python’s flask library.
class MainScore:

    def __init__(self):
        pass


    @staticmethod
    def score_server():
        try:
            with open(SCORES_FILE, "a+") as f:
                f.seek(0, 0)
                return render_template(SCORES_HTML, score = f.readline() or '0', username = "")
        except BaseException as e:
            print(f"An error occurred: {e}")
            return render_template(SCORES_HTML, error = e, username = "")
