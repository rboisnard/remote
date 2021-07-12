from flask import abort, Flask, render_template, request
from markupsafe import escape

# globals
app = Flask(__name__)
history = []

@app.route("/", methods=["GET"])
def home():
  "the home page returns the last event only"
  if request.method == "GET":
    if len(history):
      return render_template("home.html", event=history[-1]), 200
    else:
      return render_template("home.html", event="empty history"), 200

  else:
    abort(400)

@app.route("/history", methods=["GET"])
def get_history():
  "the history page returns all events with the latest first"
  if request.method == "GET":
    return render_template("history.html", history=history), 200

  else:
    abort(400)

@app.route("/ping", methods=["GET"])
def ping():
  "the ping url is used to keep the application alive"
  if request.method == "GET":
    return "", 200

  else:
    abort(400)

@app.route("/<input>", methods=["PUT"])
def update(input):
  "the update method url is called from the network to record the last event"
  if request.method == "PUT":
    input = escape(input)
    if len(history) == 0 or input != history[-1]:
      history.append(input)
    return "", 200

  else:
    abort(400)