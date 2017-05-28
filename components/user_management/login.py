from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from passlib.hash import sha512_crypt

from db.db_manager import DBManager, WhereClause, OrderClause, LimitClause
from forms.login_form import LoginForm

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	db = DBManager()
	try:
		users = db.get_users([WhereClause('username', '=', username)])
	except:
		#return 'Username not found'
		return redirect(url_for('splash.index'))

	if len(users) != 1:
		# return 'Database error - please contact support'
		return redirect(url_for('splash.index'))
			
	if not sha512_crypt.verify(password, users[0].hashed_password):
		# return 'Invalid password'
		return redirect(url_for('splash.index'))

	login_user(users[0])
	
	return redirect(url_for('dash.dashboard'))

@auth.route("/logout")
def logout():
	if current_user.get_id():
		logout_user()
	return redirect(url_for('splash.index'))

