from models import User
from models import Pet
from models import db

class PetRepository:

    def create_user(self, user_username, user_password, first_name, last_name, user_age, user_gender, user_email_address):
        new_user = User(user_username=user_username, user_password=user_password, first_name=first_name, last_name=last_name, user_age=user_age, user_gender=user_gender, user_email_address=user_email_address)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def create_pet(self, pet_name, pet_age, pet_gender, pet_type, pet_breed, pet_health, pet_training, city, state, pet_about, pet_owner, photo):
        new_pet = Pet(pet_name=pet_name, pet_age=pet_age, pet_gender=pet_gender, pet_type=pet_type, pet_breed=pet_breed, pet_health=pet_health, pet_training=pet_training, city=city, state=state, pet_about=pet_about, pet_owner=pet_owner, photo=photo)
        db.session.add(new_pet)
        db.session.commit()
        return new_pet
    
    def get_user(self, user_id):
        result = User.query.get_or_404(user_id)
        return result
    
    def get_all_pets(self):
        all_pets = Pet.query.all()
        return all_pets

    def get_pet(self, pet_id):
        #result = db.session.query(Pet).filter_by(Pet.pet_id == 7)
        result = Pet.query.get_or_404(pet_id)
        return result


# Singleton to be used in other modules
pet_repository_singleton = PetRepository()
