#! /usr/bin/python


from flask import Flask
from flask import redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "<h3>Hello World !!</h3>"


@app.route('/hello/<phrase>')
def  hello(phrase):
	return phrase

@app.route('/google')
def redirection_google():
	return redirect('http://www.google.fr')


if __name__ == '__name__':
	app.run(debug=True)
