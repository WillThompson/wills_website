import os
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from subprocess import call

DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

## MAIN PAGE
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		data1 = request.form['test1']
		data2 = request.form['test2']
		return redirect(url_for('help', input1=data1, input2=data2))
	return render_template('home.html')

## ABOUT ME
@app.route('/aboutme', methods=['GET', 'POST'])
def about():
	return render_template('aboutme.html')

@app.route('/help?input1=<input1>+input2=<input2>',methods=['GET', 'POST'])
def help(input1,input2):
 	return render_template('dir_list.html',input1=input1,input2=input2)


@app.route('/dir_list/',methods=['GET', 'POST'])
def list_dir():

	from os import listdir
	from os.path import isfile, join
	onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
 	return render_template('dir_list.html',var1=onlyfiles)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
