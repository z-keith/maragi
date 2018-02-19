import unittest
import requests
from flask import url_for, current_app

from instance.app import create_app
from api.auth_resources import RequestToken

class authRouteTest(unittest.TestCase):

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
	
	def test_route_auth_request(self):
		with self.app.app_context():
			raise NotImplementedError

	def test_route_auth_validate(self):
		with self.app.app_context():
			raise NotImplementedError
