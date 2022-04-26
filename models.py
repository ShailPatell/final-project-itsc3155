from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, nullable=False,primary_key=True)
    user_username = db.Column(db.String, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    user_gender = db.Column(db.String, nullable=False)
    user_email_address = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'User({self.user_id},{self.user_password}, {self.user_username}, {self.first_name}, {self.last_name},{self.user_age}, {self.user_gender}, {self.user_email_address})'

class Pet(db.Model):

    __tablename__ = 'pet'

    pet_id = db.Column(db.Integer, nullable=False,primary_key=True)
    pet_name = db.Column(db.String, nullable=False)
    pet_age = db.Column(db.Integer, nullable=False)
    pet_gender = db.Column(db.String, nullable=False)
    pet_type = db.Column(db.String, nullable=False)
    pet_breed = db.Column(db.String, nullable=False)
    pet_health = db.Column(db.String, nullable=False)
    pet_training = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    pet_about = db.Column(db.String, nullable=False)
    pet_owner = db.Column(db.Integer,db.ForeignKey('user.user_id'), nullable=False)
    owner= db.relationship('User',backref='pets',lazy=True)
    photo = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Pet({self.pet_id},{self.pet_name}, {self.pet_age}, {self.pet_gender}, {self.pet_type}, {self.pet_breed}, {self.pet_health}, {self.pet_training}, {self.city}, {self.state}, {self.pet_about}, {self.pet_owner}, {self.photo} )'


class Comment(db.Model):

    __tablename__ = 'comment'

    comment_id = db.Column(db.Integer, nullable=False,primary_key=True)
    comment_content = db.Column(db.String, nullable=False)
    author_id= db.Column(db.Integer,db.ForeignKey('user.user_id'), nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('pet.pet_id'), nullable=False)
    post = db.relationship('Pet',backref='posts_comments',lazy=True)
    author = db.relationship('User', backref='user_id',lazy=True)


    def __repr__(self):
        return f'User({self.comment_id },{self.author_id},{self.comment_content} {self.post_id})'