import unittest

from instance.app import create_app
from common.user import User

class userTest(unittest.TestCase):

	def setUp(self):
		self.app = create_app('testing')

	def tearDown(self):
		pass
	
	def test_user_creation(self):
		with self.app.app_context():

			username = "Ix"
			firstname = "Ford"
			lastname = "Prefect"
			email = "hoopy.frood@gmail.com"

			test_user = User(username, firstname, lastname, email)

			assert test_user.username == username
			assert test_user.firstname == firstname
			assert test_user.lastname == lastname
			assert test_user.email == email

			assert test_user.add() == True