import flask


app = flask.Flask(__name__)

@app.route("/")

def index():
  return "This runs on the server you choose to on line 12"

if __name__ == "__main__":
  app.run(host="0.0.0.0")