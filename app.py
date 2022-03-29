from flask import Flask, redirect, render_template, request

app = Flask(__name__)


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
