from passlib.hash import sha512_crypt
import config

class User:

	def __init__(self, row):
		self.id = str(row[0])
		self.username = row[1]

		self.firstname = row[2]
		self.lastname = row[3]

		self.email = row[4]
		self.hashed_password = row[5]

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