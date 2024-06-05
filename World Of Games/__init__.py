from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def score():
    try:
        with open("/score.txt", "a+") as f:
            f.seek(0)
            score = f.readline()
            if (not score.isdigit()):
                f.write('0')
                f.seek(0)
                score = f.readline()
        return render_template("score.html", score = score)
    except BaseException as error:
        return render_template("score.html", error = error.__repr__())


if __name__ == '__main__':
   app.run()