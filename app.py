import os
from flask import Flask, redirect, render_template, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

load_dotenv()
db_user = os.getenv('DB_USER','root')
db_pass = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def index():
    return render_template('index.html', home_link=True)


@app.route('/browse')
def browse():
    return render_template('browse.html', browse_link=True)


@app.route('/petfinder')
def petfinder():
    return render_template('petfinder.html', adopt_link=True)


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.get('/petpost')
def petpost():
    return render_template('petpost.html', post_link=True)


@app.post('/petview')
def petview():
    return render_template('petview.html')


@app.route('/login')
def login():
    return render_template('login.html')
