from flask import Flask, request, url_for, redirect, render_template, flash
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://parthpatel:parth2911@shopifybackendchallange.dz8by.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
mongodb = PyMongo(app)
app.secret_key = 'yessir'

@app.route('/')
def login():
    
    return render_template('login.html', form_text="Login to YearView", button_text="Login", action='/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']

        if password != request.form['confirm pass']:
 
            flash("Passwords don't match", 'bad')

            return redirect(url_for('signup'))

        flash("Account Created!", "good")
        return redirect(url_for('login', _external=True))


    return render_template('signup.html', form_text="Create Account", button_text="Create", action='/signup')