import flask
from threading import Thread
app = flask.Flask(__name__)


@app.route("/")
def index():
	return "Ayla made with ♥️ by 07"


def runapp():
	app.run("0.0.0.0", port=3000)


def run():
	Thread(target=runapp).start()
