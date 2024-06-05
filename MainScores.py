from Utils import SCORES_FILE


def html_template(data):
    return (
        "<html><head><title>Scores Game</title></head><body>"
        "<h1>The score is <div id='score'>" + data + "</div></h1></body></html>"
    )


class MainScores:
    @staticmethod
    def score_server():
        try:
            f = open(SCORES_FILE, "a")
            f.close()
            f = open(SCORES_FILE)
            score = f.readline()
            f.close()
            return html_template(score)
        except IOError:
            return html_template(str(IOError.args))
