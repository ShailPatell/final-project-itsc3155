from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html',home_link=True)

@app.route('/petfinder')
def petfinder():
    return render_template('petfinder.html',adopt_link=True)

@app.route('/postpet')
def postpet():
    return render_template('postpet.html')

@app.route('/petview')
def petview():
    return render_template('petview.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')
