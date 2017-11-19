import unittest

from instance.app import create_app
from api.user import User

class userTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		#userTest.app = create_app('testing')
		pass

	def setUp(self):
		userTest.app = create_app('testing')

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

			# adding a third user with new first and last names and email, but a repeat username
			# should not work
			firstname = "Notford"
			lastname = "Notprefect"
			email = "unused_email@gmail.com"
			test_user_3 = User(username, firstname, lastname, email)
			self.assertEqual(test_user_3.add()[0], None, msg="User with duplicate username allowed to add")

			# adding a fourth user with new username, but a repeat email
			# should not work
			username = "Ix_v4"
			email = "gigatowel@hotmail.com"
			test_user_4 = User(username, firstname, lastname, email)
			self.assertEqual(test_user_4.add()[0], None, msg="User with duplicate email allowed to add")

	def test_user_get_all(self):
		with userTest.app.app_context():
			all_users = User.get_all()
			
			# Should be a list of 4 User objects
			self.assertIsInstance(all_users, list, msg="User.get_all() did not return a list")
			for user in all_users:
				self.assertIsInstance(user, User, msg="User.get_all() contained a non-User object")
			self.assertEqual(len(all_users), 4, msg="User.get_all() did not return 4 Users")

	def test_user_get_by_id(self):
		with userTest.app.app_context():
			# valid IDs
			user1, u1_msg = User.get_by_id(1)
			self.assertIsInstance(user1, User, msg="User.get_by_id() returned a non-User object")
			self.assertEqual(user1.username, 'mustbethursday', msg="User.get_by_id() returned the wrong user")
			user3, u3_msg = User.get_by_id(3)
			self.assertIsInstance(user3, User, msg="User.get_by_id() returned a non-User object")
			self.assertEqual(user3.username, 'Ix_prime', msg="User.get_by_id() returned the wrong user")

			# invalid IDs
			user5, u5_msg = User.get_by_id(5)
			self.assertIsNone(user5, msg="User.get_by_id() did not return None for a nonexistant ID")
			self.assertEqual(u5_msg, "No active user with that ID.", msg="User.get_by_id() did not properly respond to a nonexistant ID")
			userA, uA_msg = User.get_by_id('A')
			self.assertIsNone(userA, msg="User.get_by_id() did not return None for an invalid ID")


	def test_user_edit(self):
		with userTest.app.app_context():
			user1, u1_msg = User.get_by_id(1)
			# 1 valid update
			u, msg = user1.edit(username="earlofsandwich")
			self.assertEqual(user1.username, "earlofsandwich", msg="User.edit() did not update this field.")
			# 2 valid updates
			u, msg = user1.edit(username="earlofsandwiches", email="earlofsandwich@goodeats.com")
			self.assertEqual(user1.username, "earlofsandwiches", msg="User.edit() did not update this field.")
			self.assertEqual(user1.email, "earlofsandwich@goodeats.com", msg="User.edit() did not update this field.")
			# No updates
			u, msg = user1.edit()
			self.assertEqual(msg, "User edited successfully.", msg="User.edit() did not handle an empty update operation.")
			# valid and invalid updates
			u, msg = user1.edit(username="name_is_wrong", email="earlofsandwich.goodeats.com")
			self.assertIsNone(u, msg="User.edit() did not return None when there was an invalid field.")
			self.assertEqual(user1.username, "earlofsandwiches", msg="User.edit() updated a field with a valid value, when there was an invalid value in the same transaction.")
			self.assertEqual(user1.email, "earlofsandwich@goodeats.com", msg="User.edit() updated a field with an invalid value.")

	def test_user_delete(self):
		with userTest.app.app_context():
			# valid delete
			user1, response = User.get_by_id(1)
			u1_id, response = user1.delete()
			self.assertEqual(u1_id, 1, msg="User.delete() did not return the deleted ID")

			# attempt to modify/delete deleted item
			u1_id, response = user1.delete()
			self.assertIsNone(u1_id, msg="User.delete() did not return None for a previously deleted user")
			self.assertEqual(response, "User already deleted.", msg="User.delete() did not properly respond to a previously deleted user")
			user1, response = user1.edit(username="earlofsandwich")
			self.assertIsNone(user1, msg="User.edit() did not return None when editing a deleted user")
			self.assertEqual(response, "User previously deleted.", msg="User.edit() did not properly respond to a deleted user")

	def test_user_reactivate(self):
		with userTest.app.app_context():
			user1, response = User.get_by_id(1)
			u1_id, response = user1.delete()
			self.assertEqual(u1_id, 1, msg="User.delete() did not return the deleted ID")

			user1, response = User.reactivate(1)
			self.assertFalse(user1.deleted, msg="User.reactivate() did not reactivate the account")

			user3, response = User.reactivate(3)
			self.assertFalse(user3.deleted, msg="User.reactivate() deactivated an active account")

			user5, response = User.reactivate(5)
			self.assertIsNone(user5, msg="User.reactivate() returned an incorrect value for a nonexistant user")

			userA, userA_msg = User.reactivate('A')
			self.assertIsNone(userA, msg="Wrong response to reactivating invalid id")

	def test_user_validate(self):
		with userTest.app.app_context():
			# valid user
			u = User("test_user", "test", "testerino", "test@test.com")
			valid, messages = u.validate()
			self.assertTrue(valid, msg="User.validate incorrectly labeled a valid user.")

			# invalid usernames

			# invalid firstnames

			# invalid lastnames

			# invalid emails
			u.email = "wasacsac"
			valid, messages = u.validate()
			self.assertFalse(valid, msg="User.validate did not handle invalid email.")