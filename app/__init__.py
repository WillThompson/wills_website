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
@app.route('/aboutme')
def about():
	return render_template('aboutme.html')

@app.route('/compute', methods=['GET', 'POST'])
def compute():
	if request.method == 'POST':
		dat = request.form['rand']
		return redirect(url_for('output', data=dat))
	return render_template('compute.html')


import StringIO
import base64
#import matplotlib.pyplot as plt
@app.route('/response?data=<data>', methods=['GET', 'POST'])
def output(data):
	data = [int(x) for x in data.split(",")]
	op = performFrequencyTest(data)

 	return render_template('output.html',pval = op)

from scipy.stats import chisquare
def performFrequencyTest(data):
	N = len(data)
	m,M = min(data),max(data)
	counts = [data.count(x) for x in range(m,M+1)]
	expected = [float(N)/(M - m) for x in range(m,M+1)]
	p = chisquare(counts, expected)[1]
	return(p)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
