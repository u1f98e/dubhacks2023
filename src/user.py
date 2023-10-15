from config import db
from src.model import User, user_schema

def get_users():
	users = User.query.all()
	return user_schema.dump(users, many=True)

def get_user(user_id):
	user = User.query.get(user_id)
	return user_schema.dump(user)

def create(user):
	new_user = User(name=user["name"], bio=user["bio"], image_url=user["image_url"])
	db.session.add(new_user)
	db.session.commit()
	return user_schema.dump(new_user)