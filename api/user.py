from passlib.hash import sha512_crypt
from sqlalchemy.exc import IntegrityError, DataError

from instance.db import db

class User(db.Model):

	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(24), unique=True)
	email = db.Column(db.String(80), unique=True)
	hashed_password = db.Column(db.String(120))
	
	firstname = db.Column(db.String(64))
	lastname = db.Column(db.String(64))

	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    	onupdate=db.func.current_timestamp())
	deleted = db.Column(db.Boolean, default=False)

	def __init__(self, username, firstname, lastname, email, hashed_password=None):
		self.username = username
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.hashed_password = hashed_password

	def validate(self):
		if "@" not in self.email:
			return False, ["Invalid email"]
		return True, None

	# next few functions needed for flask-login	
	@property
	def is_active(self):
		return not self.deleted

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
		valid, messages = self.validate()
		if not valid:
			return None, messages
		try:
			db.session.add(self)
			db.session.commit()
			return self.user_id, "Added new user successfully."
		except IntegrityError as e:
			db.session.rollback()
			return None, str(e.orig.diag.message_primary)
		except:
			db.session.rollback()
			return None, "An unknown error occurred."

	@staticmethod
	def reactivate(id):
		user = User.query.filter_by(user_id=id).first()
		if user:
			user.deleted = False
			db.session.commit()
			return user, "User found and activated."
		else:
			return None, "No user found with that ID."

	@staticmethod
	def get_all():
		return User.query.all()

	@staticmethod
	def get_by_id(id):
		try:
			return_val = User.query.filter_by(user_id=id, deleted=False).first()
			if return_val == None:
				return None, "No active user with that ID."
			return return_val, "User found successfully."
		except DataError as e:
			return None, str(e.orig.diag.message_primary)
		except:
			return None, "An unknown error occurred."

	def edit(self, username=None, firstname=None, lastname=None, email=None):
		if self.deleted:
			return None, "User previously deleted."

		if username:
			self.username = username
		if firstname:
			self.firstname = firstname
		if lastname:
			self.lastname = lastname
		if email:
			self.email = email

		valid, messages = self.validate()
		if not valid:
			db.session.rollback()
			return None, messages

		try:
			db.session.commit()
			return self, "User edited successfully."
		except:
			db.session.rollback()
			return None, "An unknown error occurred."

	def delete(self):
		if self.deleted:
			return None, "User already deleted."
		self.deleted = True
		db.session.commit()
		return self.user_id, "User deleted successfully."