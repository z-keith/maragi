from flask import Blueprint, render_template
from flask_login import current_user

from api.utils.db_manager import manager
from forms.login_form import LoginForm

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
	users_list = manager.get_users()
	return render_template('index.html', users=users_list, loginform=LoginForm())