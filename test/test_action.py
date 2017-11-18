import unittest

from instance.app import create_app
from api.user import User
from api.goal import Goal
from api.action import Action

class actionTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		# actionTest.app = create_app('testing')
		pass

	def setUp(self):
		actionTest.app = create_app('testing')

	def tearDown(self):
		pass
	
	def test_action_creation(self):
		with actionTest.app.app_context():
			pass