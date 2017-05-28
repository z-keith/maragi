from flask import Blueprint, render_template
from flask_login import current_user

from db.db_manager import DBManager, WhereClause, OrderClause, LimitClause
from forms.login_form import LoginForm

splash = Blueprint('splash', __name__, template_folder='templates')

@splash.route('/')
def index():
	db = DBManager()
	users = db.get_users()
	return render_template('index.html', users=users, loginform=LoginForm())