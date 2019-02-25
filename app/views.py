from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from app import app


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

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)