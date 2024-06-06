from Utils import SCORES_FILE, SCORES_HTML
from flask import render_template

# serve the user’s score currently in the scores.txt file over HTTP with HTML.
# This will be done by using python’s flask library.
class MainScore:
    def __init__(self):
        pass

    # serve the score.
    # It will read the score from the scores file and will return an HTML
    @staticmethod
    def score_server():
        try:
            with open(SCORES_FILE, "a+") as f:
                f.seek(0, 0)
                score = f.readline()
                return render_template(SCORES_HTML, score = score)
        except BaseException:
            print(BaseException.args)
            return render_template(SCORES_HTML, error = BaseException.__repr__())
