from flask import render_template, Blueprint

app = Blueprint('index', 'index')

@app.route('/')
def index():
    return render_template("index.html")
