import unittest

from instance.app import create_app
from api.user import User

class userTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		userTest.app = create_app('testing')

	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def test_user_creation(self):
		with userTest.app.app_context():

			username = "Ix"
			firstname = "Ford"
			lastname = "Prefect"
			email = "hoopy.frood@gmail.com"
			test_user = User(username, firstname, lastname, email)

			# make sure constructor assigns fields properly
			self.assertEqual(test_user.username, username, msg="User did not store username correctly")
			self.assertEqual(test_user.firstname, firstname, msg="User did not store firstname correctly")
			self.assertEqual(test_user.lastname, lastname, msg="User did not store lastname correctly")
			self.assertEqual(test_user.email, email, msg="User did not store email correctly")

			# adding a new user 
			# should work fine
			msg_user_success = "Added new user successfully."
			self.assertEqual(test_user.add()[1], msg_user_success, msg="User 1 not added successfully")

			# adding another user with the same first and last names, but different username and email
			# should work fine
			username = "Ix_v2"
			email = "gigatowel@hotmail.com"
			test_user_2 = User(username, firstname, lastname, email)
			self.assertEqual(test_user_2.add()[1], msg_user_success, msg="User 2 not added successfully")

			# adding a third user with new first and last names, but a repeat username and email
			# should not work
			firstname = "Notford"
			lastname = "Notprefect"
			test_user_3 = User(username, firstname, lastname, email)
			self.assertEqual(test_user_3.add()[0], None, msg="User with duplicate username/email allowed to add")