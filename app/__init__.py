import os
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from subprocess import call
import numpy as np

DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

## MAIN PAGE
@app.route('/')
def home():
	return render_template('home.html')

## ABOUT ME
@app.route('/aboutme', methods=['GET', 'POST'])
def about():
	return render_template('aboutme.html')

@app.route('/compute', methods=['GET', 'POST'])
def compute():
	if request.method == 'POST':
		data1 = request.form['test1']
		return redirect(url_for('output', data=data1))
	return render_template('compute.html')


import StringIO
import base64
#import matplotlib.pyplot as plt
@app.route('/response?data=<data>', methods=['GET', 'POST'])
def output(data):
	data = [float(x) for x in data.split(",")]

	#img = StringIO.StringIO()

	#data = np.random.normal(0,1,100)
	#plt.clf()
	#makeplot(data)

	#plt.savefig(img, format='png')
	#img.seek(0)

	#plot_url = base64.b64encode(img.getvalue())

	op = np.mean(data)

 	return render_template('output.html',plot_url = data)


def makeplot(data):
	n, bins, patches = plt.hist(data, 50, normed=1, facecolor='g', alpha=0.75)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Plot Title')
	plt.grid(True)

# @app.route('/dir_list/',methods=['GET', 'POST'])
# def list_dir():

# 	from os import listdir
# 	from os.path import isfile, join
# 	onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
#  	return render_template('dir_list.html',var1=onlyfiles)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
