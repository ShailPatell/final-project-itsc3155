from models import User
from models import db

class PetRepository:

    def create_user(self, user_username, user_password, first_name, last_name, user_age, user_gender, user_email_address):
        # TODO create a new movie in the DB
        new_user = User(user_username=user_username, user_password=user_password, first_name=first_name, last_name=last_name, user_age=user_age, user_gender=user_gender, user_email_address=user_email_address)
        db.session.add(new_user)
        db.session.commit()
        return new_user


# Singleton to be used in other modules
pet_repository_singleton = PetRepository()
