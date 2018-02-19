import unittest
import requests
from flask import url_for, current_app

from instance.app import create_app
from api.goal_resources import ReadGoal, ReadGoals, AddGoal, EditGoal, DeleteGoal, ReactivateGoal

class goalRouteTest(unittest.TestCase):

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
	
	def test_route_goal_read(self):
		with self.app.app_context():
			raise NotImplementedError

	def test_route_goal_reads(self):
		with self.app.app_context():
			raise NotImplementedError

	def test_route_goal_add(self):
		with self.app.app_context():
			raise NotImplementedError

	def test_route_goal_edit(self):
		with self.app.app_context():
			raise NotImplementedError
			
	def test_route_goal_delete(self):
		with self.app.app_context():
			raise NotImplementedError
			
	def test_route_goal_reactivate(self):
		with self.app.app_context():
			raise NotImplementedError