import os
from flask import Flask, render_template
from flask_login import LoginManager, current_user

from components.user_management.login import auth
from components.error_handling.error_pages import errors
from components.splash_page.index import splash
from components.dashboard.dashboard import dash
from forms.login_form import LoginForm

from db.db_manager import DBManager

import config

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "splash.index"

@login_manager.user_loader
def load_user(user_id):
	db = DBManager()
	user = db.get_user_by_ID(user_id)
	return user

app.register_blueprint(auth)
app.register_blueprint(splash)
app.register_blueprint(errors)
app.register_blueprint(dash)

if __name__ == '__main__':
	app.debug = True
	app.secret_key = config.SECRET_KEY

	host = os.environ.get('IP', '0.0.0.0')
	port = int(os.environ.get('PORT', 8080))
	app.run(host=host, port=port)



