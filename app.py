from flask import Flask, request, url_for, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)


@app.route('/')
def login():
    
    return "we getting shopify offer for fall 2021 baby!"