from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello from Git+Docker+Jenkins"

if __name__="__main":
	app.run(debug=True)
