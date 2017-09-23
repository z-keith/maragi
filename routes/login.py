from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from passlib.hash import sha512_crypt
import requests

from forms.login_form import LoginForm

from common.user import user_from_json

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
	if not current_user.get_id():
		logout_user()

	if request.form:
		username = request.form['username']
		password = request.form['password']
		if 'next' in request.form:
			next = request.form['next']
		else:
			next = url_for('dash.dashboard')
		
		token_response = requests.post(url_for('api.requesttoken', _external=True), data={'username' : username, 'password' : password})

		if token_response.status_code == 200:
			token = token_response.json()['token']
			user_id = token_response.json()['user_id']

			validate_response = requests.post(url_for('api.validatetoken', _external=True), data={'token' : token, 'user_id' : user_id})
			
			if validate_response.status_code == 200 and int(validate_response.json()['user_id']) == user_id:
				
				user_response = requests.get(url_for('api.getuserbyuserid', user_id=user_id, _external=True))
				
				if user_response.status_code == 200:
					user_json = user_response.json()['user']
					user = user_from_json(user_json) 	
					
					login_user(user, remember=True)
					current_user.token = token
					flash('Login successful!')

					if not safe_url(next):
						abort(400, description='unsafe next url')

					return redirect(next or url_for('home.index'))
				else:
					# user not found
					error = user_response.json()['description']
			else:
				# malformed token or returned wrong user id, or server error
				error = validate_response.json()['description']
		else:
			# login error - did not correctly generate token (username and password incorrect, or server error)
			error = token_response.json()['description']

	else:
		error = 'Please log in.'
		next = request.args.get('next')
		if not next:
			next = url_for('dash.dashboard')

	return render_template('login.html', error=error, loginform=LoginForm(next=next))
	

@auth.route("/logout")
def logout():
	if current_user.get_id():
		logout_user()
		flash('Logout successful!')
	return redirect(url_for('home.index'))

login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
	user_response = requests.get(url_for('api.getuserbyuserid', user_id=user_id, _external=True))
	user_json = user_response.json()['user']
	user = user_from_json(user_json)
	return user

def safe_url(target):
	safe = [url_for('dash.dashboard'), url_for('dash.settings'), url_for('home.index')]
	return (target in safe)