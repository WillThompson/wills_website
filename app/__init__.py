import os
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['USERNAME'] = 'will'
app.config['PASSWORD'] = 'passcode'


## MAIN PAGE
@app.route('/')
def home():
	return render_template('home.html')

## INTERESTS
@app.route('/interests/')
def interests():
	return render_template('interests.html')

## PUBLICATIONS
@app.route('/publications/')
def publications():
	return render_template('publications.html')

## PUBLICATIONS
@app.route('/more/')
def more():
	return render_template('more.html')

## LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    if error:
    	flash(error)
    return render_template('login.html')

## LOGOUT
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
