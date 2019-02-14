from flask import Flask, request, render_template, redirect, jsonify, Response
import requests, json
import ipdb

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/', methods=['GET','POST'])

def post_user():
	if request.method == 'POST':
		feature1 = request.form['feature1']
		feature2 = request.form['feature2']
		feature3 = request.form['feature3']
		feature4 = request.form['feature4']	 

		input_data = {"feature1": feature1, "feature2": feature2, "feature3": feature3, "feature4": feature4}

		r = requests.post("http://api:8081", json=input_data)


	return jsonify(input_data)




if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 8080, debug = True, use_reloader = True)