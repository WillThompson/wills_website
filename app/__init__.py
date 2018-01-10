import os
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from subprocess import call

DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/')
def home():
  return render_template('home.html')

class ReusableForm(Form):
	name = TextField('Name:', validators=[validators.required()])

@app.route('/form/',methods=['GET', 'POST'])
def enter():

	form = ReusableForm(request.form)
	print(form.errors)

	if request.method == 'POST':
		usr = request.form['usr']
		name = request.form['name']
		typ = request.form['typ']

		print(usr + name + typ)
		print(os.getcwd())
		call("echo "+ usr + " -- " + name + " -- " + typ +" > filename.txt" , shell=True) 

 	return render_template('form.html',form=form)

@app.route('/dir_list/',methods=['GET', 'POST'])
def list_dir():

	from os import listdir
	from os.path import isfile, join
	onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
 	return render_template('dir_list.html',var1=onlyfiles,var2=os.getcwd())

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
