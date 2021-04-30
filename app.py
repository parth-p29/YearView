from flask import Flask, request, url_for, redirect, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://parthpatel:parth2911@shopifybackendchallange.dz8by.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
mongodb = PyMongo(app)
app.secret_key = 'yessir'

@app.route('/')
def login():
    
    return render_template('login.html')

@app.route('/signup')
def signup():

    return 'hi'