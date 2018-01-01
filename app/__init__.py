from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/form/',methods=['GET', 'POST'])
def test():
	form = ReusableForm(request.form)
	print form.errors
	if request.method == 'POST':
		name=request.form['name']
		print name
 
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')
 	return render_template('form.html',form=form)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
