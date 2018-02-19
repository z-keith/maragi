import unittest
import requests
from flask import url_for, current_app, json

from instance.app import create_app
from api.user_resources import ReadUser, ReadUsers, AddUser, EditUser, DeleteUser, ReactivateUser
from data import tokens

class userRouteTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# goalTest.app = create_app('testing')
		pass

	def setUp(self):
		self.app = create_app('testing')
		with self.app.app_context():
			self.test_app = current_app.test_client()

	def tearDown(self):
		pass
	
	def test_route_user_read(self):
		with self.app.app_context():
			# valid request
			response = self.test_app.post('/user/1', data={'token': tokens[1]})
			self.assertEqual(response.status_code, 200, msg='Returned status code other than success')

			# token for wrong user

			# no token

			# user does not exist

			raise NotImplementedError

	def test_route_user_reads(self):
		with self.app.app_context():
			# valid request

			# token for wrong user

			# no token

			raise NotImplementedError

	def test_route_user_add(self):
		with self.app.app_context():
			raise NotImplementedError

	def test_route_user_edit(self):
		with self.app.app_context():
			raise NotImplementedError

	def test_route_user_delete(self):
		with self.app.app_context():
			raise NotImplementedError

	def test_route_user_reactivate(self):
		with self.app.app_context():
			raise NotImplementedError

#'data' = {
#	'user_id'  : fields.Integer,
#	'username' : fields.String,
#	'email' : fields.String,
#	'firstname' : fields.String,
#	'lastname' : fields.String
#}

# print (response.status_code)
# print (json.loads(response.data))

#self.assertIsInstance(all_users, list, msg="User.get_all() did not return a list")
#self.assertEqual(test_user.add()[1], msg_user_success, msg="User 1 not added successfully")
#self.assertIsNone(user5, msg="User.reactivate() returned an incorrect value for a nonexistant user")
#self.assertTrue(valid, msg="User.validate incorrectly labeled a valid user.")			