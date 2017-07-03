from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from passlib.hash import sha512_crypt
import requests

from forms.login_form import LoginForm

from common.user import user_from_json

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['POST'])
def login():
	#if not current_user.get_id():
	logout_user()

	username = request.form['username']
	password = request.form['password']
	
	token_response = requests.post(url_for('api.requesttoken', _external=True), data={'username' : username, 'password' : password})
	response_code = token_response.status_code
	print(response_code)

	if response_code == 200:
		token = token_response.json()['token']
		validate_response = requests.post(url_for('api.validatetoken', _external=True), data={'token' : token})
		
		user_id = validate_response.json()['user_id']
		
		user_response = requests.get(url_for('api.getuserbyuserid', user_id=user_id, _external=True))
		user_json = user_response.json()['user']
		user = user_from_json(user_json) 	
		
		login_user(user, remember=True)
		current_user.token = token
	else:
		# login error
		return redirect(url_for('dash.dashboard'))
			
	return redirect(url_for('home.index'))

@auth.route("/logout")
def logout():
	if current_user.get_id():
		logout_user()
	return redirect(url_for('home.index'))

login_manager = LoginManager()
login_manager.login_view = "home.index"

@login_manager.user_loader
def load_user(user_id):
	user_response = requests.get(url_for('api.getuserbyuserid', user_id=user_id, _external=True))
	user_json = user_response.json()['user']
	user = user_from_json(user_json)
	return user