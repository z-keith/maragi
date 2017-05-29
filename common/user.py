from passlib.hash import sha512_crypt
from flask import jsonify

import config

class User:
	id = None
	username = None
	firstname = None
	lastname = None
	email = None
	hashed_password = None
	
	@property
	def is_active(self):
		return True

	@property
	def is_authenticated(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def hash_password(self, password):
		self.hashed_password =sha512_crypt.hash(password)

	def verify_password(self, password):
		return sha512_crypt.verify(password, self.password_hash)

	def to_json(self):
		return jsonify(id=self.id, username=self.username, firstname=self.firstname, lastname=self.lastname, email=self.email, hashed_password=self.hashed_password)

def user_from_json(json):
	user = User()

	user.id = json['id']
	user.username = json['username']

	user.firstname = json['firstname']
	user.lastname = json['lastname']

	user.email = json['email']
	user.hashed_password = json['hashed_password']

	return user

def user_from_db(row):
	user = User()

	user.id = str(row[0])
	user.username = row[1]

	user.firstname = row[2]
	user.lastname = row[3]

	user.email = row[4]
	user.hashed_password = row[5]

	return user