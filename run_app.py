import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes.login import auth, login_manager
from routes.error_pages import errors
from routes.index import home
from routes.dashboard import dash
from api.api_bp import api_bp

from db.database import db
from common.user import init_users

import config

app = Flask(__name__)

login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/maragi.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(home)
app.register_blueprint(errors)
app.register_blueprint(dash)
app.register_blueprint(api_bp)#, subdomain='api')

def setup_test_db(app):
	with app.app_context():
		db.create_all()
		init_users()

if __name__ == '__main__':
	app.debug = True
	app.secret_key = config.SECRET_KEY
	app.config['SERVER_NAME'] = config.SERVER_NAME

	#setup_test_db(app)

	host = os.environ.get('IP', '0.0.0.0')
	port = int(os.environ.get('PORT', 8080))
	app.run(host=host, port=port, threaded=True)
