import shodan
import json
import socket
from flask import Flask, render_template, request

ShodanKey = "DRfFk0rkKcMA6QUcHuUzeasGEjfZFQP0"

api = shodan.Shodan(ShodanKey)

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("frontend.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/testing")
def testing():
	return render_template("testing.html")

@app.route("/education")
def education():
	return render_template("education.html")


@app.route("/search", methods = ["POST"])
def search():
	value = request.get_json()
	if value ["loc"] == "":
		return
	else:
		print ("test")

		S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = S.connect_ex((value ["loc"], 1883))
		S.close()
		if result == 0:
			return("{\"value\":true}")
		else:
			return("{\"value\":false}")


@app.route("/check", methods = ["POST"])
def check():
	value = request.get_json()
	print (value)
	result = api.search(query="has_vuln:true ip:" + value ["loc"])
	print (result)
	if result["total"] > 0:
		return("{\"value\":true}")
	else:
		return("{\"value\":false}") 




if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 80, debug = True)

