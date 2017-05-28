import os
from flask import Flask
from flask_login import LoginManager #, current_user

from routes.login import auth
from routes.error_pages import errors
from routes.index import home
from routes.dashboard import dash
from api.api_bp import api_bp

from forms.login_form import LoginForm

from api.utils.db_manager import DBManager

import config

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "home.index"

@login_manager.user_loader
def load_user(user_id):
	db = DBManager()
	user = db.get_user_by_ID(user_id)
	return user

app.register_blueprint(auth)
app.register_blueprint(home)
app.register_blueprint(errors)
app.register_blueprint(dash)
app.register_blueprint(api_bp, subdomain='api')

if __name__ == '__main__':
	app.debug = True
	app.secret_key = config.SECRET_KEY
	app.config['SERVER_NAME'] = config.SERVER_NAME

	host = os.environ.get('IP', '0.0.0.0')
	port = int(os.environ.get('PORT', 8080))
	app.run(host=host, port=port)
