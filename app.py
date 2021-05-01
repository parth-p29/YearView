from flask import Flask, request, url_for, redirect, render_template, flash, session
from flask_pymongo import PyMongo
import random, string, base64

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://parthpatel:parth2911@shopifybackendchallange.dz8by.mongodb.net/YearView?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
mongo = PyMongo()
mongo.init_app(app) 

app.secret_key = ''.join(random.choice(string.ascii_letters) for i in range(10))

@app.route('/')
def login():
    
    return render_template('login.html', form_text="Login to YearView", button_text="Login", action='/check')

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == "POST":

        collection = mongo.db.data

        password = request.form['password']
        username = request.form['username']
        name = request.form['name']

        if password != request.form['confirm pass']:
 
            flash("Passwords don't match.")
            return redirect(url_for('signup'))

        if collection.find_one({"username": username}):

            flash("Username already exists, please try another one.")
            return redirect(url_for('signup'))
        
        else:
            configure_user = {
                "name" : name,
                "username": username,
                "password": base64.b64encode(password.encode("utf-8"))
            }

            collection.insert_one(configure_user)

        flash("Account Created!")
        return redirect(url_for('login'))

    return render_template('signup.html', form_text="Create Account", button_text="Create", action='/signup')

@app.route('/check', methods=["POST"])
def check():

    collection = mongo.db.data

    username = request.form['username']
    password = request.form['password']

    user = collection.find_one({'username': username})

    if user:
        
        user_pass = base64.b64decode(user['password'])
        decoded_pass = user_pass.decode('utf-8')
        
        if password == decoded_pass:

            session['user'] = user['name']
            return redirect(url_for('user'))
            
        else:
            
            flash("Incorrect Password.")
            return redirect(url_for('login'))
    
    else:

        flash("Username not found.")
        return redirect(url_for('login'))


@app.route('/user')
def user():

    if 'user' not in session:

        flash("Please login or create an account.")
        return redirect(url_for('login'))

    user = session['user']

    return render_template('main.html', name=user)

    
