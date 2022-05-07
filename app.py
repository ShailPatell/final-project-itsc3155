import os
from flask_bcrypt import Bcrypt
from flask import Flask, session, abort, redirect, render_template, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from pymysql import NULL
from src.repositories.pet_repository import pet_repository_singleton, User, Pet

app = Flask(__name__)

load_dotenv()
db_user = os.getenv('DB_USER', 'root')
db_pass = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')

bcrypt = Bcrypt(app)
db.init_app(app)


@app.route("/")
def index():
    # ToDo:  Find a better way check for user being logged in
    return render_template('index.html', home_link=True)


@app.route('/browse')
def browse():
    all_pets = pet_repository_singleton.get_all_pets()
    return render_template('browse.html', browse_link=True, data=all_pets)


@app.post('/account')
def account():
    user_username = request.form.get('user_username', '')
    user_password = request.form.get('user_password', '')
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    user_age = request.form.get('user_age', type=int)
    user_gender = request.form.get('user_gender', '')
    user_email_address = request.form.get('user_email_address', '')
    created_user = pet_repository_singleton.create_user(
        user_username, user_password, first_name, last_name, user_age, user_gender, user_email_address)
    return render_template('account.html', account_link=True, data=created_user)

@app.route('/view_account')
def view_account(user_id):
    print(user_id)
    single_user = pet_repository_singleton.get_user(user_id)
    print(single_user)
    return render_template('account.html', account_link=True, data=single_user)


# @app.route('/petfinder')
# def petfinder():
#    return render_template('petfinder.html', adopt_link=True)

@app.route('/faq')
def faq():
    return render_template('faq.html', faq_link=True)

@app.route('/aboutus')
def about():
    return render_template('aboutus.html', about_link=True)


@app.get('/petpost')
def petpost():
    return render_template('petpost.html', post_link=True)

@app.post('/postpet')
def savepet():
    pet_name = request.form.get('pet_name', '')
    pet_type = request.form.get('pet_type', '')
    pet_gender = request.form.get('pet_gender', '')
    pet_age = 1
    pet_breed = request.form.get('pet_breed', '')
    pet_health = request.form.get('pet_health', '')
    pet_training = request.form.get('pet_training', '')
    city = request.form.get('city', '')
    state = request.form.get('state', '')
    pet_about = request.form.get('pet_about', '')
    pet_owner = session['user'].get('user_id')
    # Get thie image from the form

    image = request.files['photo']
    print(image.filename)

    if image:
        # save the image to the satic folder
        image.save(os.path.join('./static', image.filename))
        # write the image file to the database
        photo = image.filename
    else:
        photo = ''

    created_pet = pet_repository_singleton.create_pet(
        pet_name, pet_age, pet_gender, pet_type, pet_breed, pet_health, pet_training, city, state, pet_about, pet_owner, photo)
    return render_template('petview.html', post_link=True, data=created_pet)


@app.post('/postcomment')
def postcomment():
    comment_content = request.form.get('comment_content', '')
    pet_id = session.get('pet_id')
    owner = session['user'].get('user_id')

    comment = pet_repository_singleton.create_comment(owner,comment_content,pet_id)

    single_pet = pet_repository_singleton.get_pet(pet_id)
    comments = pet_repository_singleton.get_comments(pet_id)

    return render_template('petview.html',post_link=True, data=single_pet,comments=comments)

@app.post('/editpet')
def editpet():
    pet_name = request.form.get('pet_name', '')
    pet_type = request.form.get('pet_type', '')
    pet_gender = request.form.get('pet_gender', '')
    pet_age = 1
    pet_breed = request.form.get('pet_breed', '')
    pet_health = request.form.get('pet_health', '')
    pet_training = request.form.get('pet_training', '')
    city = request.form.get('city', '')
    state = request.form.get('state', '')
    pet_about = request.form.get('pet_about', '')

    pet_id = session.get('pet_id')

    pet_repository_singleton.update_pet(pet_id, pet_name, pet_age, pet_gender, pet_type, pet_breed, pet_health, pet_training, city, state, pet_about)

    single_pet = pet_repository_singleton.get_pet(pet_id)
    comments = pet_repository_singleton.get_comments(pet_id)

    return render_template('petview.html',browse_link=True, data=single_pet,comments=comments)

@app.post('/remove')
def deletepet():
    pet_id = session.get('pet_id')
    pet_repository_singleton.delete_pet(pet_id)
    return render_template('index.html',home_link=True)



@app.route('/petview/<int:pet_id>')
def petview(pet_id):
    session['pet_id'] = pet_id
    single_pet = pet_repository_singleton.get_pet(pet_id)
    comments = pet_repository_singleton.get_comments(pet_id)
    return render_template('petview.html', browse_link=True, data=single_pet,comments=comments)


@app.route('/login')
def login():
    return render_template('login.html')


@app.post('/login')
def loginuser():
    username = request.form.get('user_username', '')
    password = request.form.get('user_password', '')

    if username == '' or password == '':
        abort(400)

    existing_user = User.query.filter_by(user_username=username).first()
    print(existing_user)

    if not existing_user or existing_user.user_id == 0:
        return redirect('/login')

    if not bcrypt.check_password_hash(existing_user.user_password, password):
        return redirect('/login')

    session['user'] = {
        'username': username,
        'user_id': existing_user.user_id,
        'user_email': existing_user.user_email_address
    }
    print(session['user'].get('username'))
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.post('/reguser')
def reguser():

    user_username = request.form.get('user_username', '')
    user_password = request.form.get('user_password', '')
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    user_age = request.form.get('user_age', 0, type=int)
    user_gender = request.form.get('user_gender', '')
    user_email_address = request.form.get('user_email_address', '')

    # ToDo: Need to add better validation and handle exceptions.
    if user_username == '' or user_password == '':
        abort(400)

    hashed_password = bcrypt.generate_password_hash(
        user_password).decode('utf-8')

    created_user = pet_repository_singleton.create_user(
        user_username, hashed_password, first_name, last_name, user_age, user_gender, user_email_address)
    return redirect(f'/browse')

@app.route("/external-sources")
def external_sources():
    # ToDo:  Find a better way check for user being logged in
    return render_template('external-sources.html', ext_link=True)