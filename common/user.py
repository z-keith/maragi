from passlib.hash import sha512_crypt
from flask import jsonify

import config
from db.database import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(24), unique=True)
	firstname = db.Column(db.String(20))
	lastname = db.Column(db.String(20))
	email = db.Column(db.String(64))
	hashed_password = db.Column(db.String(120))

	def __init__(self, id, username, firstname, lastname, email, hashed_password):
		self.id = id
		self.username = username
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.hashed_password = hashed_password
	
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
		return str(self.id)

	def hash_password(self, password):
		self.hashed_password =sha512_crypt.hash(password)

	def verify_password(self, password):
		return sha512_crypt.verify(password, self.password_hash)

	def to_json(self):
		return jsonify(id=self.id, username=self.username, firstname=self.firstname, lastname=self.lastname, email=self.email, hashed_password=self.hashed_password)

def user_from_json(json):
	id = json['id']
	username = json['username']

	firstname = json['firstname']
	lastname = json['lastname']

	email = json['email']
	hashed_password = json['hashed_password']

	return User(id, username, firstname, lastname, email, hashed_password)

def init_users():
	arthur = User(1, 'mustbethursday', 'Arthur', 'Dent', 'bewareofleopard@yahoo.com', '$6$rounds=656000$4zRd68HDkcQMoo3A$Ovlvva/VdfsJKZK6/sYAIoFnUcL6Cbpoh35wf2n4TZ1OAAgAo/DkBgxiMK1qKb4r/MxytGMgX4UfMg2JyQlNe0')
	fenchurch = User(2, 'AnArtToFlying', 'Fenchurch', '', 'nomorenails@outlook.com', '$6$rounds=656000$4zRd68HDkcQMoo3A$Ovlvva/VdfsJKZK6/sYAIoFnUcL6Cbpoh35wf2n4TZ1OAAgAo/DkBgxiMK1qKb4r/MxytGMgX4UfMg2JyQlNe0')
	ford = User(3, 'Ix', 'Ford', 'Prefect', 'unpleasantlydrunk@gmail.com', '$6$rounds=656000$4zRd68HDkcQMoo3A$Ovlvva/VdfsJKZK6/sYAIoFnUcL6Cbpoh35wf2n4TZ1OAAgAo/DkBgxiMK1qKb4r/MxytGMgX4UfMg2JyQlNe0')
	marvin = User(4, 'oh_no', 'Marvin', 'the Paranoid Android', 'GPP.0042@siriuscybernetics.com', '$6$rounds=656000$4zRd68HDkcQMoo3A$Ovlvva/VdfsJKZK6/sYAIoFnUcL6Cbpoh35wf2n4TZ1OAAgAo/DkBgxiMK1qKb4r/MxytGMgX4UfMg2JyQlNe0')

	db.session.add(arthur)
	db.session.add(fenchurch)
	db.session.add(ford)
	db.session.add(marvin)

	db.session.commit()