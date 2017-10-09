# /test/test_environment.py

import unittest

class environmentTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_environment(self):	
		import os	
		self.assertEqual(os.getenv('SECRET'), "testing_secret???", msg="Secret set incorrectly (or test not updated)")
		self.assertEqual(os.getenv('DATABASE_URL'), "postgresql:///maragi_test_db", msg="Database path set incorrectly (or test not updated)")
		self.assertEqual(os.getenv('FLASK_APP'), "run.py", msg="Run command set incorrectly")

	def test_config(self):
		import os
		from instance.app import create_app
		
		app = create_app('testing')
		
		self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'], msg="Track_modifications not disabled")
		self.assertTrue(app.config['CSRF_ENABLED'], msg="CSRF disabled")
		self.assertEqual(app.config['SECRET_KEY'], os.getenv('SECRET'), msg="Secret loaded incorrectly")
		self.assertEqual(app.config['SQLALCHEMY_DATABASE_URI'], os.getenv('DATABASE_URL'), msg="Database path loaded incorrectly")