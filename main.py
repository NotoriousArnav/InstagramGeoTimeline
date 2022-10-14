from flask import Flask
from blueprints import index, api

app = Flask(__name__)

app.register_blueprint(api.app)
app.register_blueprint(index.app)

@app.route("/ping")
def ping():
    return "pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
