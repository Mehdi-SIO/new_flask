#! /usr/bin/python


from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World !!'


@app.route('/hello/<phrase>')
def  hello(phrase):
	return phrase


@app.route('/contact/')
def contact():
	#mail = "abcd@gmial.com"
	tel = "01 02 03 04 05"
	return "Mail: {} --- Tel: {}".format(mail, tel)

if __name__ == '__main__'
	app.run(debug=True)