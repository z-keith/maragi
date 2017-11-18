import unittest

from instance.app import create_app
from api.user import User
from api.goal import Goal
from api.action import Action

class goalTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# goalTest.app = create_app('testing')
		pass

	def setUp(self):
		goalTest.app = create_app('testing')

	def tearDown(self):
		pass
	
	def test_goal_creation(self):
		with goalTest.app.app_context():
			pass