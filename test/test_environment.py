# /test/test_environment.py

import unittest

class environmentTest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_environment(self):	
		import os	
		assert os.getenv('SECRET') == "testing_secret???"
		assert os.getenv('DATABASE_URL') == "postgresql:///maragi_test_db"
		assert os.getenv('FLASK_APP') == "run.py"

	def test_config(self):
		import os
		from instance.app import create_app
		
		app = create_app('testing')
		
		assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] == False
		assert app.config['CSRF_ENABLED'] == True
		assert app.config['SECRET_KEY'] == os.getenv('SECRET')
		assert app.config['SQLALCHEMY_DATABASE_URI'] == os.getenv('DATABASE_URL')