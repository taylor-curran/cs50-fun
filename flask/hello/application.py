from flask import Flask, render_template

# Flask, turn the current file into an application
app = Flask(__name__)

# A Route is a URL
@app.route("/")
def index():
    return render_template("index.html")