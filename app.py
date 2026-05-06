from flask import Flask, request

app = Flask(__name__)

number = 50  # fast tall (du kan senere gjøre det tilfeldig)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        guess = int(request.form["guess"])

        if guess < number:
            return "For lavt"
        elif guess > number:
            return "For høyt"
        else:
            return "Riktig!"

    return '''
        <form method="POST">
            <input type="text" name="guess">
            <button type="submit">Gjett</button>
        </form>
    '''

