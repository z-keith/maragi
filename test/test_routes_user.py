import unittest
import requests
from flask import url_for, current_app

from instance.app import create_app
from api.user_resources import ReadUser, ReadUsers, AddUser, EditUser, DeleteUser, ReactivateUser

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
			response = self.test_app.post('/user/1', data={'firstname':'tom'})
		pass

	def test_route_user_reads(self):
		with self.app.app_context():
			pass

	def test_route_user_add(self):
		with self.app.app_context():
			pass

	def test_route_user_edit(self):
		with self.app.app_context():
			pass

	def test_route_user_delete(self):
		with self.app.app_context():
			pass

	def test_route_user_reactivate(self):
		with self.app.app_context():
			pass