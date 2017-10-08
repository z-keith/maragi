from passlib.hash import sha512_crypt

from instance.db import db

class User(db.Model):

	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(24), unique=True)
	email = db.Column(db.String(80))
	hashed_password = db.Column(db.String(120))
	
	firstname = db.Column(db.String(64))
	lastname = db.Column(db.String(64))

	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    	onupdate=db.func.current_timestamp())

	def __init__(self, username, firstname, lastname, email, hashed_password=None):
		self.username = username
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.hashed_password = hashed_password


	# next few functions needed for flask-login	
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
		return str(self.user_id)


	# authentication functions
	def hash_password(self, password):
		self.hashed_password =sha512_crypt.hash(password)

	def verify_password(self, password):
		return sha512_crypt.verify(password, self.password_hash)


	# database interaction functions
	def add(self):
		db.session.add(self)
		db.session.commit()

		return True