from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/mnist_playground/", methods=["GET", "POST"])
def mnist_playground():
    mousePostitions = request.json
    print(mousePostitions)
    return "Hello World."

app.run(debug=True)