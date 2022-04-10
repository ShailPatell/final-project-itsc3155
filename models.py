from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
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
