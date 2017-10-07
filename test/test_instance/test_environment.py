# /test/test_environment.py

def test_environment():
	import os
	
	assert os.getenv('SECRET') == "testing_secret???"
	assert os.getenv('DATABASE_URL') == "postgresql://localhost/maragi_tdd_test"
	assert os.getenv('FLASK_APP') == "run.py"

def test_config():
	import sys

	print(sys.path)

	from instance import create_app
	
	app = create_app('testing')
	
	assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] == False
	assert app.config['DEBUG'] == False
	assert app.config['CSRF_ENABLED'] == True
	assert app.config['SECRET_KEY'] == os.getenv('SECRET')
	assert app.config['SQLALCHEMY_DATABASE_URI'] == os.getenv('DATABASE_URL')