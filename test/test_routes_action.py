import unittest
import requests
from flask import url_for, current_app

from instance.app import create_app
from api.action_resources import ReadAction, ReadActions, AddAction, EditAction, DeleteAction, ReactivateAction

class actionRouteTest(unittest.TestCase):

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
	
	def test_route_action_read(self):
		with self.app.app_context():
			raise NotImplementedError
				
	def test_route_action_reads(self):
		with self.app.app_context():
			raise NotImplementedError
			
	def test_route_action_add(self):
		with self.app.app_context():
			raise NotImplementedError
			
	def test_route_action_edit(self):
		with self.app.app_context():
			raise NotImplementedError
			
	def test_route_action_delete(self):
		with self.app.app_context():
			raise NotImplementedError
			
	def test_route_action_reactivate(self):
		with self.app.app_context():
			raise NotImplementedError