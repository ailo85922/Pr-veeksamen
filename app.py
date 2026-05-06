from flask import Flask, render_template, request
import random

app = Flask(__name__)

number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])

        if guess < number:
            message = "For lavt"
        elif guess > number:
            message = "For høyt"
        else:
            message = "Riktig!"

    return render_template("index.html", message=message)